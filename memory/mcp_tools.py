"""Synchronous tool logic for the MCP server, scoped to one coach.

Every function receives the coach explicitly and only touches that coach's athletes.
The MCP layer (management command ``run_mcp_server``) wraps these for async use.
"""
from datetime import date

from django.db.models import Q

from training import plan_changes
from training.models import Athlete, ChangeSource, SessionStatus, TrainingSession

from . import services
from .models import AthleteMemory, MemoryCategory, MemorySource, MemoryStatus

RECENT_SESSIONS = 5
UPCOMING_SESSIONS = 10
SEARCH_LIMIT = 30


def _athlete(coach, athlete_id):
    try:
        return Athlete.objects.get(pk=athlete_id, coach=coach)
    except Athlete.DoesNotExist as exc:
        raise ValueError(f"No athlete with id {athlete_id} for this coach.") from exc


def _memory_dict(memory):
    return {
        "id": memory.pk, "category": memory.category, "content": memory.content,
        "exercise": memory.exercise or None, "reason": memory.reason or None,
        "observed_on": memory.observed_on.isoformat(), "status": memory.status, "source": memory.source,
    }


def list_athletes(coach):
    return [{"id": a.pk, "name": a.name} for a in Athlete.objects.filter(coach=coach)]


def get_athlete_context(coach, athlete_id):
    """Active memories plus the most recent sessions with prescribed and actual sets."""
    athlete = _athlete(coach, athlete_id)
    memories = athlete.memories.filter(status=MemoryStatus.ACTIVE)
    sessions = (TrainingSession.objects.filter(plan__athlete=athlete, scheduled_date__lte=date.today())
        .select_related("plan").prefetch_related("sets__performance").order_by("-scheduled_date", "-pk")
        [:RECENT_SESSIONS])
    recent = []
    for session in sessions:
        sets = []
        for item in session.sets.all():
            log = getattr(item, "performance", None)
            sets.append({
                "exercise": item.exercise, "planned": f"{item.weight_kg} kg x {item.reps}",
                "actual": f"{log.weight_kg} kg x {log.reps}" if log else None,
                "rpe": str(log.rpe) if log and log.rpe is not None else None,
            })
        recent.append({"date": session.scheduled_date.isoformat(), "plan": session.plan.title,
            "session": session.title, "sets": sets})
    upcoming = (TrainingSession.objects.filter(plan__athlete=athlete, scheduled_date__gt=date.today(),
        status=SessionStatus.PLANNED).select_related("plan").order_by("scheduled_date", "pk")[:UPCOMING_SESSIONS])
    return {
        "athlete": {"id": athlete.pk, "name": athlete.name},
        "active_memories": [_memory_dict(m) for m in memories],
        "pending_proposals": athlete.memories.filter(status=MemoryStatus.PROPOSED).count(),
        "recent_sessions": recent,
        "upcoming_sessions": [{"session_id": s.pk, "date": s.scheduled_date.isoformat(), "plan": s.plan.title,
            "plan_version": s.plan.version, "session": s.title} for s in upcoming],
    }


def search_memories(coach, query, athlete_id=None, include_resolved=True):
    statuses = [MemoryStatus.ACTIVE] + ([MemoryStatus.RESOLVED] if include_resolved else [])
    memories = AthleteMemory.objects.filter(athlete__coach=coach, status__in=statuses)
    if athlete_id is not None:
        memories = memories.filter(athlete=_athlete(coach, athlete_id))
    for word in query.split():
        memories = memories.filter(Q(content__icontains=word) | Q(exercise__icontains=word)
            | Q(reason__icontains=word))
    return [{**_memory_dict(m), "athlete_id": m.athlete_id, "athlete_name": m.athlete.name}
        for m in memories.select_related("athlete")[:SEARCH_LIMIT]]


def _write(coach, athlete_id, source, category, content, exercise="", reason="", observed_on=None):
    athlete = _athlete(coach, athlete_id)
    data = services.MemoryInput(category=category, content=content, exercise=exercise or "",
        reason=reason or "", observed_on=date.fromisoformat(observed_on) if observed_on else None)
    try:
        memory = services.create_memory(coach, athlete, data, source)
    except services.DuplicateMemoryError as exc:
        return {"saved": False, "reason": "duplicate", "existing": _memory_dict(exc.existing)}
    except services.MemoryRuleError as exc:
        return {"saved": False, "reason": str(exc)}
    return {"saved": True, "memory": _memory_dict(memory)}


def propose_memory(coach, athlete_id, category, content, reason, exercise="", observed_on=None):
    return _write(coach, athlete_id, MemorySource.AI_PROPOSAL, category, content, exercise, reason, observed_on)


def save_memory_on_coach_request(coach, athlete_id, category, content, exercise="", observed_on=None):
    return _write(coach, athlete_id, MemorySource.AI_COACH_REQUEST, category, content, exercise, "", observed_on)



def propose_session_change(coach, athlete_id, session_id, kind, reason, new_date=None):
    """Create a move/skip proposal for one future, unlogged session; the coach approves it in the app."""
    athlete = _athlete(coach, athlete_id)
    try:
        session = TrainingSession.objects.get(pk=session_id, plan__athlete=athlete)
    except TrainingSession.DoesNotExist as exc:
        raise ValueError(f"No session with id {session_id} for this athlete.") from exc
    try:
        change = plan_changes.propose(coach, session, kind, date.fromisoformat(new_date) if new_date else None,
            reason, source=ChangeSource.AI)
    except plan_changes.PlanChangeError as exc:
        return {"saved": False, "reason": str(exc)}
    return {"saved": True, "change_id": change.pk, "status": change.status, "base_version": change.base_version,
        "note": "The coach reviews the before/after view and approves or rejects it in the app."}


CATEGORIES = ", ".join(f"{value} ({label})" for value, label in MemoryCategory.choices)
