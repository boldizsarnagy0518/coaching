import uuid
from decimal import Decimal

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Athlete(models.Model):
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField("Sportoló neve", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name", "pk"]

    def __str__(self):
        return self.name


class TrainingPlan(models.Model):
    athlete = models.ForeignKey(Athlete, related_name="plans", on_delete=models.PROTECT)
    title = models.CharField("Terv neve", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    # Incremented by every approved PlanChange; proposals record the version they were based on.
    version = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return f"{self.title} (v{self.version})"


class SessionStatus(models.TextChoices):
    PLANNED = "planned", "Tervezett"
    SKIPPED = "skipped", "Kihagyva"


class TrainingSession(models.Model):
    plan = models.ForeignKey(TrainingPlan, related_name="sessions", on_delete=models.PROTECT)
    title = models.CharField("Edzés neve", max_length=120)
    scheduled_date = models.DateField("Tervezett dátum")
    status = models.CharField(max_length=10, choices=SessionStatus.choices, default=SessionStatus.PLANNED)

    class Meta:
        ordering = ["scheduled_date", "pk"]

    def __str__(self):
        return f"{self.title} · {self.scheduled_date.isoformat()}"


class ChangeKind(models.TextChoices):
    MOVE = "move", "Áthelyezés"
    SKIP = "skip", "Kihagyás"


class ChangeStatus(models.TextChoices):
    PROPOSED = "proposed", "Jóváhagyásra vár"
    APPROVED = "approved", "Jóváhagyva"
    REJECTED = "rejected", "Elutasítva"
    STALE = "stale", "Elavult – a terv közben megváltozott"


class ChangeSource(models.TextChoices):
    COACH = "coach", "Edző"
    AI = "ai", "AI-javaslat"


class PlanChange(models.Model):
    """A proposed change to one session; approved changes form the plan's version history.

    The before/after values are stored on the record, so history stays readable even after
    later changes, and logged performance is never touched.
    """
    plan = models.ForeignKey(TrainingPlan, related_name="changes", on_delete=models.PROTECT)
    session = models.ForeignKey(TrainingSession, related_name="changes", on_delete=models.PROTECT)
    kind = models.CharField(max_length=10, choices=ChangeKind.choices)
    status = models.CharField(max_length=10, choices=ChangeStatus.choices, default=ChangeStatus.PROPOSED)
    source = models.CharField(max_length=10, choices=ChangeSource.choices, default=ChangeSource.COACH)
    base_version = models.PositiveIntegerField()
    old_date = models.DateField()
    new_date = models.DateField(null=True, blank=True)
    reason = models.CharField("Indoklás", max_length=300, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="+", null=True, blank=True,
        on_delete=models.PROTECT)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    # Plan version created by this change when approved.
    result_version = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at", "-pk"]
        constraints = [
            models.CheckConstraint(
                condition=(models.Q(kind="move", new_date__isnull=False) | models.Q(kind="skip", new_date__isnull=True)),
                name="plan_change_new_date_matches_kind"),
        ]

    def __str__(self):
        return f"#{self.pk} {self.kind} session={self.session_id} ({self.status})"


class PlannedSet(models.Model):
    session = models.ForeignKey(TrainingSession, related_name="sets", on_delete=models.PROTECT)
    exercise = models.CharField("Gyakorlat és változat", max_length=120)
    reps = models.PositiveSmallIntegerField("Célismétlés", validators=[MinValueValidator(1), MaxValueValidator(100)])
    weight_kg = models.DecimalField("Előírt súly (kg)", max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ["pk"]
        constraints = [
            models.CheckConstraint(condition=models.Q(reps__gte=1, reps__lte=100), name="planned_reps_range"),
            models.CheckConstraint(condition=models.Q(weight_kg__gte=0), name="planned_weight_nonnegative"),
        ]

    def __str__(self):
        return f"{self.exercise} {self.weight_kg} kg x {self.reps}"


class SetLog(models.Model):
    """Actual performance is a separate record; one submission per prescribed set."""
    planned_set = models.OneToOneField(PlannedSet, related_name="performance", on_delete=models.PROTECT)
    submission_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    reps = models.PositiveSmallIntegerField("Elvégzett ismétlés", validators=[MaxValueValidator(100)])
    weight_kg = models.DecimalField("Tényleges súly (kg)", max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    rpe = models.DecimalField("Sorozat-RPE (opcionális)", max_digits=3, decimal_places=1, null=True, blank=True,
        validators=[MinValueValidator(Decimal("1")), MaxValueValidator(Decimal("10"))])
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(reps__gte=0, reps__lte=100), name="actual_reps_range"),
            models.CheckConstraint(condition=models.Q(weight_kg__gte=0), name="actual_weight_nonnegative"),
            models.CheckConstraint(condition=models.Q(rpe__isnull=True) | models.Q(rpe__gte=1, rpe__lte=10), name="actual_rpe_range"),
        ]

    def __str__(self):
        return f"{self.weight_kg} kg x {self.reps} (set {self.planned_set_id})"
