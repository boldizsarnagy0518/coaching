# Database schema and migrations

[Training module](../README.md) · Updated: 17 October 2026

## Responsibility

Reproducible creation and later modification of the database structure.

## Current state

[0001_initial.py](0001_initial.py) creates the five training models, their relations, and the uniqueness and value-range constraints. [0002_plan_versions_and_changes.py](0002_plan_versions_and_changes.py) adds the plan version number, the session status and the `PlanChange` table; existing plans start at version 1 and existing sessions as planned. [0003_partial_and_batch_changes.py](0003_partial_and_batch_changes.py) adds the `move_rest` kind, the batch id, the continuation session and the moved-set count, and replaces the date/kind constraint. Login and session tables are created by Django's own migrations.

**Not done:** versioning of prescribed sets, a PostgreSQL migration trial, an operational restore procedure. The database schema version is not the same thing as the version of an athlete's plan.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Migration files in the repo | The same schema can be built on another machine and in CI | Every model change needs a migration |
| Database constraints also protect the log | Writes outside the forms cannot bypass the basic limits | Professional correctness needs additional rules |
| The local database is not in Git | Athlete or login data must not be uploaded | Git is not a backup; the working database needs a separate backup |

## Verification and usage

From the project root:

```powershell
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py migrate
uv run python manage.py test training
```

Tests use a separate test database. All three training migrations ran locally (development and demo databases); the latest check found no missing migration.

## Next step

Prescription versioning will need a further migration that keeps earlier logs linked to the prescription they were logged against. Do not rewrite a shared or applied migration afterwards; record the next change in a new file.
