from django import forms

from .models import Athlete, PlannedSet, SetLog, TrainingPlan, TrainingSession


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


class PlanChangeForm(forms.Form):
    new_date = forms.DateField(label="Új dátum", required=False,
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"))
    reason = forms.CharField(label="Indoklás (opcionális)", max_length=300, required=False,
        widget=forms.Textarea(attrs={"rows": 2, "maxlength": 300}))

    def __init__(self, *args, kind, **kwargs):
        super().__init__(*args, **kwargs)
        if kind in ("move", "move_rest"):
            self.fields["new_date"].required = True
        else:
            del self.fields["new_date"]


class RescheduleForm(forms.Form):
    """One date field per movable session, prefilled with its current date."""

    reason = forms.CharField(label="Indoklás (opcionális)", max_length=300, required=False,
        widget=forms.Textarea(attrs={"rows": 2, "maxlength": 300}))

    def __init__(self, *args, sessions, **kwargs):
        super().__init__(*args, **kwargs)
        self.sessions = sessions
        for session in sessions:
            label = f"{session.title} (most: {session.scheduled_date:%Y. %m. %d.})"
            self.fields[f"date_{session.pk}"] = forms.DateField(label=label, initial=session.scheduled_date,
                widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"))
        self.order_fields([f"date_{session.pk}" for session in sessions] + ["reason"])

    def moves(self):
        return [(session, self.cleaned_data[f"date_{session.pk}"]) for session in self.sessions]
