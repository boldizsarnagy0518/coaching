from datetime import date
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from training.models import Athlete, TrainingPlan, TrainingSession, PlannedSet


class Command(BaseCommand):
    help = "Create synthetic training examples for an existing coach; never changes credentials."

    def add_arguments(self, parser):
        parser.add_argument("--username", required=True)

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            coach = get_user_model().objects.get(username=options["username"])
        except get_user_model().DoesNotExist as exc:
            raise CommandError("Előbb hozz létre egy felhasználót: python manage.py createsuperuser") from exc
        athlete, _ = Athlete.objects.get_or_create(coach=coach, name="Demó sportoló · szintetikus")
        plan, _ = TrainingPlan.objects.get_or_create(athlete=athlete, title="Demó alapozó blokk")
        session, created = TrainingSession.objects.get_or_create(plan=plan, title="A nap · erőalap", defaults={"scheduled_date": date.today()})
        if created:
            PlannedSet.objects.bulk_create([
                PlannedSet(session=session, exercise="Szünetes fekvenyomás", reps=5, weight_kg=60),
                PlannedSet(session=session, exercise="Szünetes fekvenyomás", reps=5, weight_kg=60),
                PlannedSet(session=session, exercise="Guggolás", reps=5, weight_kg=80),
            ])
        self.stdout.write(self.style.SUCCESS("Szintetikus demóadat elkészült; meglévő adatot nem írtunk át."))
