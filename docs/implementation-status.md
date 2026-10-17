# Implementation status

17 October 2026. The current schedule, reworked to 17 work weeks, is the reference.

The detailed state and decision reasoning of each part is available from the [per-module README index](../README.md). Under the [documentation rule](README.md), these are updated together with later development.

## Completed technical work packages

**Training log prototype**

- Django 5.2, local SQLite, versioned database migrations.
- Login and server-side coach data isolation in every app view.
- Creating athletes, plans, sessions and prescribed sets.
- Actual performance in a separate record: reps, kg, optional set RPE.
- Mobile-friendly server-rendered UI, save feedback and partial logging status.
- Repeating an identical submission does not duplicate; a different submission does not overwrite the earlier performance.
- Synthetic demo data for an existing account, without changing passwords.
- Automated functional and access tests, GitHub Actions workflow.

**CSV and Google Sheets transfer**

CSV export, plus a structural preview of an uploaded CSV or a published Google Sheets CSV link. Nothing is imported yet. No private Google authentication. [State and decisions](data-transfer/README.md).

**Athlete memory and MCP server**

Per-athlete curated memory with fixed categories, near-duplicate rejection, reasoned AI proposals that need coach approval, and resolve/reactivate. A local stdio MCP server exposes one coach's athletes, memory and recent sessions to an AI client. [State and decisions](../memory/README.md).

**Plan versions and session changes**

Plans have a version number; a session without logged sets can be moved or skipped, the remaining sets of a partially logged session can be moved to a new continuation session, and several sessions can be rescheduled as one batch (one version, all or nothing), always through a proposal with a before/after view and coach approval. Memory entries can be edited under the same rules as new ones. Approving a proposal based on an outdated version marks it stale; skipped sessions cannot be logged. The AI can propose such changes through the MCP server, but cannot apply them. [State and decisions](../training/README.md).

**Testability, observability and stability**

Lint (ruff) and branch coverage with an 85% gate in CI; request IDs, request and domain event logs without personal text; public `/healthz`; SQLite WAL with busy timeout and immediate write transactions for the web and MCP processes; verified backups with retention and a timeout; error-isolated MCP tool calls; Hungarian 404/500 pages and a 409 conflict page; basic security headers. [State and decisions](../ops/README.md).

Restore command with a safety copy and a recorded restore drill; a backup scheduling script (tried, then unregistered at the user's request; backups are manual); a demo login command; a browser check of the main flows at phone width.

**Verification:** 80 local tests passed (95% branch coverage); the multi-process concurrency check passed after these changes; the online download is tested with a simulated response; a manual stdio smoke test of the MCP server succeeded. Real use in an AI client has not been tried yet.

This is a technical foundation brought forward at the user's request. It does not prove that the validation gate has been met, and it does not mean all tasks of weeks 6–10 are complete.

## Open validation

- Document your own real cases; no invented interview or client data.
- Coach and athlete interviews and the time measurement of at least 5 complete manual adjustments.
- Actually trying Kaizer and one more alternative.
- Evidence for the demand, time-cost and differentiation gate.
- Whether coaches actually lose track of athlete history (the memory hypothesis), asked in the same interviews.

## Next technical work packages

1. Trying the MCP server in a real AI client with synthetic data and tuning the memory rules (guide: [mcp-trial.md](mcp-trial.md)).
2. Versioned prescriptions, so load and exercise swaps can use the same approval flow.
3. Adding or removing sessions inside a proposal.
4. Repeating the concurrency check after larger data-model changes.

## Not done yet

Athlete self-service login; approved CSV import and column mapping; private Google Sheets connection; correction workflow for past logs; full offline operation; load/exercise changes; prescription versioning; in-app AI chat and AI-assisted plan proposals; billing; public deployment; scheduled and off-machine backups; load testing beyond the single-machine concurrency check; a complete data-handling process.

The current UI is built for coaches: the coach records the athlete's data. The app does not change loads automatically and gives no injury-management advice. It is not yet suitable for running a live service with real athlete data.
