# Automatikus ellenőrzés

[Projektáttekintés](../../README.md) · Frissítve: 2026. október 17.

## Felelősség

A [tests.yml](tests.yml) GitHub Actions-folyamat push és pull request eseményre ellenőrzi a projektet.

## Aktuális állapot

Ubuntu futtatókörnyezet, Python 3.12, rögzített uv 0.8.14. A folyamat a lockfájlból telepít, futtatja a Django rendszerellenőrzést, a hiányzó migráció ellenőrzését és a teszteket. GitHub-jogosultsága csak `contents: read`; nincs telepítési lépés.

**Bizonyíték:** a legutóbbi helyi futtatásban 26 teszt sikeres, a Django-ellenőrzés hibamentes. Az adatátadás nem módosította az adatmodellt. A GitHubon futó konkrét munkafolyamat eredményét külön kell ellenőrizni; a konfiguráció megléte és a helyi siker nem bizonyít távoli CI-sikert.

**Nincs kész:** böngészős E2E-teszt, PostgreSQL-es és több Python-verziós teszt, terhelésmérés, automatikus telepítés.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Lockfájlból telepítés | A függőségek ne változzanak észrevétlenül | Függőségfrissítéskor a lockfájl és a teszt együtt változik |
| Hiányzó migráció hibának számít | Ne kerüljön fel sémafrissítés nélkül modellváltozás | Az adatmegőrző migráció helyességét külön is vizsgálni kell |
| Funkcionális és jogosultsági tesztek | A tényleges munkafolyamat és adatelkülönítés az első kockázat | A teljes biztonságot nem igazolják |
| Nincs automatikus telepítés | A prototípus éles működésre még nincs előkészítve | A push nem publikál webalkalmazást |

## Ellenőrzés

A gyökér [README](../../README.md) tartalmazza a helyi parancsokat. Távoli eredmény: a repó Actions oldalán az adott commit futása. Sikertelen ellenőrzést ne minősíts sikeresnek egy korábbi zöld futás alapján.

## Következő lépés

Tervverziózáskor regressziós teszt a múltbeli teljesítés megőrzésére és az elavult jóváhagyás elutasítására. PostgreSQL bevezetésekor azon is szükséges tesztelni.
