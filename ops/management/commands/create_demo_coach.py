"""Create a local demo coach with a generated password, for trying the app or browser checks."""
import secrets
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

CREDENTIALS_FILE = Path(settings.BASE_DIR) / ".local" / "demo-credentials.txt"


class Command(BaseCommand):
    help = ("Create a demo coach (development only). The generated password is written to "
            ".local/demo-credentials.txt, never printed.")

    def add_arguments(self, parser):
        parser.add_argument("--username", default="demo-coach")

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError("Demo accounts can only be created in local development mode.")
        username = options["username"]
        if get_user_model().objects.filter(username=username).exists():
            raise CommandError(f"User {username!r} already exists; its password is left unchanged.")
        password = secrets.token_urlsafe(18)
        get_user_model().objects.create_user(username=username, password=password)
        CREDENTIALS_FILE.parent.mkdir(parents=True, exist_ok=True)
        CREDENTIALS_FILE.write_text(f"username={username}\npassword={password}\n", encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Demo coach {username!r} created; credentials in {CREDENTIALS_FILE}."))
