import uuid
from datetime import date
from decimal import Decimal
from io import StringIO

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import Client, TestCase
from django.urls import reverse

from .models import Athlete, TrainingPlan, TrainingSession, PlannedSet, SetLog


class JournalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus sportoló")
        cls.plan = TrainingPlan.objects.create(athlete=cls.athlete, title="Alapozó blokk")
        cls.session = TrainingSession.objects.create(plan=cls.plan, title="A nap", scheduled_date=date(2026, 10, 17))
        cls.item = PlannedSet.objects.create(session=cls.session, exercise="Szünetes fekvenyomás", reps=5, weight_kg=100)

    def setUp(self):
        self.client.force_login(self.coach)

    def payload(self, **changes):
        return {"submission_id": str(uuid.uuid4()), "reps": 4, "weight_kg": "97.50", "rpe": "8.5", **changes}

    def test_login_required_on_all_routes(self):
        self.client.logout()
        routes = [("dashboard", None), ("athlete-create", None), ("athlete", self.athlete.pk),
            ("plan-create", self.athlete.pk), ("plan", self.plan.pk), ("session-create", self.plan.pk),
            ("session", self.session.pk), ("set-create", self.session.pk), ("log-set", self.item.pk)]
        for name, pk in routes:
            with self.subTest(route=name):
                url = reverse(name, kwargs={"pk": pk} if pk else None)
                self.assertEqual(self.client.get(url).status_code, 302)
                self.assertEqual(self.client.post(url, {}).status_code, 302)

    def test_foreign_coach_cannot_read_or_write_any_nested_resource(self):
        self.client.force_login(self.other)
        for name, pk in [("athlete", self.athlete.pk), ("plan-create", self.athlete.pk),
            ("plan", self.plan.pk), ("session-create", self.plan.pk), ("session", self.session.pk),
            ("set-create", self.session.pk), ("log-set", self.item.pk)]:
            with self.subTest(route=name):
                url = reverse(name, kwargs={"pk": pk})
                self.assertEqual(self.client.get(url).status_code, 404)
                self.assertEqual(self.client.post(url, self.payload()).status_code, 404)
        self.assertEqual(SetLog.objects.count(), 0)
        self.assertNotContains(self.client.get(reverse("dashboard")), self.athlete.name)

    def test_complete_creation_and_journaling_flow(self):
        self.client.post(reverse("athlete-create"), {"name": "Új teszt", "coach": self.other.pk})
        athlete = Athlete.objects.get(name="Új teszt")
        self.assertEqual(athlete.coach, self.coach)
        self.client.post(reverse("plan-create", args=[athlete.pk]), {"title": "Második terv"})
        plan = athlete.plans.get()
        self.client.post(reverse("session-create", args=[plan.pk]), {"title": "Guggolás", "scheduled_date": "2026-10-18"})
        session = plan.sessions.get()
        self.client.post(reverse("set-create", args=[session.pk]), {"exercise": "Guggolás", "reps": 3, "weight_kg": "120"})
        item = session.sets.get()
        response = self.client.post(reverse("log-set", args=[item.pk]), self.payload(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mentve")
        self.assertEqual(SetLog.objects.get(planned_set=item).weight_kg, Decimal("97.50"))
        item.refresh_from_db()
        self.assertEqual(item.weight_kg, Decimal("120"))
        self.assertEqual(item.reps, 3)

    def test_identical_resubmission_is_idempotent(self):
        data = self.payload()
        url = reverse("log-set", args=[self.item.pk])
        self.assertEqual(self.client.post(url, data).status_code, 302)
        self.assertEqual(self.client.post(url, data).status_code, 302)
        self.assertEqual(SetLog.objects.count(), 1)

    def test_changed_retry_cannot_overwrite_performance(self):
        data = self.payload()
        url = reverse("log-set", args=[self.item.pk])
        self.client.post(url, data)
        response = self.client.post(url, {**data, "reps": 7})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(SetLog.objects.get().reps, 4)

    def test_new_submission_for_logged_set_is_rejected(self):
        url = reverse("log-set", args=[self.item.pk])
        self.client.post(url, self.payload())
        self.assertEqual(self.client.post(url, self.payload()).status_code, 409)
        self.assertEqual(SetLog.objects.count(), 1)

    def test_submission_id_cannot_be_reused_for_a_different_set(self):
        second = PlannedSet.objects.create(session=self.session, exercise="Evezés", reps=8, weight_kg=60)
        data = self.payload()
        self.client.post(reverse("log-set", args=[self.item.pk]), data)
        response = self.client.post(reverse("log-set", args=[second.pk]), data)
        self.assertEqual(response.status_code, 409)
        self.assertFalse(SetLog.objects.filter(planned_set=second).exists())

    def test_invalid_inputs_do_not_write_records(self):
        for invalid in [{"reps": -1}, {"reps": 101}, {"weight_kg": "-1"}, {"weight_kg": "NaN"},
            {"rpe": "10.1"}, {"rpe": "0"}, {"submission_id": "invalid"}]:
            with self.subTest(invalid=invalid):
                response = self.client.post(reverse("log-set", args=[self.item.pk]), self.payload(**invalid))
                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.context["form"].errors)
        self.assertEqual(SetLog.objects.count(), 0)

    def test_optional_rpe_and_zero_reps_are_preserved(self):
        self.client.post(reverse("log-set", args=[self.item.pk]), self.payload(reps=0, rpe=""))
        record = SetLog.objects.get()
        self.assertEqual(record.reps, 0)
        self.assertIsNone(record.rpe)

    def test_partial_completion_is_visible(self):
        PlannedSet.objects.create(session=self.session, exercise="Felhúzás", reps=3, weight_kg=140)
        self.client.post(reverse("log-set", args=[self.item.pk]), self.payload())
        response = self.client.get(reverse("session", args=[self.session.pk]))
        self.assertContains(response, "1 / 2")
        self.assertContains(response, "Részben teljesített")

    def test_get_form_does_not_write(self):
        response = self.client.get(reverse("log-set", args=[self.item.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(SetLog.objects.count(), 0)
        uuid.UUID(str(response.context["form"].initial["submission_id"]))

    def test_csrf_is_required_for_mutations(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.coach)
        response = client.post(reverse("log-set", args=[self.item.pk]), self.payload())
        self.assertEqual(response.status_code, 403)
        self.assertFalse(SetLog.objects.exists())

    def test_names_are_escaped_in_html(self):
        self.athlete.name = '<script>alert("test")</script>'
        self.athlete.save()
        response = self.client.get(reverse("dashboard"))
        self.assertNotContains(response, '<script>')
        self.assertContains(response, '&lt;script&gt;')

    def test_seed_demo_is_repeatable_and_scoped_to_user(self):
        for _ in range(2):
            call_command("seed_demo", username=self.coach.username, stdout=StringIO())
        self.assertEqual(Athlete.objects.filter(coach=self.coach, name="Demó sportoló · szintetikus").count(), 1)
        self.assertFalse(Athlete.objects.filter(coach=self.other).exists())
