# Athletes, plans and training log

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

The athlete → plan → session → prescribed set → actual performance workflow, plus versioned session changes with a before/after view and coach approval: move or skip a session, move the remaining sets of a partially logged session, or reschedule several sessions at once. Currently the coach records the data; athletes have no account of their own.

## Current state

| Sub-part | Works | Still missing |
|---|---|---|
| Athlete | Name, assignment to a coach, own list | Detailed profile, athlete login |
| Plan and session | Plan title, session name, scheduled date, session status (planned/skipped), plan version number | Adding or removing sessions as part of a change |
| Plan changes | Move or skip one unlogged session; move the unlogged sets of a partial session to a new continuation session; reschedule several unlogged sessions as one batch (e.g. 3 → 4 training days). Proposal → before/after view → approve or reject; a batch is approved or rejected as a whole and creates one version; stale proposals are refused | Load, volume and exercise changes; automatic suggestions of a new weekly pattern |
| Prescribed set | Free-text exercise variant, reps, kg | Exercise catalogue, swaps and target RPE |
| Actual performance | Reps, kg, optional RPE, recording time | Later correction, separate actual session time |
| Submission | An identical repeated request does not duplicate; conflicts return a 409 page with a link back to the session; every outcome is logged as an event | Log correction workflow |
| Access | Every app view filters by the logged-in coach | Shared coaching, athlete role |
| CSV transfer | Export and read-only CSV / Google Sheets preview | Column mapping and approved import, see [data transfer](../docs/data-transfer/README.md) |
| Athlete page | Link to the athlete memory with active and pending counts | The memory itself lives in the [memory module](../memory/README.md) |

Main files: [models.py](models.py) data, [forms.py](forms.py) input, [views.py](views.py) workflow and permissions, [urls.py](urls.py) routes, [transfers.py](transfers.py) CSV reading and restricted download, [plan_changes.py](plan_changes.py) change rules and versioning, [tests.py](tests.py), [test_transfers.py](test_transfers.py) and [test_plan_changes.py](test_plan_changes.py) checks.

## Data relations

`User → Athlete → TrainingPlan → TrainingSession → PlannedSet → SetLog`

`TrainingPlan → PlanChange → TrainingSession` (each change records the plan version it was based on, the old and new date or status, and the version it produced; batch items share a `batch` id; a remaining-sets move records the continuation session and the number of moved sets)

At most one performance record can belong to a prescribed set. Prescribed and actual values are kept in separate fields and separate records. Creating a log entry does not modify the prescription. Plan history is kept as an event log of approved changes (with before/after values), not as full snapshots of every plan version; prescribed sets themselves are not versioned yet.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Separate prescription and performance | What the coach asked for and what happened remain comparable | Plan adjustment will need a link to plan versions |
| One log record per set | A clear first logging model with a uniqueness constraint enforced by the database | Extra attempts and corrections cannot yet be handled as separate events |
| Unique submission UUID | A network retry must not create a new performance record | Repeating the same UUID with the same data is accepted; different content is a conflict |
| Database transaction and uniqueness constraint | Duplication is prevented not only by the UI | Load testing of concurrent requests is still missing |
| Server-side coach filtering | An athlete ID sent by the client is not a permission | Every new read/write view needs the same filter |
| Actual reps may be zero, RPE optional | Failed sets and missing estimates can also be recorded | A logged set is not necessarily a successful set |
| Weight as decimal kg | Prescription and performance are exactly comparable | No pounds or unit conversion |
| `PROTECT` on relations | History cannot be deleted accidentally by cascading | The final data-protection deletion process is separate work |
| Changes are proposals first, also for the coach | The core of the product is the reviewable before/after step | Two clicks instead of one for simple moves |
| Version number + change records instead of full plan snapshots | Small, readable history that covers moves and skips | Load or exercise changes will need prescription versioning |
| Optimistic check on approval (`base_version`) | An approval based on an outdated view must not overwrite a newer plan | Any approved change makes other pending proposals of the plan stale |
| Only unlogged sessions can be moved or skipped; skipped sessions cannot be logged | Logged work is never rewritten or duplicated | A partial session uses the remaining-sets move instead |
| Remaining sets move to a new continuation session | Logged sets stay with the day they were done; the rest gets its own date | The continuation is a separate session titled "… (folytatás)" |
| Batch reschedule: all or nothing, one version | A new weekly pattern must not be half applied | If any session got logged meanwhile, the whole batch goes stale |
| Pending-proposal cap counts a batch once | A reschedule of many sessions is one decision for the coach | A batch is limited to 20 sessions |
| AI can only propose (`source=ai`, reason required) | The coach keeps control of the plan | Proposals still have to be reviewed in the app |

The ranges 1–100 target reps, 0–100 actual reps and 1–10 RPE are **input limits**, not professional load recommendations. Formal validity does not prove that a training plan is appropriate.

## Verification

Run `uv run python manage.py test training` from the project root. The module's three test files contain 48 tests in total:

- [tests.py](tests.py), 15 tests: the full creation path, blocking another coach's access, resubmission, conflicts, invalid values, optional RPE, partial logging, CSRF, HTML escaping, repeatable demo data with ASCII-only output, and the demo coach command.
- [test_transfers.py](test_transfers.py), 12 tests: CSV export and preview, URL and redirect restrictions, access control, and that the preview page shows no error on first load.
- [test_plan_changes.py](test_plan_changes.py), 21 tests: dashboard and athlete-page counts that treat a batch as one item, remaining-sets moves (result, rules, staleness, session-page button), batches (one version, all-or-nothing staleness, rules, reject, view and plan listing, AI tool), the change form's link back to the session, move and skip with versioning, stale proposals, logged sessions, input rules, same-day conflict in the preview, the full view flow, access isolation and the AI proposal tool.

Last local result: 48/48 passed (81/81 in the full suite including the [memory](../memory/README.md) and [operations](../ops/README.md) modules).

## Next step

1. Versioned prescriptions, so load and exercise swaps can go through the same approval.
2. Adding or removing sessions inside a proposal (e.g. when going from 3 to 4 days needs a new session, not only new dates).

The module does not re-plan automatically, does not call AI itself and gives no injury-management advice.

Related details: [database migrations](migrations/README.md), [demo data](management/README.md), [user interface](../templates/README.md).
