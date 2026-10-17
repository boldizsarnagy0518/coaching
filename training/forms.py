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


class TransferPreviewForm(forms.Form):
    csv_file = forms.FileField(label="Letöltött CSV-fájl", required=False)
    sheet_url = forms.URLField(label="Publikált Google Sheets CSV-link", required=False)

    def clean(self):
        data = super().clean()
        if bool(data.get("csv_file")) == bool(data.get("sheet_url")):
            raise forms.ValidationError("Vagy CSV-fájlt válassz, vagy Google Sheets-linket adj meg.")
        return data
