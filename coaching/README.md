# Alkalmazáskonfiguráció és belépés

[Projektáttekintés](../README.md) · Frissítve: 2026. október 17.

## Felelősség

A Django-projekt összeállítása: adatbázis, munkamenetek, bejelentkezés, útvonalak, sablonok és helyi beállítások. Az edzési adatok és azok hozzáférési szűrése a [training modulban](../training/README.md) vannak.

## Aktuális állapot

- A [settings.py](settings.py) a [configuration.py](configuration.py) beállításait tölti be.
- SQLite-adatbázis a projekt gyökerében; magyar nyelv, Europe/Budapest időzóna.
- Django-bejelentkezés és POST-alapú kijelentkezés; munkamenet- és CSRF-kezelés.
- A [urls.py](urls.py) kapcsolja össze a belépést, az adminfelületet és az edzésmodult.
- Alapesetben helyi fejlesztői mód, csak localhost hosztnevekkel. A titkos kulcs környezeti változóból vagy helyi, Gitből kizárt fájlból jön.

**Nincs kész:** éles telepítési konfiguráció, sportolói szerepkör, önkiszolgáló regisztráció és jelszó-visszaállítás. A README-ben használt `createsuperuser` rendszergazdai jogot is ad; ez fejlesztői kényelmi megoldás, nem a későbbi ügyfélfiók-létrehozás.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Egy Django-alkalmazás | A Python-központú mellékprojektben együtt ad adatkezelést, űrlapot és hitelesítést | Most nincs külön frontend- vagy API-szolgáltatás |
| SQLite helyben | Külső adatbázis nélkül kipróbálható az első folyamat | PostgreSQL és annak párhuzamos írási viselkedése még nincs ellenőrizve |
| Django beépített hitelesítése | Nem kell saját jelszó- és munkamenetkezelőt írni | Az erőforrásokhoz való hozzáférést ettől még külön szűrjük |
| Helyileg generált titkos kulcs | Nincs közösen használt, repóba írt fejlesztői titok | A `.local/` tartalma nem tölthető fel |
| Éles módhoz kötelező környezeti kulcs | Hiányzó titokkal ne induljon el élesnek szánt konfiguráció | A kapcsoló önmagában nem teszi éles használatra alkalmassá a rendszert |

## Ellenőrzés

A projekt gyökeréből: `uv run python manage.py check`. A belépéshez kötött nézeteket és a CSRF-védelmet a [tesztek](../training/tests.py) ellenőrzik. A helyi bejelentkezési oldal HTTP-válasza ellenőrizve; teljes böngészős használhatósági vizsgálat még nincs dokumentálva.

## Következő lépés

A sportolói hozzáférés előtt külön szerep- és jogosultságmodell kell. Külső telepítés előtt külön konfiguráció, mentés-visszaállítás, titokkezelés és üzemeltetési felülvizsgálat szükséges.
