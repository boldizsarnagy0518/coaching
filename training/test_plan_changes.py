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


class PartialAndBatchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")
        cls.plan = TrainingPlan.objects.create(athlete=cls.athlete, title="Blokk")
        cls.days = [TrainingSession.objects.create(plan=cls.plan, title=f"Nap {index}",
            scheduled_date=TODAY + timedelta(days=index * 2 + 1)) for index in range(3)]
        cls.sets = [PlannedSet.objects.create(session=cls.days[0], exercise=name, reps=5, weight_kg=100)
            for name in ["Guggolás", "Fekvenyomás", "Evezés"]]

    def setUp(self):
        self.client.force_login(self.coach)

    def test_move_rest_keeps_logged_sets_and_creates_continuation(self):
        SetLog.objects.create(planned_set=self.sets[0], reps=5, weight_kg=100)
        new_date = TODAY + timedelta(days=2)
        change = plan_changes.propose(self.coach, self.days[0], "move_rest", new_date, "Elfogyott az idő")
        rows = plan_changes.preview(change)
        self.assertTrue(any(row.is_new and row.after == new_date for row in rows))
        plan_changes.approve(self.coach, change)
        change.refresh_from_db()
        continuation = change.created_session
        self.assertEqual((change.moved_sets, continuation.scheduled_date), (2, new_date))
        self.assertEqual(list(self.days[0].sets.values_list("exercise", flat=True)), ["Guggolás"])
        self.assertEqual(sorted(continuation.sets.values_list("exercise", flat=True)), ["Evezés", "Fekvenyomás"])
        self.assertEqual(SetLog.objects.get().planned_set.session, self.days[0])
        self.plan.refresh_from_db()
        self.assertEqual(self.plan.version, 2)

    def test_move_rest_rules(self):
        with self.assertRaisesMessage(plan_changes.PlanChangeError, "egész edzést"):
            plan_changes.propose(self.coach, self.days[0], "move_rest", TODAY + timedelta(days=2))
        for item in self.sets:
            SetLog.objects.create(planned_set=item, reps=5, weight_kg=100)
        with self.assertRaisesMessage(plan_changes.PlanChangeError, "Nincs hátralévő"):
            plan_changes.propose(self.coach, self.days[0], "move_rest", TODAY + timedelta(days=2))

    def test_move_rest_goes_stale_when_everything_gets_logged(self):
        SetLog.objects.create(planned_set=self.sets[0], reps=5, weight_kg=100)
        change = plan_changes.propose(self.coach, self.days[0], "move_rest", TODAY + timedelta(days=2))
        for item in self.sets[1:]:
            SetLog.objects.create(planned_set=item, reps=5, weight_kg=100)
        with self.assertRaises(plan_changes.PlanChangeError):
            plan_changes.approve(self.coach, change)
        change.refresh_from_db()
        self.assertEqual((change.status, change.created_session), (ChangeStatus.STALE, None))

    def test_batch_is_one_version_and_all_or_nothing(self):
        moves = [(self.days[1], TODAY + timedelta(days=4)), (self.days[2], TODAY + timedelta(days=6)),
            (self.days[0], self.days[0].scheduled_date)]  # an unchanged date is ignored
        changes = plan_changes.propose_batch(self.coach, self.plan, moves, "Négy edzésnap")
        self.assertEqual(len(changes), 2)
        self.assertEqual(len({change.batch for change in changes}), 1)
        plan_changes.approve(self.coach, changes[1])
        self.plan.refresh_from_db()
        self.assertEqual(self.plan.version, 2)
        self.assertEqual(set(PlanChange.objects.values_list("status", "result_version")), {("approved", 2)})
        self.days[2].refresh_from_db()
        self.assertEqual(self.days[2].scheduled_date, TODAY + timedelta(days=6))

    def test_batch_goes_stale_as_a_whole(self):
        changes = plan_changes.propose_batch(self.coach, self.plan,
            [(self.days[1], TODAY + timedelta(days=4)), (self.days[2], TODAY + timedelta(days=6))])
        late_set = PlannedSet.objects.create(session=self.days[2], exercise="Felhúzás", reps=3, weight_kg=120)
        SetLog.objects.create(planned_set=late_set, reps=3, weight_kg=120)
        with self.assertRaises(plan_changes.PlanChangeError):
            plan_changes.approve(self.coach, changes[0])
        self.assertEqual(set(PlanChange.objects.values_list("status", flat=True)), {"stale"})
        self.days[1].refresh_from_db()
        self.assertEqual(self.days[1].scheduled_date, TODAY + timedelta(days=3))  # nothing applied

    def test_batch_rules_and_reject(self):
        with self.assertRaisesMessage(plan_changes.PlanChangeError, "Egyetlen dátum sem változott"):
            plan_changes.propose_batch(self.coach, self.plan, [(self.days[1], self.days[1].scheduled_date)])
        with self.assertRaises(PermissionError):
            plan_changes.propose_batch(self.other, self.plan, [(self.days[1], TODAY + timedelta(days=9))])
        changes = plan_changes.propose_batch(self.coach, self.plan, [(self.days[1], TODAY + timedelta(days=9)),
            (self.days[2], TODAY + timedelta(days=10))])
        with self.assertRaisesMessage(plan_changes.PlanChangeError, "már van jóváhagyásra váró"):
            plan_changes.propose(self.coach, self.days[1], "skip")
        plan_changes.reject(self.coach, changes[0])
        self.assertEqual(set(PlanChange.objects.values_list("status", flat=True)), {"rejected"})

    def test_reschedule_view_and_plan_listing(self):
        url = reverse("plan-reschedule", args=[self.plan.pk])
        self.assertContains(self.client.get(url), "Nap 1")
        data = {f"date_{day.pk}": day.scheduled_date.isoformat() for day in self.days}
        data[f"date_{self.days[1].pk}"] = (TODAY + timedelta(days=8)).isoformat()
        data[f"date_{self.days[2].pk}"] = (TODAY + timedelta(days=9)).isoformat()
        response = self.client.post(url, data, follow=True)
        self.assertContains(response, "Átütemezés · 2 edzés")
        plan_page = self.client.get(reverse("plan", args=[self.plan.pk]))
        self.assertContains(plan_page, "Jóváhagyásra váró módosítások (1)")
        self.client.force_login(self.other)
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_session_page_offers_move_rest_only_when_partial(self):
        url = reverse("session", args=[self.days[0].pk])
        self.assertNotContains(self.client.get(url), "Hátralévő sorozatok áthelyezése")
        SetLog.objects.create(planned_set=self.sets[0], reps=5, weight_kg=100)
        self.assertContains(self.client.get(url), "Hátralévő sorozatok áthelyezése")

    def test_ai_reschedule_tool(self):
        moves = [{"session_id": self.days[1].pk, "new_date": (TODAY + timedelta(days=4)).isoformat()},
            {"session_id": self.days[2].pk, "new_date": (TODAY + timedelta(days=6)).isoformat()}]
        result = mcp_tools.propose_reschedule(self.coach, self.athlete.pk, moves, "A sportoló négy napot tud edzeni")
        self.assertEqual((result["saved"], result["moves"]), (True, 2))
        self.assertEqual(set(PlanChange.objects.values_list("source", flat=True)), {"ai"})
        refused = mcp_tools.propose_reschedule(self.coach, self.athlete.pk, moves[:1], "rövid")
        self.assertFalse(refused["saved"])
        for bad in [[], [{"session_id": 999999, "new_date": "2026-11-01"}], [{"new_date": "2026-11-01"}]]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                mcp_tools.propose_reschedule(self.coach, self.athlete.pk, bad, "Elég hosszú indoklás")

