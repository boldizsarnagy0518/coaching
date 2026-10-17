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
