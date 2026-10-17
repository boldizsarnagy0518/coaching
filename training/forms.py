from django import forms
from .models import Athlete, TrainingPlan, TrainingSession, PlannedSet, SetLog


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ["name"]


class PlanForm(forms.ModelForm):
    class Meta:
        model = TrainingPlan
        fields = ["title"]


class SessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ["title", "scheduled_date"]
        widgets = {"scheduled_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d")}


class PlannedSetForm(forms.ModelForm):
    class Meta:
        model = PlannedSet
        fields = ["exercise", "reps", "weight_kg"]


class SetLogForm(forms.ModelForm):
    submission_id = forms.UUIDField(widget=forms.HiddenInput())

    class Meta:
        model = SetLog
        fields = ["reps", "weight_kg", "rpe"]
