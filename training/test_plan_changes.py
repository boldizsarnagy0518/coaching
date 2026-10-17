import uuid
from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from memory import mcp_tools

from . import plan_changes
from .models import Athlete, ChangeStatus, PlanChange, PlannedSet, SessionStatus, SetLog, TrainingPlan, TrainingSession

TODAY = date.today()


class PlanChangeRuleTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")
        cls.plan = TrainingPlan.objects.create(athlete=cls.athlete, title="Blokk")
        cls.monday = TrainingSession.objects.create(plan=cls.plan, title="Hétfő",
            scheduled_date=TODAY + timedelta(days=3))
        cls.friday = TrainingSession.objects.create(plan=cls.plan, title="Péntek",
            scheduled_date=TODAY + timedelta(days=7))
        cls.item = PlannedSet.objects.create(session=cls.monday, exercise="Guggolás", reps=5, weight_kg=100)

    def test_move_is_proposed_then_applied_with_new_version(self):
        new_date = TODAY + timedelta(days=4)
        change = plan_changes.propose(self.coach, self.monday, "move", new_date, "Hétfőn nem ér rá")
        self.monday.refresh_from_db()
        self.assertEqual(self.monday.scheduled_date, TODAY + timedelta(days=3))  # nothing applied yet
        plan_changes.approve(self.coach, change)
        self.monday.refresh_from_db()
        self.plan.refresh_from_db()
        self.assertEqual((self.monday.scheduled_date, self.plan.version), (new_date, 2))
        self.assertEqual((change.status, change.result_version, change.old_date),
            (ChangeStatus.APPROVED, 2, TODAY + timedelta(days=3)))

    def test_skip_blocks_logging(self):
        plan_changes.approve(self.coach, plan_changes.propose(self.coach, self.monday, "skip"))
        self.monday.refresh_from_db()
        self.assertEqual(self.monday.status, SessionStatus.SKIPPED)
        self.client.force_login(self.coach)
        response = self.client.post(reverse("log-set", args=[self.item.pk]),
            {"submission_id": str(uuid.uuid4()), "reps": 5, "weight_kg": "100"})
        self.assertEqual(response.status_code, 409)
        self.assertFalse(SetLog.objects.exists())

    def test_logged_session_cannot_change(self):
        SetLog.objects.create(planned_set=self.item, reps=5, weight_kg=100)
        for kind, new_date in [("move", TODAY + timedelta(days=5)), ("skip", None)]:
            with self.subTest(kind=kind), self.assertRaises(plan_changes.PlanChangeError):
                plan_changes.propose(self.coach, self.monday, kind, new_date)

    def test_stale_proposal_is_not_applied(self):
        first = plan_changes.propose(self.coach, self.monday, "move", TODAY + timedelta(days=4))
        second = plan_changes.propose(self.coach, self.friday, "skip")
        plan_changes.approve(self.coach, first)
        with self.assertRaises(plan_changes.PlanChangeError):
            plan_changes.approve(self.coach, second)
        second.refresh_from_db()
        self.friday.refresh_from_db()
        self.assertEqual((second.status, self.friday.status), (ChangeStatus.STALE, SessionStatus.PLANNED))

    def test_proposal_goes_stale_if_session_gets_logged(self):
        change = plan_changes.propose(self.coach, self.monday, "skip")
        SetLog.objects.create(planned_set=self.item, reps=5, weight_kg=100)
        with self.assertRaises(plan_changes.PlanChangeError):
            plan_changes.approve(self.coach, change)
        change.refresh_from_db()
        self.assertEqual(change.status, ChangeStatus.STALE)

    def test_input_rules(self):
        for kind, new_date in [("move", None), ("move", TODAY + timedelta(days=3)), ("rename", None)]:
            with self.subTest(kind=kind, new_date=new_date), self.assertRaises(plan_changes.PlanChangeError):
                plan_changes.propose(self.coach, self.monday, kind, new_date)
        with self.assertRaises(plan_changes.PlanChangeError):
            plan_changes.propose(self.coach, self.monday, "skip", source="ai")  # AI needs a reason
        plan_changes.propose(self.coach, self.monday, "skip")
        with self.assertRaises(plan_changes.PlanChangeError):
            plan_changes.propose(self.coach, self.monday, "move", TODAY + timedelta(days=5))  # one pending per session
        with self.assertRaises(PermissionError):
            plan_changes.propose(self.other, self.friday, "skip")

    def test_preview_flags_same_day_conflict(self):
        change = plan_changes.propose(self.coach, self.monday, "move", self.friday.scheduled_date)
        rows = {row.session.pk: row for row in plan_changes.preview(change)}
        self.assertTrue(rows[self.monday.pk].same_day_conflict)
        self.assertEqual(rows[self.monday.pk].after, self.friday.scheduled_date)
        self.assertFalse(rows[self.friday.pk].changed)


class PlanChangeViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")
        cls.plan = TrainingPlan.objects.create(athlete=athlete, title="Blokk")
        cls.session = TrainingSession.objects.create(plan=cls.plan, title="Hétfő",
            scheduled_date=TODAY + timedelta(days=3))

    def setUp(self):
        self.client.force_login(self.coach)

    def test_full_flow_through_views(self):
        new_date = TODAY + timedelta(days=5)
        response = self.client.post(reverse("session-change", args=[self.session.pk, "move"]),
            {"new_date": new_date.isoformat(), "reason": "Időpontváltozás"}, follow=True)
        self.assertContains(response, "Előtte / utána")
        change = PlanChange.objects.get()
        self.assertContains(self.client.get(reverse("plan", args=[self.plan.pk])), "Jóváhagyásra váró módosítások (1)")
        self.client.post(reverse("plan-change-review", args=[change.pk, "approve"]))
        self.session.refresh_from_db()
        self.assertEqual(self.session.scheduled_date, new_date)
        self.assertContains(self.client.get(reverse("plan", args=[self.plan.pk])), "2. verzió")

    def test_change_form_links_back_to_session(self):
        response = self.client.get(reverse("session-change", args=[self.session.pk, "move"]))
        self.assertContains(response, f'href="{reverse("session", args=[self.session.pk])}"')
        self.assertContains(response, "Előtte / utána megtekintése")

    def test_move_requires_date_and_access_is_scoped(self):
        response = self.client.post(reverse("session-change", args=[self.session.pk, "move"]), {"reason": "x"})
        self.assertTrue(response.context["form"].errors)
        change = plan_changes.propose(self.coach, self.session, "skip")
        self.client.force_login(self.other)
        for url in [reverse("session-change", args=[self.session.pk, "skip"]), reverse("plan-change", args=[change.pk])]:
            self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(self.client.post(reverse("plan-change-review", args=[change.pk, "approve"])).status_code, 404)
        change.refresh_from_db()
        self.assertEqual(change.status, ChangeStatus.PROPOSED)

    def test_ai_proposal_tool_only_proposes(self):
        result = mcp_tools.propose_session_change(self.coach, self.plan.athlete_id, self.session.pk, "skip",
            "A sportoló jelezte, hogy beteg")
        self.assertTrue(result["saved"])
        self.session.refresh_from_db()
        self.assertEqual(self.session.status, SessionStatus.PLANNED)
        context = mcp_tools.get_athlete_context(self.coach, self.plan.athlete_id)
        self.assertEqual(context["upcoming_sessions"][0]["session_id"], self.session.pk)
        with self.assertRaises(ValueError):
            mcp_tools.propose_session_change(self.other, self.plan.athlete_id, self.session.pk, "skip", "x" * 20)
