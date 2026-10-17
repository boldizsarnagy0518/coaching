"""Synchronous tool logic for the MCP server, scoped to one coach.

Every function receives the coach explicitly and only touches that coach's athletes.
The MCP layer (management command ``run_mcp_server``) wraps these for async use.
"""
import logging
import time
import uuid
from datetime import date

from django.db import close_old_connections
from django.db.models import Q

from coaching.observability import log_event, request_id_var
from training import plan_changes
from training.models import Athlete, ChangeSource, SessionStatus, TrainingSession

from . import services
from .models import AthleteMemory, MemoryCategory, MemorySource, MemoryStatus

logger = logging.getLogger("coaching.mcp")
RECENT_SESSIONS = 5
UPCOMING_SESSIONS = 10
SEARCH_LIMIT = 30


class ToolFailure(RuntimeError):
    """An unexpected error, reported to the AI client without internal details."""


def call_tool_safely(name, func, coach, *args, **kwargs):
    """Run one tool call with a fresh DB connection, a correlation id, timing and error isolation.

    ValueError carries a message meant for the AI client (bad id, bad date, rule violation).
    Anything else is logged with a traceback and reported as a generic failure with a reference.
    """
    call_id = uuid.uuid4().hex[:12]
    token = request_id_var.set(f"mcp-{call_id}")
    started = time.perf_counter()
    outcome = "ok"
    # The MCP process is long-lived; drop connections that went stale between calls.
    close_old_connections()
    try:
        result = func(coach, *args, **kwargs)
        if isinstance(result, dict) and result.get("saved") is False:
            outcome = "refused"
        return result
    except ValueError:
        outcome = "invalid_input"
        raise
    except Exception as exc:
        outcome = "error"
        logger.exception("tool %s failed", name)
        raise ToolFailure(f"Internal error in {name}; reference mcp-{call_id}.") from exc
    finally:
        log_event("mcp.tool", tool=name, outcome=outcome, duration_ms=round((time.perf_counter() - started) * 1000, 1))
        close_old_connections()
        request_id_var.reset(token)


def _parse_date(value, field):
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be an ISO date (YYYY-MM-DD).") from exc


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
        reason=reason or "", observed_on=_parse_date(observed_on, "observed_on"))
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
    """Create a move, skip or move_rest proposal for one session; the coach approves it in the app."""
    athlete = _athlete(coach, athlete_id)
    try:
        session = TrainingSession.objects.get(pk=session_id, plan__athlete=athlete)
    except TrainingSession.DoesNotExist as exc:
        raise ValueError(f"No session with id {session_id} for this athlete.") from exc
    try:
        change = plan_changes.propose(coach, session, kind, _parse_date(new_date, "new_date"),
            reason, source=ChangeSource.AI)
    except plan_changes.PlanChangeError as exc:
        return {"saved": False, "reason": str(exc)}
    return {"saved": True, "change_id": change.pk, "status": change.status, "base_version": change.base_version,
        "note": "The coach reviews the before/after view and approves or rejects it in the app."}


def propose_reschedule(coach, athlete_id, moves, reason):
    """Propose several session moves as one batch (e.g. a new weekly schedule).

    ``moves`` is a list of {"session_id": int, "new_date": "YYYY-MM-DD"}; all sessions must belong to one plan.
    """
    athlete = _athlete(coach, athlete_id)
    if not isinstance(moves, list) or not moves:
        raise ValueError("moves must be a non-empty list of {session_id, new_date}.")
    pairs = []
    for move in moves:
        try:
            session = TrainingSession.objects.get(pk=int(move["session_id"]), plan__athlete=athlete)
        except (KeyError, TypeError, ValueError, TrainingSession.DoesNotExist) as exc:
            raise ValueError(f"Unknown or invalid session in moves: {move!r}") from exc
        pairs.append((session, _parse_date(move.get("new_date"), "new_date")))
    if len({session.plan_id for session, _ in pairs}) != 1:
        raise ValueError("All sessions of one reschedule must belong to the same plan.")
    try:
        changes = plan_changes.propose_batch(coach, pairs[0][0].plan, pairs, reason, source=ChangeSource.AI)
    except plan_changes.PlanChangeError as exc:
        return {"saved": False, "reason": str(exc)}
    return {"saved": True, "change_id": changes[0].pk, "moves": len(changes), "base_version": changes[0].base_version,
        "note": "The coach reviews the before/after view and approves or rejects the whole batch in the app."}


CATEGORIES = ", ".join(f"{value} ({label})" for value, label in MemoryCategory.choices)
