from django.core.management.base import BaseCommand, CommandError

from ops.backup import DEFAULT_KEEP, BackupError, create_backup, integrity_check


class Command(BaseCommand):
    help = "Create a verified SQLite backup in .local/backups (or --dir) and keep the newest --keep copies."

    def add_arguments(self, parser):
        parser.add_argument("--dir", help="Target directory (default: .local/backups).")
        parser.add_argument("--keep", type=int, default=DEFAULT_KEEP, help="Number of backups to keep.")
        parser.add_argument("--verify", metavar="FILE", help="Only run an integrity check on an existing backup file.")

    def handle(self, *args, **options):
        if options["verify"]:
            ok, detail = integrity_check(options["verify"])
            if not ok:
                raise CommandError(f"Integrity check failed: {detail}")
            self.stdout.write(self.style.SUCCESS("Integrity check passed."))
            return
        if options["keep"] < 1:
            raise CommandError("--keep must be at least 1.")
        try:
            target, removed = create_backup(options["dir"], options["keep"])
        except BackupError as exc:
            raise CommandError(str(exc)) from exc
        self.stdout.write(self.style.SUCCESS(f"Backup written and verified: {target} (removed {len(removed)} old)."))
