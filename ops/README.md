# Operations: logging, health check, backups and stability

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

Everything that keeps the app observable and its data safe while running: request IDs and request logs, domain event logs, the health check, SQLite settings for two processes sharing one file, and verified backups. The code lives in [coaching/observability.py](../coaching/observability.py), [coaching/configuration.py](../coaching/configuration.py) and this app ([backup.py](backup.py), [backup_db](management/commands/backup_db.py)).

## Current state

| Area | Works | Still missing |
|---|---|---|
| Request IDs | Every response has `X-Request-ID`; a safe incoming ID (8–64 of `A-Z a-z 0-9 _ -`) is reused, anything else is replaced | Propagation to external services (none exist yet) |
| Request log | One line per request: method, path without query string, status, duration, user id; 5xx logged as warnings | Metrics aggregation, dashboards |
| Domain events | `event=… key=value` lines for set logging (saved, duplicate, conflict, refused), memory (created, refused, reviewed), plan changes (proposed, approved, stale, rejected), MCP tool calls (tool, outcome, duration), backups | Alerting |
| Log output | stderr always; rotating file `.local/logs/app.log` (2 MB × 5) when `DEBUG` and not testing, or with `COACHING_LOG_FILE=true` | Central log collection |
| Health check | `GET /healthz` without login: `{"status": "ok", "database": "ok"}` or HTTP 503 | Deeper checks (disk space, backup age) |
| SQLite | WAL journal, 20 s busy timeout, `IMMEDIATE` write transactions, `synchronous=NORMAL` | PostgreSQL for multi-user hosting |
| Backups | `backup_db`: online backup API, integrity check, retention (default 14), 60 s timeout, refuses to run inside a transaction; `--verify FILE` | Scheduled runs, off-machine copies, automated restore drill |
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

**Restore** (manual, tested only via `--verify` so far): stop the web server and the MCP server, keep a copy of the current `db.sqlite3`, delete `db.sqlite3-wal` and `db.sqlite3-shm` if present, copy the chosen backup to `db.sqlite3`, start the server and open `/healthz`. `COACHING_DB_PATH` can point the app at a different database file, for example to inspect a backup without touching the live data.

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
| `closing()` around ad-hoc SQLite connections | sqlite3's context manager does not close the file; on Windows the open handle blocked deleting old backups (found by a test) | All direct SQLite access must close explicitly |
| Generic MCP error messages with a reference | The AI client must not see internal details or stack traces | Use the reference to find the traceback in the log |
| `/healthz` is public | Monitoring must work without a session | It reveals only ok/error |

## Verification

`uv run python manage.py test ops`: 12 tests for the health check, request ID reuse and replacement, request and event logs (including that query strings and memory content are not logged), MCP error isolation and refusal outcomes, 404 and 409 pages, verified backups, retention, the command, `--verify` on a broken file and the transaction guard. Last local result: all passed (62/62 in the full suite, 94% branch coverage).

Manual checks on the local database: `PRAGMA journal_mode` returns `wal`, `busy_timeout` is 20000 ms, and `backup_db` wrote and verified a backup. A concurrent load test of the web server and the MCP server together has not been done.

## Next step

1. Schedule `backup_db` (Windows Task Scheduler) and copy backups off the machine.
2. Do one real restore drill with the procedure above and record the result here.
3. Before any hosted deployment: PostgreSQL, central logs, alerting on 5xx and failed backups, and a Content Security Policy.
