from django.core.management.base import BaseCommand, CommandError

from ops.backup import BackupError, restore_backup


class Command(BaseCommand):
    help = "Restore the database from a verified backup; the current content is saved as pre-restore-*.sqlite3."

    def add_arguments(self, parser):
        parser.add_argument("--from", dest="source", required=True, help="Backup file to restore.")
        parser.add_argument("--yes", action="store_true", help="Confirm replacing the current database content.")

    def handle(self, *args, **options):
        if not options["yes"]:
            raise CommandError("This replaces the current database content. Stop the servers and rerun with --yes.")
        try:
            safety_copy = restore_backup(options["source"])
        except BackupError as exc:
            raise CommandError(str(exc)) from exc
        self.stdout.write(self.style.SUCCESS(f"Restored. Previous content saved to: {safety_copy or 'n/a (no database)'}"))
