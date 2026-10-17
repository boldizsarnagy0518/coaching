"""Read-only CSV preparation. Downloading or previewing never writes training data."""
import csv
import io
import re
from urllib.error import URLError
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

MAX_BYTES = 1_000_000
MAX_ROWS = 2000
MAX_COLUMNS = 50


def safe_cell(value):
    text = "" if value is None else str(value)
    # Spreadsheet programs must not execute user-entered exercise/plan names.
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) or text.startswith(("\t", "\r", "\n")) else text


def read_csv(data):
    if len(data) > MAX_BYTES:
        raise ValueError("Legfeljebb 1 MB méretű CSV tölthető be.")
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("UTF-8 kódolású CSV szükséges.") from exc
    if "\x00" in text or text.lstrip().lower().startswith(("<!doctype", "<html")):
        raise ValueError("A forrás nem CSV-adat, hanem hibás fájl vagy bejelentkezési oldal.")
    try:
        dialect = csv.Sniffer().sniff(text[:8192], delimiters=",;\t")
        rows = list(csv.reader(io.StringIO(text), dialect, strict=True))
    except csv.Error as exc:
        raise ValueError("A CSV elválasztója vagy idézőjelezése nem értelmezhető.") from exc
    rows = [row for row in rows if any(cell.strip() for cell in row)]
    if len(rows) < 2:
        raise ValueError("Fejléc és legalább egy adatsor szükséges.")
    header = [cell.strip() for cell in rows[0]]
    if not all(header) or len(set(header)) != len(header):
        raise ValueError("Minden oszlopnak külön, nem üres fejléc kell.")
    if len(header) > MAX_COLUMNS or len(rows) - 1 > MAX_ROWS:
        raise ValueError("Legfeljebb 50 oszlop és 2000 adatsor olvasható be.")
    if any(len(row) != len(header) for row in rows[1:]):
        raise ValueError("Az adatsorok oszlopszáma nem egyezik a fejléccel.")
    return {"headers": header, "rows": rows[1:21], "row_count": len(rows) - 1}


def published_sheet_url(value):
    """Accept only published Google Sheets CSV URLs; never arbitrary fetch URLs."""
    url = urlsplit(value)
    if url.scheme != "https" or url.netloc != "docs.google.com" or not re.fullmatch(r"/spreadsheets/d/e/[A-Za-z0-9_-]+/pub", url.path):
        raise ValueError("Publikált Google Sheets CSV-link szükséges (docs.google.com/spreadsheets/d/e/…/pub). Privát táblázathoz most CSV-feltöltést használj.")
    query = parse_qs(url.query)
    if query.get("output") != ["csv"]:
        raise ValueError("CSV-formátumú publikált link szükséges: output=csv.")
    gid = query.get("gid", [None])[0]
    if gid is not None and not gid.isdigit():
        raise ValueError("Érvénytelen munkalapazonosító.")
    params = {"output": "csv"}
    if gid is not None:
        params.update(gid=gid, single="true")
    return "https://docs.google.com" + url.path + "?" + urlencode(params)


class GoogleRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target = urlsplit(newurl)
        host = target.hostname or ""
        if target.scheme != "https" or target.username or target.password or target.port not in (None, 443) or not (
            host == "docs.google.com" or host.endswith(".googleusercontent.com")
        ):
            raise ValueError("A letöltés nem engedélyezett címre irányított át.")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def download_sheet(url):
    source = published_sheet_url(url)
    try:
        with build_opener(GoogleRedirects()).open(Request(source, headers={"Accept": "text/csv"}), timeout=10) as response:
            data = response.read(MAX_BYTES + 1)
    except (URLError, TimeoutError, OSError) as exc:
        raise ValueError("A Google-táblázat nem tölthető le. Ellenőrizd a hozzáférést, vagy tölts fel CSV-t.") from exc
    return read_csv(data)
