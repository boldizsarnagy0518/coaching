"""Memory write rules shared by the web UI and the MCP tools.

Selection rules keep the memory small and useful:
- every entry needs a known category and a short, specific statement;
- AI-initiated entries are only proposals and need a reason and coach approval;
- near-duplicates of an existing open entry are rejected;
- the number of pending proposals per athlete is capped.
"""
import re
from dataclasses import dataclass
from datetime import date
from difflib import SequenceMatcher

from django.db import transaction
from django.utils import timezone

from coaching.observability import log_event
from training.models import Athlete

from .models import AthleteMemory, MemoryCategory, MemorySource, MemoryStatus

MIN_CONTENT_LENGTH = 12
MAX_CONTENT_LENGTH = 300
MIN_REASON_LENGTH = 12
MAX_PENDING_PROPOSALS = 10
DUPLICATE_SIMILARITY = 0.85
OPEN_STATUSES = (MemoryStatus.PROPOSED, MemoryStatus.ACTIVE)


class MemoryRuleError(ValueError):
    """Raised when an entry does not meet the selection rules; the message is user-facing (Hungarian)."""


class DuplicateMemoryError(MemoryRuleError):
    def __init__(self, existing):
        self.existing = existing
        super().__init__(f"Már van hasonló bejegyzés (#{existing.pk}): {existing.content}")


@dataclass(frozen=True)
class MemoryInput:
    category: str
    content: str
    exercise: str = ""
    reason: str = ""
    observed_on: date | None = None


def normalize(text):
    return re.sub(r"[^\w]+", " ", text.lower()).strip()


def find_duplicate(athlete, category, content):
    """Return an open entry in the same category that says essentially the same thing."""
    target = normalize(content)
    for existing in athlete.memories.filter(category=category, status__in=OPEN_STATUSES):
        other = normalize(existing.content)
        if target == other or target in other or other in target:
            return existing
        if SequenceMatcher(None, target, other).ratio() >= DUPLICATE_SIMILARITY:
            return existing
    return None


def _validate(athlete, data, source):
    if data.category not in MemoryCategory.values:
        raise MemoryRuleError("Ismeretlen kategória. Válassz a megadott kategóriák közül.")
    content = " ".join(data.content.split())
    if len(content) < MIN_CONTENT_LENGTH:
        raise MemoryRuleError("Túl rövid bejegyzés: írd le konkrétan, mit kell megjegyezni.")
    if len(content) > MAX_CONTENT_LENGTH:
        raise MemoryRuleError("Legfeljebb 300 karakteres, tömör bejegyzés menthető.")
    reason = " ".join(data.reason.split())
    if source == MemorySource.AI_PROPOSAL:
        if len(reason) < MIN_REASON_LENGTH:
            raise MemoryRuleError("AI-javaslathoz indoklás kell: miért lesz ez később is fontos?")
        pending = athlete.memories.filter(status=MemoryStatus.PROPOSED).count()
        if pending >= MAX_PENDING_PROPOSALS:
            raise MemoryRuleError("Túl sok jóváhagyásra váró javaslat; előbb az edző nézze át őket.")
    duplicate = find_duplicate(athlete, data.category, content)
    if duplicate:
        raise DuplicateMemoryError(duplicate)
    return content, reason[:MAX_CONTENT_LENGTH]


@transaction.atomic
def create_memory(coach, athlete, data, source):
    """Create an entry for the coach's own athlete according to its source.

    Coach entries and explicit coach requests from an AI chat are active at once;
    AI-initiated proposals wait for coach review.
    """
    if athlete.coach_id != coach.pk:
        raise PermissionError("Athlete does not belong to this coach.")
    # Lock the athlete row so concurrent writes see each other's duplicates and pending counts.
    Athlete.objects.select_for_update().get(pk=athlete.pk)
    try:
        content, reason = _validate(athlete, data, source)
    except MemoryRuleError as exc:
        rule = "duplicate" if isinstance(exc, DuplicateMemoryError) else "invalid"
        log_event("memory.refused", athlete=athlete.pk, source=source, category=data.category, rule=rule)
        raise
    status = MemoryStatus.PROPOSED if source == MemorySource.AI_PROPOSAL else MemoryStatus.ACTIVE
    memory = AthleteMemory.objects.create(
        athlete=athlete, category=data.category, content=content, exercise=data.exercise.strip()[:120],
        reason=reason, observed_on=data.observed_on or timezone.localdate(), status=status, source=source,
        created_by=coach,
    )
    log_event("memory.created", memory=memory.pk, athlete=athlete.pk, source=source, status=status,
        category=data.category)
    return memory


def _review(coach, memory, allowed_from, new_status):
    if memory.athlete.coach_id != coach.pk:
        raise PermissionError("Memory does not belong to this coach.")
    if memory.status not in allowed_from:
        raise MemoryRuleError("Ez a bejegyzés ebben az állapotban nem módosítható.")
    memory.status = new_status
    memory.reviewed_by = coach
    memory.reviewed_at = timezone.now()
    memory.save(update_fields=["status", "reviewed_by", "reviewed_at"])
    log_event("memory.reviewed", memory=memory.pk, athlete=memory.athlete_id, status=new_status)
    return memory


def approve(coach, memory):
    return _review(coach, memory, [MemoryStatus.PROPOSED], MemoryStatus.ACTIVE)


def reject(coach, memory):
    return _review(coach, memory, [MemoryStatus.PROPOSED], MemoryStatus.REJECTED)


def resolve(coach, memory):
    """Mark an active entry as no longer current; it stays visible as history."""
    return _review(coach, memory, [MemoryStatus.ACTIVE], MemoryStatus.RESOLVED)


def reactivate(coach, memory):
    return _review(coach, memory, [MemoryStatus.RESOLVED], MemoryStatus.ACTIVE)
