from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from training.models import Athlete

from . import services
from .forms import MemoryForm
from .models import AthleteMemory, MemoryCategory, MemorySource, MemoryStatus

REVIEW_ACTIONS = {
    "approve": (services.approve, "Javaslat jóváhagyva, bekerült az aktív emlékek közé."),
    "reject": (services.reject, "Javaslat elutasítva."),
    "resolve": (services.resolve, "Bejegyzés lezárva; az előzmények között megmarad."),
    "reactivate": (services.reactivate, "Bejegyzés újra aktív."),
}


@login_required
def athlete_memory(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk, coach=request.user)
    form = MemoryForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        try:
            services.create_memory(request.user, athlete, _input(form), MemorySource.COACH)
        except services.MemoryRuleError as exc:
            form.add_error(None, str(exc))
        else:
            messages.success(request, "Bejegyzés mentve az aktív emlékek közé.")
            return redirect("athlete-memory", pk=athlete.pk)
    memories = list(athlete.memories.exclude(status=MemoryStatus.REJECTED))
    active = [m for m in memories if m.status == MemoryStatus.ACTIVE]
    groups = [(label, [m for m in active if m.category == value]) for value, label in MemoryCategory.choices]
    return render(request, "memory/athlete_memory.html", {
        "athlete": athlete, "form": form,
        "groups": [(label, items) for label, items in groups if items],
        "proposals": [m for m in memories if m.status == MemoryStatus.PROPOSED],
        "resolved": [m for m in memories if m.status == MemoryStatus.RESOLVED],
    })


def _input(form):
    data = form.cleaned_data
    return services.MemoryInput(category=data["category"], content=data["content"] or "",
        exercise=data["exercise"] or "", reason=data["reason"] or "", observed_on=data["observed_on"])


@login_required
def edit_memory(request, pk):
    memory = get_object_or_404(AthleteMemory.objects.select_related("athlete"), pk=pk, athlete__coach=request.user,
        status__in=services.OPEN_STATUSES)
    form = MemoryForm(request.POST if request.method == "POST" else None, instance=memory)
    if request.method == "POST" and form.is_valid():
        memory.refresh_from_db()  # form validation mutates the instance; the service applies the change
        try:
            services.update_memory(request.user, memory, _input(form))
        except services.MemoryRuleError as exc:
            form.add_error(None, str(exc))
        else:
            messages.success(request, "Bejegyzés módosítva.")
            return redirect("athlete-memory", pk=memory.athlete_id)
    return render(request, "training/form.html", {"form": form, "title": f"Bejegyzés szerkesztése · {memory.athlete.name}",
        "back_url": reverse("athlete-memory", args=[memory.athlete_id]), "back_label": "Emlékek"})


@login_required
@require_POST
def review_memory(request, pk, action):
    if action not in REVIEW_ACTIONS:
        raise Http404
    memory = get_object_or_404(AthleteMemory.objects.select_related("athlete"), pk=pk,
        athlete__coach=request.user)
    handler, success = REVIEW_ACTIONS[action]
    try:
        handler(request.user, memory)
    except services.MemoryRuleError as exc:
        messages.error(request, str(exc))
    else:
        messages.success(request, success)
    return redirect("athlete-memory", pk=memory.athlete_id)
