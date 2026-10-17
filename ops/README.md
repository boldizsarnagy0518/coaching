# Operations: logging, health check, backups and stability

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

Everything that keeps the app observable and its data safe while running: request IDs and request logs, domain event logs, the health check, SQLite settings for two processes sharing one file, and verified backups. The code lives in [coaching/observability.py](../coaching/observability.py), [coaching/configuration.py](../coaching/configuration.py) and this app ([backup.py](backup.py), [backup_db](management/commands/backup_db.py), [restore_db](management/commands/restore_db.py), [create_demo_coach](management/commands/create_demo_coach.py)); the scheduling script is [scripts/register-backup-task.ps1](../scripts/register-backup-task.ps1).

## Current state

| Area | Works | Still missing |
|---|---|---|
| Request IDs | Every response has `X-Request-ID`; a safe incoming ID (8–64 of `A-Z a-z 0-9 _ -`) is reused, anything else is replaced | Propagation to external services (none exist yet) |
| Request log | One line per request: method, path without query string, status, duration, user id; 5xx logged as warnings; HEAD probes only at DEBUG | Metrics aggregation, dashboards |
| Domain events | `event=… key=value` lines for set logging (saved, duplicate, conflict, refused), memory (created, refused, reviewed), plan changes (proposed, approved, stale, rejected), MCP tool calls (tool, outcome, duration), backups | Alerting |
| Log output | stderr always; rotating file `.local/logs/app.log` (2 MB × 5) when `DEBUG` and not testing, or with `COACHING_LOG_FILE=true` | Central log collection |
| Health check | `GET /healthz` without login: `{"status": "ok", "database": "ok"}` or HTTP 503 | Deeper checks (disk space, backup age) |
| SQLite | WAL journal, 20 s busy timeout, `IMMEDIATE` write transactions, `synchronous=NORMAL` | PostgreSQL for multi-user hosting |
| Backups | `backup_db`: online backup API, integrity check, retention (default 14), 60 s timeout, refuses to run inside a transaction, never overwrites a same-second backup; `--verify FILE` | Off-machine copy |
| Restore | `restore_db --from FILE --yes`: verifies the backup, refuses while another process holds the database, saves the current content as `pre-restore-*.sqlite3`, copies with the backup API and re-checks integrity | Restoring a single athlete or table |
| Scheduling | [register-backup-task.ps1](../scripts/register-backup-task.ps1) registers a daily Windows task, optionally copying the newest backup to another folder (`-CopyTo`). Not registered on the development machine: it was tried and then removed at the user's request (the console window that opens on each run was not wanted) | Backups run only when started manually; the task opens a visible console window while it runs |
| Demo login | `create_demo_coach` (debug only) creates an account with a generated password stored in `.local/demo-credentials.txt`, never printed and never reset | — |
| Error pages | Hungarian 404 and 500 pages; log conflicts (409) render a page with a link back instead of plain text | Custom 403/CSRF page |
| MCP robustness | Each tool call gets a correlation id (`mcp-…`), fresh DB connection handling, timing, and error isolation: unexpected errors return a generic message with a reference, the traceback goes to the log | Rate limiting per client |
| Security headers | `nosniff`, `Referrer-Policy: same-origin`, `X-Frame-Options: DENY`, HTTP-only session cookie | Content Security Policy |

## Usage

```powershell
# Health check while the server runs
curl http://127.0.0.1:8765/healthz

# Verified backup into .local/backups, keeping the newest 14
uv run python manage.py backup_db
uv run python manage.py backup_db --keep 30 --dir D:\coaching-backups
uv run python manage.py backup_db --verify .local\backups\db-20261017-125155.sqlite3

# More or less logging
$env:DJANGO_LOG_LEVEL = "DEBUG"
```

```powershell
# Restore: stop the web server and the MCP server first
uv run python manage.py restore_db --from .local\backups\db-20261017-125155.sqlite3 --yes

# Daily backup at 21:30 with a copy to a synced folder (run it yourself; affects only your user's task list)
.\scripts\register-backup-task.ps1 -Time 21:30 -CopyTo "$env:OneDrive\CoachingBackups"

# Demo account and data in a separate database, for trying the app
$env:COACHING_DB_PATH = ".local/demo.sqlite3"
uv run python manage.py migrate
uv run python manage.py create_demo_coach
uv run python manage.py seed_demo --username demo-coach
```

After a restore, start the server and open `/healthz`. `COACHING_DB_PATH` points the app at a different database file, for example to inspect a backup or to keep demo data apart from real data. The `coaching-demo` entry in `.claude/launch.json` starts the server on the demo database.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Log ids, statuses and numbers only, never free text | Names, memory content and reasons can be personal or health data | Logs show *what* happened, not *what was written*; look up details in the app |
| Query strings are not logged | They can contain user input | The path alone identifies the view |
| Logs to stderr | The MCP server uses stdout for its protocol | Run the MCP client's own log view or the log file to see server lines |
| Plain `key=value` lines instead of JSON | Readable in a terminal and still easy to grep or parse | A log platform may need a parser rule |
| WAL + busy timeout + `IMMEDIATE` | The web server and the MCP server write to the same file; this avoids "database is locked" errors and lets readers continue during writes | Still a single-machine setup; extra `-wal`/`-shm` files sit next to the database |
| SQLite online backup API with a progress deadline | Consistent copy while the app runs; Python's backup otherwise retries a locked database forever (found by a hanging test) | A very busy database can make a backup fail after 60 s; rerun it |
| Integrity check on every backup | A backup that cannot be read is worse than none | A failed copy is renamed to `.corrupt` and the command exits with an error |
| Restore through the backup API with an exclusive-lock probe and a safety copy | A running server must not be overwritten mid-write; a wrong restore must be undoable | The servers have to be stopped; the safety copy needs disk space |
| `--yes` required for restore | Replacing data must be a deliberate step | Scripts must pass the flag explicitly |
| ASCII-only management command output | A cp1252 Windows console crashed on "ő" and rolled back `seed_demo` (found while preparing the browser check) | Command messages are English; the UI stays Hungarian |
| `closing()` around ad-hoc SQLite connections | sqlite3's context manager does not close the file; on Windows the open handle blocked deleting old backups (found by a test) | All direct SQLite access must close explicitly |
| Generic MCP error messages with a reference | The AI client must not see internal details or stack traces | Use the reference to find the traceback in the log |
| `/healthz` is public | Monitoring must work without a session | It reveals only ok/error |

## Verification

`uv run python manage.py test ops`: 16 tests for the health check, request ID reuse and replacement, request and event logs (including that query strings, HEAD probes and memory content are not logged at info level), MCP error isolation and refusal outcomes, 404 and 409 pages, verified backups, retention, the command, `--verify` on a broken file, the transaction guard, restore with safety copy, restore refusals (broken, missing, same file, busy database) and the `--yes` requirement. Last local result: all passed (68/68 in the full suite, 94% branch coverage).

Manual checks on the local database: `PRAGMA journal_mode` returns `wal`, `busy_timeout` is 20000 ms, and `backup_db` wrote and verified a backup.

**Restore drill (17 October 2026),** on a copy of the local database via `COACHING_DB_PATH`: created a user, took a backup, created a second user, ran `restore_db --yes`. Result: only the first user remained, a `pre-restore` copy was written, and `manage.py check` passed. The drill files were deleted afterwards.

**Browser check (17 October 2026),** at phone width (375 px) on the demo database: login, athlete page with memory counter, memory page (proposal, active entries, form), session page, move proposal with the before/after table and the same-day warning, approval and the plan page at version 2. No console errors; request and event log lines appeared as expected. Found and fixed: the change and log forms linked back to the athlete list instead of the session, and HEAD probes flooded the log.

**Scheduled backup (17 October 2026):** the `CoachingBackup` task was registered for 21:00 daily and started once manually: result code 0 and a new verified backup in `.local/backups`. It was then unregistered at the user's request; the script is kept for later use.

A concurrent load test of the web server and the MCP server together has not been done.

## Next step

1. If scheduled backups are wanted again: a hidden-window launcher for the task, and `-CopyTo` for an off-machine copy.
2. A short concurrency test: web server and MCP server writing at the same time.
3. Before any hosted deployment: PostgreSQL, central logs, alerting on 5xx and failed backups, and a Content Security Policy.
