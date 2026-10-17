"""Concurrency check: several processes write to one SQLite file at the same time.

Simulates the web server (HTTP requests through the full Django stack) and the MCP server
(tool calls through call_tool_safely) running side by side, then checks the data invariants.

Usage (uses a throwaway database, never the real one):
    uv run python -m ops.concurrency_check --workers 8 --ops 60
"""
import argparse
import os
import random
import sys
import tempfile
import time
import uuid
from collections import Counter
from datetime import date, timedelta
from multiprocessing import Pool
from pathlib import Path


def _setup(db_path):
    os.environ["COACHING_DB_PATH"] = str(db_path)
    os.environ["COACHING_LOG_FILE"] = "false"
    os.environ.setdefault("DJANGO_LOG_LEVEL", "ERROR")
    os.environ["DJANGO_SETTINGS_MODULE"] = "coaching.settings"
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import logging

    import django

    django.setup()
    # Expected 409 conflicts would otherwise flood the output.
    logging.getLogger("django.request").setLevel(logging.ERROR)


def prepare(db_path, sessions):
    _setup(db_path)
    from django.contrib.auth import get_user_model
    from django.core.management import call_command

    from training.models import Athlete, PlannedSet, TrainingPlan, TrainingSession

    call_command("migrate", verbosity=0)
    coach = get_user_model().objects.create_user(username="load-coach")
    athlete = Athlete.objects.create(coach=coach, name="Terheléses teszt")
    plan = TrainingPlan.objects.create(athlete=athlete, title="Terheléses blokk")
    for index in range(sessions):
        session = TrainingSession.objects.create(plan=plan, title=f"Edzés {index}",
            scheduled_date=date.today() + timedelta(days=index + 1))
        PlannedSet.objects.bulk_create([PlannedSet(session=session, exercise="Guggolás", reps=5, weight_kg=100)
            for _ in range(3)])
    return coach.pk, athlete.pk, plan.pk


def worker(args):
    db_path, role, ops, seed, coach_id, athlete_id = args
    _setup(db_path)
    from django.contrib.auth import get_user_model
    from django.test import Client

    from memory import mcp_tools
    from training import plan_changes
    from training.models import PlanChange, PlannedSet, TrainingSession

    rng = random.Random(seed)
    coach = get_user_model().objects.get(pk=coach_id)
    client = Client(HTTP_HOST="localhost")
    client.force_login(coach)
    outcomes = Counter()
    set_ids = list(PlannedSet.objects.values_list("pk", flat=True))
    session_ids = list(TrainingSession.objects.values_list("pk", flat=True))
    for _ in range(ops):
        try:
            if role == "web":
                action = rng.choice(["log", "log", "relog", "approve", "view"])
                if action in ("log", "relog"):
                    item = rng.choice(set_ids)
                    payload = {"submission_id": str(uuid.uuid4()), "reps": rng.randint(3, 5), "weight_kg": "100"}
                    status = client.post(f"/sets/{item}/log/", payload).status_code
                    outcomes[f"web.log.{status}"] += 1
                elif action == "approve":
                    pending = list(PlanChange.objects.filter(status="proposed").values_list("pk", flat=True)[:5])
                    if pending:
                        status = client.post(f"/changes/{rng.choice(pending)}/approve/").status_code
                        outcomes[f"web.approve.{status}"] += 1
                else:
                    status = client.get(f"/sessions/{rng.choice(session_ids)}/").status_code
                    outcomes[f"web.view.{status}"] += 1
            else:
                action = rng.choice(["memory", "change", "context"])
                if action == "memory":
                    result = mcp_tools.call_tool_safely("propose_memory", mcp_tools.propose_memory, coach, athlete_id,
                        "response", f"Megfigyelés {uuid.uuid4().hex}", "Terheléses teszt indoklása")
                    outcomes["mcp.memory." + ("saved" if result["saved"] else "refused")] += 1
                elif action == "change":
                    session = rng.choice(session_ids)
                    result = mcp_tools.call_tool_safely("propose_session_change", mcp_tools.propose_session_change,
                        coach, athlete_id, session, "skip", "Terheléses teszt indoklása")
                    outcomes["mcp.change." + ("saved" if result["saved"] else "refused")] += 1
                else:
                    mcp_tools.call_tool_safely("get_athlete_context", mcp_tools.get_athlete_context, coach, athlete_id)
                    outcomes["mcp.context.ok"] += 1
        except plan_changes.PlanChangeError:
            outcomes[f"{role}.rule_refusal"] += 1
        except Exception as exc:  # noqa: BLE001 - every unexpected failure is counted and reported
            outcomes[f"{role}.ERROR.{type(exc).__name__}: {str(exc)[:80]}"] += 1
    return outcomes


def check_invariants(db_path, plan_id):
    _setup(db_path)
    from django.db.models import Count

    from training.models import PlanChange, PlannedSet, SetLog, TrainingPlan

    problems = []
    plan = TrainingPlan.objects.get(pk=plan_id)
    approved = PlanChange.objects.filter(plan=plan, status="approved").order_by("result_version")
    versions = list(approved.values_list("result_version", flat=True))
    if versions != list(range(2, 2 + len(versions))):
        problems.append(f"result versions not contiguous: {versions[:10]}")
    if plan.version != 1 + len(versions):
        problems.append(f"plan version {plan.version} != 1 + {len(versions)} approved changes")
    if PlannedSet.objects.annotate(n=Count("performance")).filter(n__gt=1).exists():
        problems.append("a prescribed set has more than one log")
    for change in approved.filter(kind="skip"):
        logged_before = SetLog.objects.filter(planned_set__session=change.session,
            recorded_at__lt=change.reviewed_at).exists()
        if logged_before:
            problems.append(f"change {change.pk} skipped a session that was already logged")
    return problems, {"approved_changes": len(versions), "logs": SetLog.objects.count(),
        "memories": plan.athlete.memories.count()}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--ops", type=int, default=60)
    parser.add_argument("--sessions", type=int, default=30)
    options = parser.parse_args()
    with tempfile.TemporaryDirectory() as folder:
        db_path = Path(folder) / "concurrency.sqlite3"
        coach_id, athlete_id, plan_id = prepare(db_path, options.sessions)
        jobs = [(db_path, "web" if index % 2 == 0 else "mcp", options.ops, index, coach_id, athlete_id)
            for index in range(options.workers)]
        started = time.perf_counter()
        with Pool(options.workers) as pool:
            results = pool.map(worker, jobs)
        elapsed = time.perf_counter() - started
        total = sum(results, Counter())
        problems, summary = check_invariants(db_path, plan_id)
        from django.db import connections
        connections.close_all()  # release the file before the temporary folder is removed
    print(f"{options.workers} processes x {options.ops} operations in {elapsed:.1f} s")
    for key, count in sorted(total.items()):
        print(f"  {key}: {count}")
    print(f"  summary: {summary}")
    errors = {key: count for key, count in total.items() if ".ERROR." in key or ".500" in key}
    if errors or problems:
        print("FAILED:", errors, problems)
        sys.exit(1)
    print("OK: no unexpected errors, invariants hold")


if __name__ == "__main__":
    main()
