import csv
import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.db.models import Count, Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from coaching.observability import log_event

from . import plan_changes
from .forms import AthleteForm, PlanChangeForm, PlanForm, PlannedSetForm, SessionForm, SetLogForm, TransferPreviewForm
from .models import (
    Athlete,
    ChangeKind,
    ChangeStatus,
    PlanChange,
    PlannedSet,
    SessionStatus,
    SetLog,
    TrainingPlan,
    TrainingSession,
)
from .transfers import MAX_BYTES, download_sheet, read_csv, safe_cell


@login_required
def export_csv(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk, coach=request.user)
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="athlete-{athlete.pk}-journal.csv"'
    response["Cache-Control"] = "no-store"
    response.write("\ufeff")
    writer = csv.writer(response)
    writer.writerow(["plan", "session", "scheduled_date", "exercise", "planned_reps", "planned_weight_kg",
        "actual_reps", "actual_weight_kg", "rpe", "recorded_at"])
    items = PlannedSet.objects.filter(session__plan__athlete=athlete).select_related("session__plan", "performance").order_by("session__scheduled_date", "session_id", "pk")
    for item in items.iterator():
        log = getattr(item, "performance", None)
        writer.writerow([safe_cell(value) for value in [item.session.plan.title, item.session.title,
            item.session.scheduled_date.isoformat(), item.exercise, item.reps, item.weight_kg,
            log.reps if log else None, log.weight_kg if log else None, log.rpe if log else None,
            log.recorded_at.isoformat() if log else None]])
    return response


@login_required
def transfer_preview(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk, coach=request.user)
    is_post = request.method == "POST"
    # Passing request.FILES on GET would bind the form and show errors before any submission.
    form = TransferPreviewForm(request.POST if is_post else None, request.FILES if is_post else None)
    preview = None
    if is_post and form.is_valid():
        try:
            file = form.cleaned_data.get("csv_file")
            preview = read_csv(file.read(MAX_BYTES + 1)) if file else download_sheet(form.cleaned_data["sheet_url"])
        except ValueError as exc:
            form.add_error(None, str(exc))
    response = render(request, "training/transfer.html", {"athlete": athlete, "form": form, "preview": preview})
    response["Cache-Control"] = "no-store"
    return response


def conflict(request, message, session_id=None):
    back_url = reverse("session", args=[session_id]) if session_id else None
    return render(request, "training/conflict.html", {"message": message, "back_url": back_url}, status=409)


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
    athletes = Athlete.objects.annotate(
        active_memory_count=Count("memories", filter=Q(memories__status="active")),
        proposed_memory_count=Count("memories", filter=Q(memories__status="proposed")),
    )
    athlete = get_object_or_404(athletes, pk=pk, coach=request.user)
    return render(request, "training/athlete.html", {"athlete": athlete})


@login_required
def plan_create(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk, coach=request.user)
    return save_form(request, PlanForm, f"Új terv · {athlete.name}", {"athlete": athlete}, "plan")


@login_required
def plan_detail(request, pk):
    plan = get_object_or_404(TrainingPlan.objects.select_related("athlete"), pk=pk, athlete__coach=request.user)
    changes = list(plan.changes.select_related("session"))
    return render(request, "training/plan.html", {"plan": plan,
        "pending": [c for c in changes if c.status == ChangeStatus.PROPOSED],
        "history": [c for c in changes if c.status != ChangeStatus.PROPOSED]})


@login_required
def session_create(request, pk):
    plan = get_object_or_404(TrainingPlan, pk=pk, athlete__coach=request.user)
    return save_form(request, SessionForm, "Új edzés", {"plan": plan}, "session")


@login_required
def session_detail(request, pk):
    session = get_object_or_404(TrainingSession.objects.select_related("plan__athlete"), pk=pk, plan__athlete__coach=request.user)
    sets = list(session.sets.select_related("performance"))
    completed = sum(hasattr(item, "performance") for item in sets)
    can_change = session.status == SessionStatus.PLANNED and not completed
    return render(request, "training/session.html", {"session": session, "sets": sets, "completed": completed,
        "can_change": can_change, "pending_change": session.changes.filter(status=ChangeStatus.PROPOSED).first()})


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
    if item.session.status == SessionStatus.SKIPPED:
        log_event("set_log.refused", set=item.pk, reason="session_skipped")
        return conflict(request, "Ez az edzés ki van hagyva, ezért nem naplózható.", item.session_id)
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
                log_event("set_log.conflict", set=item.pk)
                return conflict(request, "Ez a sorozat vagy beküldés már mentve van. A korábbi adatot nem írtuk felül.",
                    item.session_id)
            log_event("set_log.duplicate_resubmission", set=item.pk)
        else:
            log_event("set_log.saved", set=item.pk)
        messages.success(request, "A sorozat mentve. Az előírt terv változatlan.")
        return redirect("session", pk=item.session_id)
    return render(request, "training/form.html", {"form": form, "title": f"Teljesítés · {item.exercise}",
        "back_url": reverse("session", args=[item.session_id]), "back_label": "Vissza az edzéshez"})


@login_required
def session_change(request, pk, kind):
    if kind not in ChangeKind.values:
        raise Http404
    session = get_object_or_404(TrainingSession.objects.select_related("plan__athlete"), pk=pk,
        plan__athlete__coach=request.user)
    form = PlanChangeForm(request.POST if request.method == "POST" else None, kind=kind)
    if request.method == "POST" and form.is_valid():
        try:
            change = plan_changes.propose(request.user, session, kind, form.cleaned_data.get("new_date"),
                form.cleaned_data["reason"])
        except plan_changes.PlanChangeError as exc:
            form.add_error(None, str(exc))
        else:
            return redirect("plan-change", pk=change.pk)
    title = f"{ChangeKind(kind).label} · {session.title} ({session.scheduled_date:%Y. %m. %d.})"
    return render(request, "training/form.html", {"form": form, "title": title, "submit_label": "Előtte / utána megtekintése",
        "back_url": reverse("session", args=[session.pk]), "back_label": session.title})


@login_required
def change_detail(request, pk):
    change = get_object_or_404(PlanChange.objects.select_related("plan__athlete", "session"), pk=pk,
        plan__athlete__coach=request.user)
    return render(request, "training/plan_change.html", {"change": change, "rows": plan_changes.preview(change),
        "outdated": change.status == ChangeStatus.PROPOSED and change.plan.version != change.base_version})


@login_required
@require_POST
def change_review(request, pk, action):
    handlers = {"approve": (plan_changes.approve, "Módosítás jóváhagyva; új tervverzió jött létre."),
        "reject": (plan_changes.reject, "Módosítás elutasítva; a terv változatlan.")}
    if action not in handlers:
        raise Http404
    change = get_object_or_404(PlanChange.objects.select_related("plan__athlete"), pk=pk,
        plan__athlete__coach=request.user)
    handler, success = handlers[action]
    try:
        handler(request.user, change)
    except plan_changes.PlanChangeError as exc:
        messages.error(request, str(exc))
    else:
        messages.success(request, success)
    return redirect("plan", pk=change.plan_id)
