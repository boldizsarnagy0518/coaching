import sqlite3
import tempfile
import uuid
from contextlib import closing
from datetime import date, datetime, timedelta
from io import StringIO
from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.management import CommandError, call_command
from django.test import TestCase, TransactionTestCase
from django.urls import reverse

from memory import mcp_tools, services
from memory.models import MemorySource
from training.models import Athlete, PlannedSet, SetLog, TrainingPlan, TrainingSession

from .backup import create_backup, integrity_check, prune


class ObservabilityTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")

    def test_health_check_is_public_and_minimal(self):
        response = self.client.get(reverse("healthz"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "database": "ok"})

    def test_request_id_header_and_request_log(self):
        with self.assertLogs("coaching.request", level="INFO") as logs:
            response = self.client.get(reverse("healthz"), headers={"X-Request-ID": "trace-12345678"})
        self.assertEqual(response["X-Request-ID"], "trace-12345678")
        self.assertIn("path=/healthz status=200", logs.output[0])
        unsafe = self.client.get(reverse("healthz"), headers={"X-Request-ID": "bad id\nwith newline"})
        self.assertRegex(unsafe["X-Request-ID"], r"^[0-9a-f]{32}$")

    def test_query_string_is_not_logged(self):
        with self.assertLogs("coaching.request", level="INFO") as logs:
            self.client.get(reverse("healthz") + "?name=Secret")
        self.assertNotIn("Secret", "".join(logs.output))

    def test_domain_events_contain_ids_not_content(self):
        with self.assertLogs("coaching.events", level="INFO") as logs:
            services.create_memory(self.coach, self.athlete, services.MemoryInput("pain_injury",
                "Bal térd fáj a guggolás alján"), MemorySource.COACH)
        self.assertIn("event=memory.created", logs.output[0])
        self.assertNotIn("térd", "".join(logs.output))


class McpRobustnessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")

    def test_unexpected_errors_are_isolated_and_logged(self):
        def broken(coach):
            raise KeyError("internal detail")

        with self.assertLogs("coaching", level="INFO") as logs, self.assertRaises(mcp_tools.ToolFailure) as caught:
            mcp_tools.call_tool_safely("broken", broken, self.coach)
        self.assertIn("reference mcp-", str(caught.exception))
        self.assertNotIn("internal detail", str(caught.exception))
        self.assertTrue(any("outcome=error" in line for line in logs.output))

    def test_invalid_input_and_refusals_are_reported(self):
        with self.assertRaisesMessage(ValueError, "YYYY-MM-DD"):
            mcp_tools.call_tool_safely("propose_memory", mcp_tools.propose_memory, self.coach, self.athlete.pk,
                "goal", "Márciusi verseny a cél", "Fontos a tervezéshez", observed_on="17/10/2026")
        with self.assertLogs("coaching.events", level="INFO") as logs:
            result = mcp_tools.call_tool_safely("propose_memory", mcp_tools.propose_memory, self.coach,
                self.athlete.pk, "mood", "Ma jókedvű volt az edzésen", "Hangulat")
        self.assertFalse(result["saved"])
        self.assertTrue(any("tool=propose_memory outcome=refused" in line for line in logs.output))


class ErrorPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")
        plan = TrainingPlan.objects.create(athlete=athlete, title="Blokk")
        session = TrainingSession.objects.create(plan=plan, title="A nap", scheduled_date=date.today())
        cls.item = PlannedSet.objects.create(session=session, exercise="Guggolás", reps=5, weight_kg=100)

    def setUp(self):
        self.client.force_login(self.coach)

    def test_not_found_page_is_friendly(self):
        response = self.client.get("/athletes/999999/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Nem található", status_code=404)

    def test_conflict_page_keeps_earlier_data(self):
        SetLog.objects.create(planned_set=self.item, reps=5, weight_kg=100)
        response = self.client.post(reverse("log-set", args=[self.item.pk]),
            {"submission_id": str(uuid.uuid4()), "reps": 3, "weight_kg": "90"})
        self.assertContains(response, "A korábbi adatot nem írtuk felül", status_code=409)
        self.assertContains(response, "Vissza az edzéshez", status_code=409)
        self.assertEqual(SetLog.objects.get().reps, 5)


class BackupTests(TransactionTestCase):
    # TransactionTestCase: the backup needs the database outside a wrapping test transaction.
    def setUp(self):
        get_user_model().objects.create_user(username="coach-a")

    def test_refuses_inside_transaction(self):
        from django.db import transaction

        from .backup import BackupError
        with tempfile.TemporaryDirectory() as folder, transaction.atomic(), self.assertRaises(BackupError):
            create_backup(folder)

    def test_backup_is_verified_and_contains_data(self):
        with tempfile.TemporaryDirectory() as folder:
            target, removed = create_backup(folder, keep=3)
            self.assertEqual(removed, [])
            self.assertEqual(integrity_check(target), (True, "ok"))
            with closing(sqlite3.connect(target)) as db:
                self.assertEqual(db.execute("SELECT username FROM auth_user").fetchall(), [("coach-a",)])

    def test_retention_keeps_newest(self):
        with tempfile.TemporaryDirectory() as folder:
            start = datetime(2026, 10, 1, 12, 0, 0)
            for day in range(4):
                create_backup(folder, keep=10, now=start + timedelta(days=day))
            removed = prune(folder, keep=2)
            self.assertEqual([p.name for p in removed], ["db-20261001-120000.sqlite3", "db-20261002-120000.sqlite3"])
            self.assertEqual(len(list(Path(folder).glob("db-*.sqlite3"))), 2)

    def test_command_and_verify(self):
        with tempfile.TemporaryDirectory() as folder:
            out = StringIO()
            call_command("backup_db", "--dir", folder, "--keep", "2", stdout=out)
            self.assertIn("verified", out.getvalue())
            broken = Path(folder) / "broken.sqlite3"
            broken.write_bytes(b"not a database" * 100)
            with self.assertRaises((CommandError, sqlite3.DatabaseError)):
                call_command("backup_db", "--verify", str(broken), stdout=StringIO())
            with self.assertRaises(CommandError):
                call_command("backup_db", "--dir", folder, "--keep", "0", stdout=StringIO())
