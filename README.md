# Coaching

Erőemelő edzők tervmódosítási és naplózási munkáját segítő alkalmazás.

## Tervezés

- [Kutatás és termékterv](eroemelo_ai_kutatas_es_terv.md)
- [Aktuális ütemterv](elso_szakasz_utemterv.md): 17 munkahét, heti 10 + 2 óra, külön validációs kapuval.

A kutatási terv korábbi 16 hetes forgatókönyvét az aktuális ütemterv pontosítja. A validációs kapu teljesülése még nincs igazolva; interjúeredményt vagy versenytárstesztet nem helyettesít a megírt kód.

## Adatok

A repóba csak kód, tervezési anyag és szintetikus példa kerülhet. Valós sportolói adatot, interjúalanyok elérhetőségét, adatbázist, jelszót vagy API-kulcsot ne commitolj. A helyi adatfájlok helye a Git által figyelmen kívül hagyott `private/` könyvtár.

## Helyi indítás

Python 3.12+ és `uv` szükséges. A függőségek verzióját az `uv.lock` rögzíti.

```powershell
uv sync --locked
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py seed_demo --username SAJAT_FELHASZNALONEV
uv run python manage.py runserver 127.0.0.1:8765
```

Nyisd meg a http://127.0.0.1:8765 címet, és lépj be az általad létrehozott fiókkal. A demófeltöltés opcionális, csak szintetikus edzést hoz létre. A jelszót a `createsuperuser` interaktívan kéri; nincs beégetett demójelszó. Másik edzői tesztfiók ugyanígy készíthető.

## Ellenőrzés

```powershell
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py test
```

## Jelenlegi funkciók és korlátok

Sportoló → terv → edzés → előírt sorozat → tényleges teljesítés. Az edző csak a saját sportolóit éri el; az előírt és tényleges adatok külön tárolódnak. Az ismételt azonos naplóbeküldés nem dupláz. A felület magyar és telefonra igazított.

Ez helyi, szintetikus adatokkal használható **edzői prototípus**. Még nincs sportolói saját belépés, verziózott újratervezés, CSV-import vagy AI-integráció. A napló utólagos szerkesztése nincs kész; eltérő ismételt beküldésnél a rendszer 409-es ütközést jelez és megőrzi a korábbi adatot.

- [Részletes állapot és következő feladatok](docs/implementation-status.md)
- [Validációs munkalap](docs/validation-template.md)

## Technológiai döntés

Django 5.2 és szerveroldali HTML: egy Python-alkalmazásban ad hitelesítést, űrlapokat, adatkezelést és mobilbarát felületet. A helyi próba SQLite-ot használ; PostgreSQL-re áttérés és az ottani tranzakciós viselkedés ellenőrzése külön lépés. Most nincs külső AI-hívás vagy API-kulcsigény.

A helyi titkos kulcs az első futáskor a kizárt `.local/` mappába kerül. Az adatbázis szintén kizárt. A fejlesztői beállítások csak localhostot fogadnak. Ne tedd a fejlesztői szervert nyilvánossá: külső használat előtt külön telepítési, adatvédelmi és biztonsági munkacsomag szükséges. A `DJANGO_DEBUG=false` beállítás megköveteli a `DJANGO_SECRET_KEY` környezeti változót, de ez önmagában nem kész éles konfiguráció.
