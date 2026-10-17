# Adatbázisséma és migrációk

[Edzésmodul](../README.md) · Frissítve: 2026. október 17.

## Felelősség

Az adatbázis szerkezetének reprodukálható létrehozása és későbbi módosítása.

## Aktuális állapot

Az [0001_initial.py](0001_initial.py) létrehozza az öt edzési modellt, a kapcsolataikat, az egyediségi és értéktartomány-korlátokat. A bejelentkezési és munkamenet-táblákat a Django saját migrációi hozzák létre.

**Nincs kész:** edzéstervek tartalmi verziózása, PostgreSQL-migrációs próba, üzemeltetési visszaállítási eljárás. Az adatbázisséma verziója nem azonos egy sportoló tervének verziójával.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Migrációs fájlok a repóban | Ugyanaz a séma építhető fel másik gépen és CI-ben | Modellváltozás mellé migráció is kell |
| Adatbáziskorlátok is védik a naplót | Az űrlapon kívüli írás se kerülhesse meg az alapkorlátokat | A szakmai helyességhez további szabályok kellenek |
| A helyi adatbázis nincs Gitben | Ne kerüljenek fel sportolói vagy bejelentkezési adatok | A Git nem adatmentés; a működő adatbázisról külön mentés kell |

## Ellenőrzés és használat

A projekt gyökeréből:

```powershell
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py migrate
uv run python manage.py test training
```

A tesztek külön tesztadatbázist használnak. Az első migráció helyben lefutott; a legutóbbi ellenőrzés nem talált hiányzó migrációt.

## Következő lépés

A tervverziózás új migrációt igényel, a korábbi naplók megőrzésével. Megosztott vagy alkalmazott migrációt utólag ne írjunk át; a következő változást új fájl rögzítse.
