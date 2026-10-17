# Database schema and migrations

[Training module](../README.md) · Updated: 17 October 2026

## Responsibility

Reproducible creation and later modification of the database structure.

## Current state

[0001_initial.py](0001_initial.py) creates the five training models, their relations, and the uniqueness and value-range constraints. Login and session tables are created by Django's own migrations.

**Not done:** content versioning of training plans, a PostgreSQL migration trial, an operational restore procedure. The database schema version is not the same thing as the version of an athlete's plan.

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

Tests use a separate test database. The first migration ran locally; the latest check found no missing migration.

## Next step

Plan versioning needs a new migration that keeps earlier logs. Do not rewrite a shared or applied migration afterwards; record the next change in a new file.
