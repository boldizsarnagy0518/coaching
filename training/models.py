import uuid
from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
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

    class Meta:
        ordering = ["-created_at", "-pk"]


class TrainingSession(models.Model):
    plan = models.ForeignKey(TrainingPlan, related_name="sessions", on_delete=models.PROTECT)
    title = models.CharField("Edzés neve", max_length=120)
    scheduled_date = models.DateField("Tervezett dátum")

    class Meta:
        ordering = ["scheduled_date", "pk"]


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
