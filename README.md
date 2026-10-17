# Coaching

An application that supports powerlifting coaches in plan adjustment and training logging.

## Modules and current state

Updated: 17 October 2026. A local coach training-log prototype works. The state, decisions and limits of each part are in its own README.

| Part | State | Details |
|---|---|---|
| Application settings and login | Works for local use | [coaching](coaching/README.md) |
| Athletes, plans and logging | First data flow works; no re-planning | [training](training/README.md) |
| Database schema | First migration done; this is not plan versioning | [migrations](training/migrations/README.md) |
| Demo data and management commands | Synthetic example for an existing account | [management](training/management/README.md) |
| User interface and forms | Hungarian, server-rendered coach screens | [templates](templates/README.md) |
| Styling | One responsive stylesheet | [static](static/README.md) |
| Automated checks | 26 local tests pass; CI defined | [workflows](.github/workflows/README.md) |
| Planning and validation | Documented; market gate still open | [docs](docs/README.md) |
| CSV and Google Sheets | CSV export, file and published-link preview | [Data transfer](docs/data-transfer/README.md) |

Every module README describes, in the same structure, its responsibility, what works and what is missing, the **what–why–consequence** decisions, verification and the next step. When a feature changes, the affected README is updated too. The exact rule is in the [documentation guide](docs/README.md); project rules, including the language rule (English docs and comments, Hungarian UI), are in [AGENTS.md](AGENTS.md).

## Planning

- [Research and product plan](eroemelo_ai_kutatas_es_terv.md)
- [Current schedule](elso_szakasz_utemterv.md): 17 work weeks, 10 + 2 hours per week, with a separate validation gate.

The current schedule refines the research plan's earlier 16-week scenario. Meeting the validation gate has not been proven yet; written code does not replace interview results or a competitor trial.

## Data

Only code, planning material and synthetic examples may go into the repository. Do not commit real athlete data, interviewees' contact details, databases, passwords or API keys. Local data files belong in the Git-ignored `private/` folder.

## Running locally

Python 3.12+ and `uv` are required. Dependency versions are pinned in `uv.lock`.

```powershell
uv sync --locked
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py seed_demo --username YOUR_USERNAME
uv run python manage.py runserver 127.0.0.1:8765
```

Open http://127.0.0.1:8765 and log in with the account you created. Loading demo data is optional and creates only a synthetic session. `createsuperuser` asks for the password interactively; there is no hard-coded demo password. Another coach test account can be created the same way.

## Verification

```powershell
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py test
```

## Current features and limits

Athlete → plan → session → prescribed set → actual performance. A coach can only access their own athletes; prescribed and actual data are stored separately. Repeating an identical log submission does not duplicate. The UI is Hungarian and phone-friendly.

This is a **coach prototype** for local use with synthetic data. CSV export and a CSV / Google Sheets preview exist; approved import, a private Google connection, athlete self-service login, versioned re-planning and AI integration do not yet. Later editing of the log is not done; a different repeated submission returns a 409 conflict and keeps the earlier data.

- [Detailed status and next tasks](docs/implementation-status.md)
- [Validation worksheet](docs/validation-template.md)

## Technology decision

Django 5.2 and server-rendered HTML: one Python application provides authentication, forms, data handling and a mobile-friendly UI. The local trial uses SQLite; moving to PostgreSQL and checking its transactional behaviour is a separate step. There are currently no external AI calls and no API key requirement.

The local secret key is written to the excluded `.local/` folder on first run. The database is excluded too. Development settings accept localhost only. Do not expose the development server publicly: external use requires a separate deployment, data-protection and security work package. `DJANGO_DEBUG=false` requires the `DJANGO_SECRET_KEY` environment variable, but that alone is not a finished production configuration.
