from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from memory import services
from memory.models import MemorySource
from training.models import Athlete, PlannedSet, TrainingPlan, TrainingSession


class Command(BaseCommand):
    help = "Create synthetic training and memory examples for an existing coach; never changes credentials."

    def add_arguments(self, parser):
        parser.add_argument("--username", required=True)

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            coach = get_user_model().objects.get(username=options["username"])
        except get_user_model().DoesNotExist as exc:
            raise CommandError("Create the user first: python manage.py createsuperuser") from exc
        athlete, _ = Athlete.objects.get_or_create(coach=coach, name="Demó sportoló · szintetikus")
        plan, _ = TrainingPlan.objects.get_or_create(athlete=athlete, title="Demó alapozó blokk")
        today = date.today()
        sessions = [
            ("A nap · erőalap", today, [("Szünetes fekvenyomás", 5, 60), ("Szünetes fekvenyomás", 5, 60),
                ("Guggolás", 5, 80)]),
            ("B nap · felhúzás", today + timedelta(days=3), [("Felhúzás", 3, 110), ("Felhúzás", 3, 110),
                ("Evezés", 8, 50)]),
        ]
        for title, scheduled, sets in sessions:
            session, created = TrainingSession.objects.get_or_create(plan=plan, title=title,
                defaults={"scheduled_date": scheduled})
            if created:  # re-running must not change a demo session already in use
                PlannedSet.objects.bulk_create([PlannedSet(session=session, exercise=exercise, reps=reps,
                    weight_kg=weight) for exercise, reps, weight in sets])
        if not athlete.memories.exists():
            services.create_memory(coach, athlete, services.MemoryInput("technique",
                "Guggolásnál a jobb térd befelé dől nehéz sorozatokon", exercise="Guggolás"), MemorySource.COACH)
            services.create_memory(coach, athlete, services.MemoryInput("preference",
                "Hétköznap csak reggel tud edzeni", reason="Ütemezési javaslatoknál számít"),
                MemorySource.AI_PROPOSAL)
        # Command output stays ASCII: a cp1252 console cannot print Hungarian letters such as "ő".
        self.stdout.write(self.style.SUCCESS("Synthetic demo data ready; existing data was not changed."))
