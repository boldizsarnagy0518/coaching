import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AthleteForm, PlanForm, SessionForm, PlannedSetForm, SetLogForm
from .models import Athlete, TrainingPlan, TrainingSession, PlannedSet, SetLog


@login_required
def dashboard(request):
    athletes = Athlete.objects.filter(coach=request.user).annotate(plan_count=Count("plans"))
    return render(request, "training/dashboard.html", {"athletes": athletes})


def save_form(request, form_class, title, relation, destination):
    form = form_class(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        for name, value in relation.items():
            setattr(instance, name, value)
        instance.save()
        return redirect(destination, pk=instance.pk)
    return render(request, "training/form.html", {"form": form, "title": title})


@login_required
def athlete_create(request):
    return save_form(request, AthleteForm, "Új sportoló", {"coach": request.user}, "athlete")


@login_required
def athlete_detail(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk, coach=request.user)
    return render(request, "training/athlete.html", {"athlete": athlete})


@login_required
def plan_create(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk, coach=request.user)
    return save_form(request, PlanForm, f"Új terv · {athlete.name}", {"athlete": athlete}, "plan")


@login_required
def plan_detail(request, pk):
    plan = get_object_or_404(TrainingPlan.objects.select_related("athlete"), pk=pk, athlete__coach=request.user)
    return render(request, "training/plan.html", {"plan": plan})


@login_required
def session_create(request, pk):
    plan = get_object_or_404(TrainingPlan, pk=pk, athlete__coach=request.user)
    return save_form(request, SessionForm, "Új edzés", {"plan": plan}, "session")


@login_required
def session_detail(request, pk):
    session = get_object_or_404(TrainingSession.objects.select_related("plan__athlete"), pk=pk, plan__athlete__coach=request.user)
    sets = list(session.sets.select_related("performance"))
    completed = sum(hasattr(item, "performance") for item in sets)
    return render(request, "training/session.html", {"session": session, "sets": sets, "completed": completed})


@login_required
def set_create(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk, plan__athlete__coach=request.user)
    form = PlannedSetForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False)
        item.session = session
        item.save()
        return redirect("session", pk=session.pk)
    return render(request, "training/form.html", {"form": form, "title": "Előírt sorozat hozzáadása"})


@login_required
def log_set(request, pk):
    item = get_object_or_404(PlannedSet.objects.select_related("session"), pk=pk, session__plan__athlete__coach=request.user)
    form = SetLogForm(request.POST if request.method == "POST" else None,
        initial={"submission_id": uuid.uuid4(), "reps": item.reps, "weight_kg": item.weight_kg})
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        try:
            with transaction.atomic():
                SetLog.objects.create(planned_set=item, submission_id=data["submission_id"],
                    reps=data["reps"], weight_kg=data["weight_kg"], rpe=data["rpe"])
        except IntegrityError:
            existing = SetLog.objects.filter(planned_set=item).first()
            if not existing or any(getattr(existing, key) != data[key] for key in ["submission_id", "reps", "weight_kg", "rpe"]):
                return HttpResponse("Ez a sorozat vagy beküldés már mentve van. A korábbi adatot nem írtuk felül.", status=409)
        messages.success(request, "A sorozat mentve. Az előírt terv változatlan.")
        return redirect("session", pk=item.session_id)
    return render(request, "training/form.html", {"form": form, "title": f"Teljesítés · {item.exercise}"})
