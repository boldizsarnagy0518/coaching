# Application configuration and login

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

Assembles the Django project: database, sessions, login, URL routing, templates and local settings. Training data and its access filtering live in the [training module](../training/README.md).

## Current state

- [settings.py](settings.py) loads the settings from [configuration.py](configuration.py).
- SQLite database in the project root; Hungarian language, Europe/Budapest time zone.
- Django login and POST-based logout; session and CSRF handling.
- [urls.py](urls.py) wires together login, the admin site and the app modules.
- Local development mode by default, accepting localhost host names only. The secret key comes from an environment variable or from a local, Git-ignored file.

**Not done:** production deployment configuration, athlete role, self-service registration and password reset. The `createsuperuser` command used in the README also grants admin rights; it is a developer convenience, not the future customer account creation.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| One Django application | In a Python-centred side project it provides data handling, forms and authentication together | No separate frontend or API service for now |
| SQLite locally | The first workflow can be tried without an external database | PostgreSQL and its concurrent-write behaviour are not verified yet |
| Django's built-in authentication | No custom password and session handling to write | Access to resources is still filtered separately |
| Locally generated secret key | No shared development secret committed to the repo | The contents of `.local/` must not be uploaded |
| Environment key required in non-debug mode | A configuration meant for production must not start without a secret | The switch alone does not make the system production-ready |
| Europe/Budapest time zone | First users are in Hungary | Revisit after the move to Dublin or when users span time zones |

## Verification

From the project root: `uv run python manage.py check`. Login-protected views and CSRF protection are covered by the [tests](../training/tests.py). The local login page's HTTP response has been checked; a full browser usability check is not documented yet.

## Next step

Before athletes get access, a separate role and permission model is needed. Before any external deployment, a separate configuration, backup and restore, secret management and an operational review are required.
