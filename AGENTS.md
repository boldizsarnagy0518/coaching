# Project working rules

## Language

- Code comments, docstrings, commit messages and all Markdown documentation are written in **English**.
- User-facing UI text (templates, form labels, validation and status messages) stays **Hungarian**, because the first users are Hungarian coaches and athletes.

## Per-module documentation

At the user's request, every self-contained part of the project has a README describing its current state and its decisions, with the reasoning behind them.

- When a feature or the architecture changes, update the affected README in the same change.
- A new self-contained module gets its own README.md, linked from the module index in the root README.
- The structure and template are defined in docs/README.md.
- Keep working features, missing pieces and proposals separate. Never claim validation or test success that was not actually performed.
- When the overall project state changes significantly, also update the docs/implementation-status.md summary.
- Secrets, local databases and personal athlete or interview data must never go into documentation or Git.

## Code quality and observability

- Before committing, run `uv run ruff check .` and the test suite with coverage (`uv run coverage run manage.py test`, `uv run coverage report`); keep coverage at or above the configured threshold.
- Every new rule or failure path gets a test, including permission checks for other coaches.
- Log domain events with `coaching.observability.log_event`, passing only ids, statuses and numbers. Never log names, memory content, reasons or other free text.
- New write paths go through the service modules (`memory/services.py`, `training/plan_changes.py`) so the UI and the MCP server follow the same rules.
- Close every direct `sqlite3` connection explicitly (`contextlib.closing`).
