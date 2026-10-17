# Management commands and demo data

[Training module](../README.md) · Updated: 17 October 2026

## Responsibility

Manually started, reproducible helper operations. Currently there is a single command: [seed_demo](commands/seed_demo.py).

## Current state

For an existing user, it creates one synthetic athlete, one plan, two sessions (today and in three days) with three prescribed sets each, and two memory entries (one active coach entry, one pending AI proposal). It does not create users, does not change passwords and does not log performance. It reports an error if the user does not exist. A demo login can be created with `create_demo_coach` from the [operations module](../../ops/README.md).

```powershell
uv run python manage.py seed_demo --username YOUR_USERNAME
```

Run the command from the project root. The session dates are relative to the current date of the machine running it.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Synthetic data only | The data flow can be demonstrated without real client data | The example weights are not personalised training advice |
| Existing account required | Loading test data must not change authentication | The account has to be created separately |
| Reuse existing demo items | Running it again must not duplicate the example | Matching is by name/title; renamed data can lead to a new example |
| Sets are only created for a new session | Re-running must not overwrite a demo already in use | Not a general repair or reset command |
| One transaction | A failed run must not leave half-created data | Does not replace an operational backup |
| English, ASCII-only output | A cp1252 console crashed on Hungarian letters and rolled the run back | Demo data itself stays Hungarian |

## Verification

The `test_seed_demo_is_repeatable_and_scoped_to_user` test runs the command repeatedly and checks that it creates data scoped to the given coach. Full suite: `uv run python manage.py test training`.

## Next step

Named synthetic datasets can be added for new test scenarios. There is no CSV import, export or data repair command yet.
