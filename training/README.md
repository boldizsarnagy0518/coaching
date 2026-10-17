# Athletes, plans and training log

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

The athlete → plan → session → prescribed set → actual performance workflow. Currently the coach records the data; athletes have no account of their own.

## Current state

| Sub-part | Works | Still missing |
|---|---|---|
| Athlete | Name, assignment to a coach, own list | Detailed profile, athlete login |
| Plan and session | Plan title, session name and scheduled date | Plan versions, missed and moved sessions |
| Prescribed set | Free-text exercise variant, reps, kg | Exercise catalogue, swaps and target RPE |
| Actual performance | Reps, kg, optional RPE, recording time | Later correction, separate actual session time |
| Submission | An identical repeated request does not duplicate; conflicts return 409 | Log correction workflow |
| Access | Every app view filters by the logged-in coach | Shared coaching, athlete role |
| CSV transfer | Export and read-only CSV / Google Sheets preview | Column mapping and approved import, see [data transfer](../docs/data-transfer/README.md) |

Main files: [models.py](models.py) data, [forms.py](forms.py) input, [views.py](views.py) workflow and permissions, [urls.py](urls.py) routes, [transfers.py](transfers.py) CSV reading and restricted download, [tests.py](tests.py) and [test_transfers.py](test_transfers.py) checks.

## Data relations

`User → Athlete → TrainingPlan → TrainingSession → PlannedSet → SetLog`

At most one performance record can belong to a prescribed set. Prescribed and actual values are kept in separate fields and separate records. Creating a log entry does not modify the prescription. This is **not** a full audit log or an immutable plan history; those are not implemented yet.

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

The ranges 1–100 target reps, 0–100 actual reps and 1–10 RPE are **input limits**, not professional load recommendations. Formal validity does not prove that a training plan is appropriate.

## Verification

Run `uv run python manage.py test training` from the project root. The module's two test files contain 26 tests in total:

- [tests.py](tests.py), 14 tests: the full creation path, blocking another coach's access, resubmission, conflicts, invalid values, optional RPE, partial logging, CSRF, HTML escaping and repeatable demo data.
- [test_transfers.py](test_transfers.py), 12 tests: CSV export and preview, URL and redirect restrictions, access control, and that the preview page shows no error on first load.

Last local result: 26/26 passed.

## Next step

Plan versions, then a structured move request, a reviewable proposal and coach approval. The module currently does not re-plan, does not call AI and gives no injury-management advice.

Related details: [database migrations](migrations/README.md), [demo data](management/README.md), [user interface](../templates/README.md).
