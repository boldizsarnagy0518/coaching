"""Propose, preview and apply session changes with plan versioning.

Rules:
- only sessions without any logged set can be moved or skipped (logged work is never rewritten);
- a proposal records the plan version it was based on; approving it after the plan changed
  marks it stale instead of applying it;
- applying a change increments the plan version and keeps the before/after values on the record.
"""
from dataclasses import dataclass

from django.db import transaction
from django.utils import timezone

from coaching.observability import log_event

from .models import ChangeKind, ChangeSource, ChangeStatus, PlanChange, SessionStatus, TrainingPlan, TrainingSession

MAX_PENDING_CHANGES = 10


class PlanChangeError(ValueError):
    """Raised when a change breaks a rule; the message is user-facing (Hungarian)."""


@dataclass(frozen=True)
class PreviewRow:
    session: TrainingSession
    before: object
    after: object
    skipped_after: bool
    changed: bool
    same_day_conflict: bool


def _check_session(session):
    if session.status == SessionStatus.SKIPPED:
        raise PlanChangeError("Ez az edzés már ki van hagyva.")
    if session.sets.filter(performance__isnull=False).exists():
        raise PlanChangeError("Már naplózott edzés nem helyezhető át és nem hagyható ki; a teljesítés megmarad.")


@transaction.atomic
def propose(coach, session, kind, new_date=None, reason="", source=ChangeSource.COACH):
    plan = TrainingPlan.objects.select_for_update().get(pk=session.plan_id)
    if plan.athlete.coach_id != coach.pk:
        raise PermissionError("Session does not belong to this coach.")
    if kind not in ChangeKind.values:
        raise PlanChangeError("Ismeretlen módosítástípus.")
    _check_session(session)
    if kind == ChangeKind.MOVE:
        if new_date is None:
            raise PlanChangeError("Áthelyezéshez új dátum kell.")
        if new_date == session.scheduled_date:
            raise PlanChangeError("Az új dátum megegyezik a jelenlegivel.")
    else:
        new_date = None
    reason = " ".join(reason.split())
    if source == ChangeSource.AI and len(reason) < 12:
        raise PlanChangeError("AI-javaslathoz indoklás kell.")
    if plan.changes.filter(status=ChangeStatus.PROPOSED).count() >= MAX_PENDING_CHANGES:
        raise PlanChangeError("Túl sok jóváhagyásra váró módosítás; előbb nézd át őket.")
    if plan.changes.filter(status=ChangeStatus.PROPOSED, session=session).exists():
        raise PlanChangeError("Erre az edzésre már van jóváhagyásra váró módosítás.")
    change = PlanChange.objects.create(plan=plan, session=session, kind=kind, new_date=new_date,
        old_date=session.scheduled_date, base_version=plan.version, reason=reason[:300], source=source,
        created_by=coach)
    log_event("plan_change.proposed", change=change.pk, plan=plan.pk, session=session.pk, kind=kind, source=source,
        base_version=plan.version)
    return change


def preview(change):
    """Before/after rows for every session of the plan, with same-day conflicts flagged."""
    sessions = list(change.plan.sessions.all())
    rows = []
    for session in sessions:
        is_target = session.pk == change.session_id
        after = change.new_date if is_target and change.kind == ChangeKind.MOVE else session.scheduled_date
        skipped_after = session.status == SessionStatus.SKIPPED or (is_target and change.kind == ChangeKind.SKIP)
        conflict = (is_target and change.kind == ChangeKind.MOVE and any(
            other.pk != session.pk and other.scheduled_date == after and other.status != SessionStatus.SKIPPED
            for other in sessions))
        rows.append(PreviewRow(session, session.scheduled_date, after, skipped_after,
            changed=is_target, same_day_conflict=conflict))
    return sorted(rows, key=lambda row: (row.after, row.session.pk))


def _review(coach, change):
    if change.plan.athlete.coach_id != coach.pk:
        raise PermissionError("Change does not belong to this coach.")
    if change.status != ChangeStatus.PROPOSED:
        raise PlanChangeError("Ez a módosítás már le van zárva.")
    change.reviewed_by = coach
    change.reviewed_at = timezone.now()


def approve(coach, change):
    """Apply the change if the plan has not changed since the proposal; otherwise mark it stale."""
    error = _apply(coach, change)
    if error:
        raise PlanChangeError(error)
    return change


@transaction.atomic
def _apply(coach, change):
    # Returns an error message instead of raising, so the stale status is committed.
    plan = TrainingPlan.objects.select_for_update().get(pk=change.plan_id)
    change.refresh_from_db()
    _review(coach, change)
    session = TrainingSession.objects.get(pk=change.session_id)
    error = None
    if plan.version != change.base_version:
        error = "A terv a javaslat óta megváltozott; a javaslat elavult, készíts újat."
    else:
        try:
            _check_session(session)
        except PlanChangeError as exc:
            error = f"{exc} A javaslat elavult."
    if error:
        change.status = ChangeStatus.STALE
        change.save(update_fields=["status", "reviewed_by", "reviewed_at"])
        log_event("plan_change.stale", change=change.pk, plan=plan.pk, base_version=change.base_version,
            plan_version=plan.version)
        return error
    if change.kind == ChangeKind.MOVE:
        session.scheduled_date = change.new_date
    else:
        session.status = SessionStatus.SKIPPED
    session.save(update_fields=["scheduled_date", "status"])
    plan.version += 1
    plan.save(update_fields=["version"])
    change.status = ChangeStatus.APPROVED
    change.result_version = plan.version
    change.save(update_fields=["status", "reviewed_by", "reviewed_at", "result_version"])
    log_event("plan_change.approved", change=change.pk, plan=plan.pk, version=plan.version)
    return None


def reject(coach, change):
    _review(coach, change)
    change.status = ChangeStatus.REJECTED
    change.save(update_fields=["status", "reviewed_by", "reviewed_at"])
    log_event("plan_change.rejected", change=change.pk, plan=change.plan_id)
    return change
