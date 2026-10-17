"""Curated, per-athlete coaching memory.

Only durable, coaching-relevant facts belong here (pain, technique issues,
preferences, constraints, responses to training, goals, coach decisions).
Session numbers already live in the training log and are not copied here.
"""
from django.conf import settings
from django.db import models
from django.utils import timezone

from training.models import Athlete


class MemoryCategory(models.TextChoices):
    PAIN_OR_INJURY = "pain_injury", "Fájdalom / sérülés"
    TECHNIQUE = "technique", "Technikai probléma"
    PREFERENCE = "preference", "Preferencia"
    CONSTRAINT = "constraint", "Időbeosztás / eszköz / körülmény"
    RESPONSE = "response", "Reakció az edzésre"
    GOAL = "goal", "Cél / verseny"
    DECISION = "decision", "Edzői döntés"


class MemoryStatus(models.TextChoices):
    PROPOSED = "proposed", "Javaslat – jóváhagyásra vár"
    ACTIVE = "active", "Aktív"
    RESOLVED = "resolved", "Lezárt / már nem aktuális"
    REJECTED = "rejected", "Elutasítva"


class MemorySource(models.TextChoices):
    COACH = "coach", "Edző, közvetlenül"
    AI_COACH_REQUEST = "ai_coach_request", "AI-chat, az edző kérésére"
    AI_PROPOSAL = "ai_proposal", "AI-javaslat"


class AthleteMemory(models.Model):
    athlete = models.ForeignKey(Athlete, related_name="memories", on_delete=models.PROTECT)
    category = models.CharField("Kategória", max_length=20, choices=MemoryCategory.choices)
    status = models.CharField(max_length=10, choices=MemoryStatus.choices, default=MemoryStatus.ACTIVE)
    source = models.CharField(max_length=20, choices=MemorySource.choices, default=MemorySource.COACH)
    content = models.CharField("Mit kell megjegyezni?", max_length=300)
    exercise = models.CharField("Érintett gyakorlat (opcionális)", max_length=120, blank=True)
    # Why the fact is worth keeping; required for AI proposals so the coach can judge them.
    reason = models.CharField("Miért fontos? (opcionális)", max_length=300, blank=True)
    observed_on = models.DateField("Mikor derült ki?", default=timezone.localdate)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", null=True, blank=True,
        on_delete=models.PROTECT)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    # Last manual edit by the coach; the previous wording is not kept.
    edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", null=True, blank=True,
        on_delete=models.PROTECT)
    edited_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-observed_on", "-pk"]
        indexes = [models.Index(fields=["athlete", "status"])]
        constraints = [
            models.CheckConstraint(condition=~models.Q(content=""), name="memory_content_not_empty"),
        ]

    def __str__(self):
        return f"{self.athlete} · {self.get_category_display()}: {self.content[:40]}"
