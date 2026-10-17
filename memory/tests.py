from datetime import date

from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from training.models import Athlete, PlannedSet, SetLog, TrainingPlan, TrainingSession

from . import mcp_tools, services
from .management.commands.run_mcp_server import build_server
from .models import AthleteMemory, MemorySource, MemoryStatus

PAIN = "pain_injury"


def entry(content="Jobb térd fáj mély guggolásnál", category=PAIN, **extra):
    return services.MemoryInput(category=category, content=content, **extra)


class MemoryRuleTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")

    def test_coach_entry_is_active_and_normalised(self):
        memory = services.create_memory(self.coach, self.athlete, entry("  Jobb térd   fáj mély guggolásnál "),
            MemorySource.COACH)
        self.assertEqual(memory.status, MemoryStatus.ACTIVE)
        self.assertEqual(memory.content, "Jobb térd fáj mély guggolásnál")

    def test_rejects_short_unknown_and_foreign(self):
        for data in [entry("térd"), entry(category="mood"), entry("x" * 301)]:
            with self.subTest(data=data), self.assertRaises(services.MemoryRuleError):
                services.create_memory(self.coach, self.athlete, data, MemorySource.COACH)
        with self.assertRaises(PermissionError):
            services.create_memory(self.other, self.athlete, entry(), MemorySource.COACH)
        self.assertFalse(AthleteMemory.objects.exists())

    def test_near_duplicates_are_rejected_per_category(self):
        services.create_memory(self.coach, self.athlete, entry(), MemorySource.COACH)
        for text in ["jobb térd fáj mély guggolásnál!", "Jobb térd fáj mély guggolásnál, főleg reggel",
                "Jobb térd fáj a mély guggolásnál"]:
            with self.subTest(text=text), self.assertRaises(services.DuplicateMemoryError):
                services.create_memory(self.coach, self.athlete, entry(text), MemorySource.COACH)
        # Same text in another category, or a resolved entry, does not block a new one.
        services.create_memory(self.coach, self.athlete, entry(category="technique"), MemorySource.COACH)
        self.assertEqual(AthleteMemory.objects.count(), 2)

    def test_ai_proposal_needs_reason_and_review(self):
        with self.assertRaises(services.MemoryRuleError):
            services.create_memory(self.coach, self.athlete, entry(reason="fontos"), MemorySource.AI_PROPOSAL)
        memory = services.create_memory(self.coach, self.athlete,
            entry(reason="Visszatérő panasz, a guggolás mélységét befolyásolja"), MemorySource.AI_PROPOSAL)
        self.assertEqual(memory.status, MemoryStatus.PROPOSED)
        services.approve(self.coach, memory)
        self.assertEqual(memory.status, MemoryStatus.ACTIVE)
        self.assertEqual(memory.reviewed_by, self.coach)
        with self.assertRaises(services.MemoryRuleError):
            services.reject(self.coach, memory)

    def test_pending_proposals_are_capped(self):
        facts = ["Guggolásnál a térd befelé dől", "Fekvenyomásnál elemeli a fenekét", "Felhúzásban kerekedik a hát",
            "Hétfőn csak negyven perce van", "Otthon nincs fekvenyomópad", "Versenyre márciusban készül",
            "Szereti a szünetes variációkat", "Nagy volumen után két napig fáradt", "Délutáni edzésen erősebb",
            "Edző döntése: nincs maximális kísérlet decemberig"]
        self.assertEqual(len(facts), services.MAX_PENDING_PROPOSALS)
        for fact in facts:
            services.create_memory(self.coach, self.athlete, entry(fact, category="response",
                reason="Hosszabb távon is releváns"), MemorySource.AI_PROPOSAL)
        with self.assertRaises(services.MemoryRuleError):
            services.create_memory(self.coach, self.athlete, entry("Teljesen más új megfigyelés",
                category="goal", reason="Hosszabb távon is releváns"), MemorySource.AI_PROPOSAL)

    def test_resolve_and_reactivate(self):
        memory = services.create_memory(self.coach, self.athlete, entry(), MemorySource.COACH)
        services.resolve(self.coach, memory)
        services.create_memory(self.coach, self.athlete, entry(), MemorySource.COACH)  # resolved is not a duplicate
        with self.assertRaises(PermissionError):
            services.reactivate(self.other, memory)


class MemoryViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")

    def setUp(self):
        self.client.force_login(self.coach)
        self.url = reverse("athlete-memory", args=[self.athlete.pk])

    def test_coach_adds_entry_and_sees_it(self):
        response = self.client.post(self.url, {"category": PAIN, "content": "Bal váll fáj fekvenyomásnál",
            "observed_on": "2026-10-17"}, follow=True)
        self.assertContains(response, "Bal váll fáj fekvenyomásnál")
        memory = AthleteMemory.objects.get()
        self.assertEqual((memory.status, memory.source), (MemoryStatus.ACTIVE, MemorySource.COACH))
        self.assertContains(self.client.get(reverse("athlete", args=[self.athlete.pk])), "1 aktív")

    def test_rule_errors_are_shown_not_saved(self):
        response = self.client.post(self.url, {"category": PAIN, "content": "rövid", "observed_on": "2026-10-17"})
        self.assertContains(response, "Túl rövid bejegyzés")
        self.assertFalse(AthleteMemory.objects.exists())

    def test_review_actions(self):
        memory = services.create_memory(self.coach, self.athlete, entry(reason="Visszatérő, fontos panasz"),
            MemorySource.AI_PROPOSAL)
        self.assertContains(self.client.get(self.url), "Jóváhagyásra váró javaslatok (1)")
        self.assertEqual(self.client.get(reverse("memory-review", args=[memory.pk, "approve"])).status_code, 405)
        self.assertEqual(self.client.post(reverse("memory-review", args=[memory.pk, "delete"])).status_code, 404)
        self.client.post(reverse("memory-review", args=[memory.pk, "approve"]))
        memory.refresh_from_db()
        self.assertEqual(memory.status, MemoryStatus.ACTIVE)

    def test_other_coach_is_blocked(self):
        memory = services.create_memory(self.coach, self.athlete, entry(), MemorySource.COACH)
        self.client.force_login(self.other)
        self.assertEqual(self.client.get(self.url).status_code, 404)
        self.assertEqual(self.client.post(reverse("memory-review", args=[memory.pk, "resolve"])).status_code, 404)
        memory.refresh_from_db()
        self.assertEqual(memory.status, MemoryStatus.ACTIVE)
        self.client.logout()
        self.assertEqual(self.client.get(self.url).status_code, 302)


class McpToolTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coach = get_user_model().objects.create_user(username="coach-a")
        cls.other = get_user_model().objects.create_user(username="coach-b")
        cls.athlete = Athlete.objects.create(coach=cls.coach, name="Szintetikus")
        cls.foreign = Athlete.objects.create(coach=cls.other, name="Idegen")
        plan = TrainingPlan.objects.create(athlete=cls.athlete, title="Blokk")
        session = TrainingSession.objects.create(plan=plan, title="A nap", scheduled_date=date(2026, 10, 1))
        item = PlannedSet.objects.create(session=session, exercise="Guggolás", reps=5, weight_kg=100)
        SetLog.objects.create(planned_set=item, reps=4, weight_kg=100, rpe=9)
        services.create_memory(cls.coach, cls.athlete, entry(), MemorySource.COACH)

    def test_scoped_listing_and_context(self):
        self.assertEqual(mcp_tools.list_athletes(self.coach), [{"id": self.athlete.pk, "name": "Szintetikus"}])
        context = mcp_tools.get_athlete_context(self.coach, self.athlete.pk)
        self.assertEqual(context["active_memories"][0]["content"], "Jobb térd fáj mély guggolásnál")
        self.assertEqual(context["recent_sessions"][0]["sets"][0]["actual"], "100.00 kg x 4")
        with self.assertRaises(ValueError):
            mcp_tools.get_athlete_context(self.coach, self.foreign.pk)

    def test_search_only_own_memories(self):
        services.create_memory(self.other, self.foreign, entry(), MemorySource.COACH)
        results = mcp_tools.search_memories(self.coach, "térd")
        self.assertEqual([r["athlete_id"] for r in results], [self.athlete.pk])

    def test_writes_follow_selection_rules(self):
        duplicate = mcp_tools.propose_memory(self.coach, self.athlete.pk, PAIN, "jobb térd fáj mély guggolásnál",
            "Visszatérő panasz")
        self.assertEqual(duplicate["reason"], "duplicate")
        proposal = mcp_tools.propose_memory(self.coach, self.athlete.pk, "preference",
            "Reggeli edzést preferál hétköznap", "Ütemezésnél számít")
        self.assertEqual(proposal["memory"]["status"], MemoryStatus.PROPOSED)
        saved = mcp_tools.save_memory_on_coach_request(self.coach, self.athlete.pk, "goal",
            "Márciusi országos bajnokság a fő cél")
        self.assertEqual(saved["memory"]["status"], MemoryStatus.ACTIVE)
        self.assertEqual(saved["memory"]["source"], MemorySource.AI_COACH_REQUEST)

    def test_server_exposes_tools_end_to_end(self):
        server = build_server(self.coach)
        names = {tool.name for tool in async_to_sync(server.list_tools)()}
        self.assertEqual(names, {"list_athletes", "get_athlete_context", "search_memories", "propose_memory",
            "save_memory_on_coach_request"})
        result = async_to_sync(server.call_tool)("list_athletes", {})
        self.assertIn("Szintetikus", str(result))
