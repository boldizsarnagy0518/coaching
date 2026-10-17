"""Consistent SQLite backups with an integrity check and simple retention."""
import sqlite3
import time
from contextlib import closing
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.db import connection

from coaching.observability import log_event

DEFAULT_KEEP = 14
BACKUP_TIMEOUT_SECONDS = 60
PAGES_PER_STEP = 256


class BackupError(RuntimeError):
    pass


def default_backup_dir():
    return Path(settings.BASE_DIR) / ".local" / "backups"


def integrity_check(path):
    # sqlite3's context manager only ends the transaction; closing() releases the file (Windows locks it).
    with closing(sqlite3.connect(path)) as db:
        result = db.execute("PRAGMA integrity_check").fetchone()[0]
    return result == "ok", result


def create_backup(target_dir=None, keep=DEFAULT_KEEP, now=None, timeout=BACKUP_TIMEOUT_SECONDS):
    """Copy the live database with SQLite's online backup API, verify the copy and prune old copies.

    The backup API takes a consistent snapshot even while the web or MCP server is writing.
    """
    if connection.vendor != "sqlite":
        raise BackupError("Only SQLite databases are supported by this command.")
    if connection.in_atomic_block:
        # The source would hold a lock that the backup waits for; refuse instead of hanging.
        raise BackupError("Backups cannot run inside a database transaction.")
    target_dir = Path(target_dir or default_backup_dir())
    target_dir.mkdir(parents=True, exist_ok=True)
    stamp = (now or datetime.now()).strftime("%Y%m%d-%H%M%S")
    target = target_dir / f"db-{stamp}.sqlite3"
    connection.ensure_connection()
    deadline = time.monotonic() + timeout

    def progress(status, remaining, total):
        # sqlite3 retries busy/locked steps forever; give up after the deadline instead.
        if time.monotonic() > deadline:
            raise BackupError(f"Backup did not finish within {timeout} seconds (database busy).")

    destination = sqlite3.connect(target)
    try:
        connection.connection.backup(destination, pages=PAGES_PER_STEP, progress=progress)
    except BackupError:
        destination.close()
        target.unlink(missing_ok=True)
        log_event("backup.failed", reason="timeout")
        raise
    finally:
        destination.close()
    ok, detail = integrity_check(target)
    if not ok:
        target.rename(target.with_suffix(".corrupt"))
        log_event("backup.failed", reason="integrity_check")
        raise BackupError(f"Backup failed the integrity check: {detail}")
    removed = prune(target_dir, keep)
    log_event("backup.created", size_bytes=target.stat().st_size, removed=len(removed))
    return target, removed


def prune(target_dir, keep):
    backups = sorted(Path(target_dir).glob("db-*.sqlite3"))
    old = backups[:-keep] if keep > 0 else []
    for path in old:
        path.unlink()
    return old
