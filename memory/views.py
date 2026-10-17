from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
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
        data = services.MemoryInput(**{name: form.cleaned_data[name] or "" for name in
            ["category", "content", "exercise", "reason"]}, observed_on=form.cleaned_data["observed_on"])
        try:
            services.create_memory(request.user, athlete, data, MemorySource.COACH)
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
