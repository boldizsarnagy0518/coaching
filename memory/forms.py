from django import forms

from .models import AthleteMemory


class MemoryForm(forms.ModelForm):
    class Meta:
        model = AthleteMemory
        fields = ["category", "content", "exercise", "reason", "observed_on"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "maxlength": 300}),
            "observed_on": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }
