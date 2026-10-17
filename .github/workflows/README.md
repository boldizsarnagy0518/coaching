# Automated checks

[Project overview](../../README.md) · Updated: 17 October 2026

## Responsibility

The [tests.yml](tests.yml) GitHub Actions workflow checks the project on push and pull request events.

## Current state

Ubuntu runner, Python 3.12, pinned uv 0.8.14. The workflow installs from the lockfile and runs the Django system check, the missing-migration check and the tests. Its GitHub permission is `contents: read` only; there is no deployment step.

**Evidence:** the latest local run passed all tests (the current count is in the [training README](../../training/README.md)) and the Django check reported no issues. The result of the workflow on GitHub has to be checked separately; the existence of the configuration and a local success do not prove a remote CI success.

**Not done:** browser E2E tests, tests on PostgreSQL and on multiple Python versions, load testing, automatic deployment.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Install from the lockfile | Dependencies must not change unnoticed | Dependency updates change the lockfile and tests together |
| A missing migration is a failure | A model change must not be pushed without a schema update | The correctness of data-preserving migrations needs separate review |
| Functional and permission tests | The real workflow and data isolation are the first risks | They do not prove full security |
| No automatic deployment | The prototype is not prepared for production | A push does not publish a web application |

## Verification

The root [README](../../README.md) lists the local commands. Remote result: the run for the given commit on the repository's Actions page. Never treat a failed check as passing because of an earlier green run.

## Next step

With plan versioning: regression tests that past performance is kept and stale approvals are rejected. When PostgreSQL is introduced, tests must run on it too.
