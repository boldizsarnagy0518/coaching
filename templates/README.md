# User interface and forms

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

The HTML screens served by Django. Input validation and data isolation are the backend's job; templates are not a permission boundary. UI text is Hungarian by design (see [AGENTS.md](../AGENTS.md)).

## Current state

| File | Screen |
|---|---|
| [base.html](base.html) | Header, logout, status messages, shared layout |
| [404.html](404.html), [500.html](500.html) | Error pages; the 500 page is standalone so it renders even if the layout fails |
| [training/conflict.html](training/conflict.html) | 409 page when a log submission would overwrite earlier data or the session is skipped |
| [registration/login.html](registration/login.html) | Coach login |
| [training/dashboard.html](training/dashboard.html) | Own athletes and number of plans |
| [training/athlete.html](training/athlete.html) | One athlete's plans |
| [training/plan.html](training/plan.html) | Sessions of one plan, version number, reschedule button, pending changes (a batch listed once), change history |
| [training/session.html](training/session.html) | Prescribed and actual sets, number of logged sets, move/skip buttons or the remaining-sets button for a partial session, skipped notice |
| [training/plan_change.html](training/plan_change.html) | One change or a whole batch: before/after table with notes (kept/moved sets, new continuation session), same-day conflict, approve/reject |
| [training/form.html](training/form.html) | Shared data entry form; views can set the back link, an intro line and the submit label (also used for the reschedule form, one date per session) |
| [training/transfer.html](training/transfer.html) | CSV / Google Sheets structural preview |
| [memory/athlete_memory.html](memory/athlete_memory.html) | Athlete memory: pending AI proposals, active entries by category, new entry form, resolved history |

**Not done:** athlete self-service UI, drag-and-drop weekly planner, later correction of logs, offline drafts. "Partially completed" is derived from the number of log records; it is not a separate session status model.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Server-rendered HTML | The first data path of a side project needs fewer separate technologies | Every action currently needs a server connection |
| Shared layout and form template | New screens stay consistent with less duplicated code | A specialised logging experience is a later refinement |
| Prescription and actual value shown together | The difference can be checked | No trend or professional evaluation yet |
| Redirect after save | The user sees the saved state | Protection against resubmission is provided by the backend in addition |
| Success message only after a save or an identical resubmission | Invalid data must not look successfully recorded | A conflict shows a 409 page with a link back |

## Verification

The [functional tests](../training/tests.py) and the [memory tests](../memory/tests.py) check responses, the displayed saved state, partial logging and HTML escaping. The login page has been checked over HTTP. A full browser, mobile and accessibility test has not been verified; the previous browser trial was interrupted by a tooling error.

## Next step

A separate usability trial is needed to measure whether logging on a phone can be completed without help. Styling decisions: [static](../static/README.md).
