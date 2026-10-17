"""Propose, preview and apply session changes with plan versioning.

Rules:
- only sessions without any logged set can be moved or skipped (logged work is never rewritten);
- a partially logged session can only have its remaining (unlogged) sets moved to a new
  continuation session; the logged sets stay where they are;
- several moves can be proposed together as one batch (e.g. a new weekly schedule); a batch is
  approved or rejected as a whole and produces a single new plan version;
- a proposal records the plan version it was based on; approving it after the plan changed
  marks it stale instead of applying it;
- applying a change increments the plan version and keeps the before/after values on the record.
"""
import uuid
from dataclasses import dataclass, field

from django.db import transaction
from django.db.models import Count, Q
from django.utils import timezone

from coaching.observability import log_event

from .models import ChangeKind, ChangeSource, ChangeStatus, PlanChange, SessionStatus, TrainingPlan, TrainingSession

MAX_PENDING_CHANGES = 10
MAX_BATCH_SIZE = 20
MIN_AI_REASON = 12


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
    note: str = ""
    is_new: bool = field(default=False)


def _logged_counts(session):
    counts = session.sets.aggregate(total=Count("pk"), logged=Count("pk", filter=Q(performance__isnull=False)))
    return counts["total"], counts["logged"]


def _check_session(session, kind):
    if session.status == SessionStatus.SKIPPED:
        raise PlanChangeError("Ez az edzés már ki van hagyva.")
    total, logged = _logged_counts(session)
    if kind == ChangeKind.MOVE_REST:
        if logged == 0:
            raise PlanChangeError("Még nincs naplózott sorozat; az egész edzést helyezd át.")
        if logged == total:
            raise PlanChangeError("Nincs hátralévő, naplózatlan sorozat.")
    elif logged:
        raise PlanChangeError("Már naplózott edzés nem helyezhető át és nem hagyható ki; "
            "a hátralévő sorozatokat külön áthelyezheted. A teljesítés megmarad.")


def _pending_groups(plan):
    pending = plan.changes.filter(status=ChangeStatus.PROPOSED)
    return pending.filter(batch__isnull=True).count() + pending.exclude(batch__isnull=True).values("batch").distinct().count()


def _validate_item(plan, session, kind, new_date):
    if session.plan_id != plan.pk:
        raise PlanChangeError("Az edzés nem ehhez a tervhez tartozik.")
    if kind not in ChangeKind.values:
        raise PlanChangeError("Ismeretlen módosítástípus.")
    _check_session(session, kind)
    if kind in (ChangeKind.MOVE, ChangeKind.MOVE_REST):
        if new_date is None:
            raise PlanChangeError("Áthelyezéshez új dátum kell.")
        if new_date == session.scheduled_date:
            raise PlanChangeError("Az új dátum megegyezik a jelenlegivel.")
        return new_date
    return None


def _validate_common(plan, coach, reason, source, sessions):
    if plan.athlete.coach_id != coach.pk:
        raise PermissionError("Session does not belong to this coach.")
    reason = " ".join(reason.split())
    if source == ChangeSource.AI and len(reason) < MIN_AI_REASON:
        raise PlanChangeError("AI-javaslathoz indoklás kell.")
    if _pending_groups(plan) >= MAX_PENDING_CHANGES:
        raise PlanChangeError("Túl sok jóváhagyásra váró módosítás; előbb nézd át őket.")
    if plan.changes.filter(status=ChangeStatus.PROPOSED, session__in=sessions).exists():
        raise PlanChangeError("Erre az edzésre már van jóváhagyásra váró módosítás.")
    return reason[:300]


@transaction.atomic
def propose(coach, session, kind, new_date=None, reason="", source=ChangeSource.COACH):
    plan = TrainingPlan.objects.select_for_update().get(pk=session.plan_id)
    reason = _validate_common(plan, coach, reason, source, [session])
    new_date = _validate_item(plan, session, kind, new_date)
    change = PlanChange.objects.create(plan=plan, session=session, kind=kind, new_date=new_date,
        old_date=session.scheduled_date, base_version=plan.version, reason=reason, source=source, created_by=coach)
    log_event("plan_change.proposed", change=change.pk, plan=plan.pk, session=session.pk, kind=kind, source=source,
        base_version=plan.version)
    return change


@transaction.atomic
def propose_batch(coach, plan, moves, reason="", source=ChangeSource.COACH):
    """Propose several session moves at once; ``moves`` is a list of (session, new_date).

    Unchanged dates are ignored. Returns the created changes (all sharing one batch id).
    """
    plan = TrainingPlan.objects.select_for_update().get(pk=plan.pk)
    moves = [(session, new_date) for session, new_date in moves if new_date and new_date != session.scheduled_date]
    if not moves:
        raise PlanChangeError("Egyetlen dátum sem változott.")
    if len(moves) > MAX_BATCH_SIZE:
        raise PlanChangeError(f"Egyszerre legfeljebb {MAX_BATCH_SIZE} edzés helyezhető át.")
    reason = _validate_common(plan, coach, reason, source, [session for session, _ in moves])
    batch = uuid.uuid4()
    changes = []
    for session, new_date in moves:
        _validate_item(plan, session, ChangeKind.MOVE, new_date)
        changes.append(PlanChange.objects.create(plan=plan, session=session, kind=ChangeKind.MOVE, new_date=new_date,
            old_date=session.scheduled_date, base_version=plan.version, reason=reason, source=source,
            created_by=coach, batch=batch))
    log_event("plan_change.batch_proposed", plan=plan.pk, size=len(changes), source=source, base_version=plan.version)
    return changes


def group(change):
    """The change itself, or every change of its batch."""
    if change.batch is None:
        return [change]
    return list(PlanChange.objects.filter(batch=change.batch).select_related("session").order_by("old_date", "pk"))


def preview(change):
    """Before/after rows for every session of the plan, with same-day conflicts flagged."""
    items = {item.session_id: item for item in group(change)}
    sessions = list(change.plan.sessions.annotate(
        logged=Count("sets", filter=Q(sets__performance__isnull=False)), total=Count("sets")))
    rows = []
    for session in sessions:
        item = items.get(session.pk)
        after = item.new_date if item and item.kind == ChangeKind.MOVE else session.scheduled_date
        skipped_after = session.status == SessionStatus.SKIPPED or bool(item and item.kind == ChangeKind.SKIP)
        note = ""
        if item and item.kind == ChangeKind.MOVE_REST:
            note = f"{session.logged} naplózott sorozat marad, {session.total - session.logged} átkerül"
        rows.append(PreviewRow(session, session.scheduled_date, after, skipped_after, changed=bool(item),
            same_day_conflict=False, note=note))
        if item and item.kind == ChangeKind.MOVE_REST:
            continuation = TrainingSession(plan=change.plan, title=_continuation_title(session),
                scheduled_date=item.new_date)
            rows.append(PreviewRow(continuation, None, item.new_date, False, changed=True, same_day_conflict=False,
                note=f"új edzés {session.total - session.logged} sorozattal", is_new=True))
    active_dates = [row.after for row in rows if not row.skipped_after]
    rows = [PreviewRow(**{**row.__dict__, "same_day_conflict": row.changed and not row.skipped_after
        and row.after != row.before and active_dates.count(row.after) > 1}) for row in rows]
    return sorted(rows, key=lambda row: (row.after, row.session.pk or 0))


def _continuation_title(session):
    return f"{session.title} (folytatás)"[:120]


def _review(coach, change):
    if change.plan.athlete.coach_id != coach.pk:
        raise PermissionError("Change does not belong to this coach.")
    if change.status != ChangeStatus.PROPOSED:
        raise PlanChangeError("Ez a módosítás már le van zárva.")


def approve(coach, change):
    """Apply the change (or its whole batch) if the plan has not changed since the proposal.

    Otherwise every item is marked stale and nothing is applied.
    """
    error = _apply(coach, change)
    if error:
        raise PlanChangeError(error)
    return change


def _close(items, coach, status, **extra):
    now = timezone.now()
    for item in items:
        item.status, item.reviewed_by, item.reviewed_at = status, coach, now
        for name, value in extra.items():
            setattr(item, name, value)
        item.save()


@transaction.atomic
def _apply(coach, change):
    # Returns an error message instead of raising, so the stale status is committed.
    plan = TrainingPlan.objects.select_for_update().get(pk=change.plan_id)
    change.refresh_from_db()
    _review(coach, change)
    items = group(change)
    error = None
    if plan.version != change.base_version:
        error = "A terv a javaslat óta megváltozott; a javaslat elavult, készíts újat."
    else:
        try:
            for item in items:
                _check_session(TrainingSession.objects.get(pk=item.session_id), item.kind)
        except PlanChangeError as exc:
            error = f"{exc} A javaslat elavult."
    if error:
        _close(items, coach, ChangeStatus.STALE)
        log_event("plan_change.stale", change=change.pk, plan=plan.pk, size=len(items),
            base_version=change.base_version, plan_version=plan.version)
        return error
    plan.version += 1
    plan.save(update_fields=["version"])
    for item in items:
        session = TrainingSession.objects.get(pk=item.session_id)
        extra = {}
        if item.kind == ChangeKind.MOVE:
            session.scheduled_date = item.new_date
            session.save(update_fields=["scheduled_date"])
        elif item.kind == ChangeKind.SKIP:
            session.status = SessionStatus.SKIPPED
            session.save(update_fields=["status"])
        else:
            continuation = TrainingSession.objects.create(plan=plan, title=_continuation_title(session),
                scheduled_date=item.new_date)
            moved = session.sets.filter(performance__isnull=True).update(session=continuation)
            extra = {"created_session": continuation, "moved_sets": moved}
        _close([item], coach, ChangeStatus.APPROVED, result_version=plan.version, **extra)
    log_event("plan_change.approved", change=change.pk, plan=plan.pk, size=len(items), version=plan.version)
    return None


@transaction.atomic
def reject(coach, change):
    change.refresh_from_db()
    _review(coach, change)
    items = group(change)
    _close(items, coach, ChangeStatus.REJECTED)
    log_event("plan_change.rejected", change=change.pk, plan=change.plan_id, size=len(items))
    return change
