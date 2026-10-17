# CSV and Google Sheets data transfer

[Project overview](../../README.md) · Updated: 17 October 2026

## Current state

| Path | What works? | Limit |
|---|---|---|
| App → CSV | Per-athlete download of the prescribed and actual set log | Sessions without sets are not included |
| Downloaded Google Sheets CSV → app | Upload, structural validation, preview of the first 20 rows | No column mapping or approved import |
| Published Google Sheets → app | On-demand online CSV download and the same preview | No real spreadsheet trial yet; tested with a simulated response |
| Private Google Sheets → app | Next integration direction | No Google authentication yet |

## Usage

On the athlete page: **Napló letöltése CSV-ben** (download log as CSV) and **CSV / Google Sheets előnézet** (preview).

Manual path: Google Sheets → File → Download → Comma-separated values (.csv), from the current sheet. Then upload it into the app. The app gets no access to the Google account this way.

Online path: the CSV link of an already published sheet, in this form:

```text
https://docs.google.com/spreadsheets/d/e/PUBLISHED_ID/pub?gid=0&single=true&output=csv
```

This is an example structure, not a real spreadsheet. The usual `/spreadsheets/d/…/edit` link is not supported yet. The download is performed by the machine running the app; when running locally, that is your own computer. There is no background sync and no write-back to Sheets.

**Do not publish private athlete data just to connect it.** Publishing can give a wider audience access. For a private sheet, use the manual CSV path for now. [Google publishing guide](https://support.google.com/docs/answer/183965).

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| One shared CSV reader for both sources | Format validation should be identical | A private connection can later plug into the same reader |
| Preview only, no automatic import | Coaches' spreadsheets have different layouts | Column mapping and approval are the next step |
| Only specific Google URLs and redirects | Arbitrary internet or local addresses must not be fetchable | Private and plain sharing links are rejected |
| 1 MB, 2,000 rows, 50 columns | Bounded resource use in the prototype | Large sheets must be narrowed down |
| UTF-8 with optional BOM; comma, semicolon or tab | Handles Google exports and common CSV variants | Excel workbooks and merged cells are not interpreted |
| Formula protection in exports | User-entered names/exercises must not run as formulas | Dangerous leading characters get an apostrophe prefix; not a lossless database backup |
| The form is bound only on POST | Opening the page must not show validation errors before submission | Regression test covers the first GET |

The preview expects unique, non-empty headers and rows with the same number of columns. It does not interpret the meaning of formulas, colours or coach-specific layouts. It does not save training records, files or source links into the app database; the framework's temporary upload handling works independently of this. The response gets a `no-store` header.

Export columns: `plan`, `session`, `scheduled_date`, `exercise`, `planned_reps`, `planned_weight_kg`, `actual_reps`, `actual_weight_kg`, `rpe`, `recorded_at`. Numbers use a decimal point and weights are in kg; the spreadsheet's locale settings matter. The date is the scheduled day; the recording time is not the actual start of the session. For sets that were not logged, the actual values are empty; zero reps are written as zero.

## Verification

`uv run python manage.py test`: the data-transfer checks cover export, access control, file preview, malformed CSV, delimiters, size limit, formula protection, URL and redirect restrictions, a simulated online response and an error-free first page load. The current total test count is recorded in the [training README](../../training/README.md). A trial with a live Google spreadsheet is still needed.

Code: [transfers.py](../../training/transfers.py), [views](../../training/views.py), [tests](../../training/test_transfers.py).

## Next step

1. Column mapping based on anonymised coach samples.
2. Import after validation and approval, with protection against repeated imports.
3. Private Google connection: user authorisation, read-only access, sheet selection and revocation.
4. Later: scheduled refresh with change detection and conflict handling.
