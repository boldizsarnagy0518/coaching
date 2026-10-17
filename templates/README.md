# Felület és űrlapok

[Projektáttekintés](../README.md) · Frissítve: 2026. október 17.

## Felelősség

A Django által kiszolgált HTML-képernyők. A bevitel ellenőrzése és az adatelkülönítés a háttérrendszer feladata; a sablon nem jogosultsági határ.

## Aktuális állapot

| Fájl | Képernyő |
|---|---|
| [base.html](base.html) | Fejléc, kijelentkezés, állapotüzenetek, közös keret |
| [registration/login.html](registration/login.html) | Edzői bejelentkezés |
| [training/dashboard.html](training/dashboard.html) | Saját sportolók és tervszám |
| [training/athlete.html](training/athlete.html) | Egy sportoló tervei |
| [training/plan.html](training/plan.html) | Egy terv edzései |
| [training/session.html](training/session.html) | Előírt és tényleges sorozatok, naplózott darabszám |
| [training/form.html](training/form.html) | Közös adatbeviteli űrlap |

**Nincs kész:** sportolói saját felület, tervkülönbség és jóváhagyási képernyő, utólagos javítás, offline piszkozat. A részleges állapot a naplórekordok számából származik; nem önálló edzésstátusz-modell.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Szerveroldali HTML | A mellékprojekt első adatútjához kevesebb külön technológia kell | Jelenleg minden művelethez szerverkapcsolat szükséges |
| Közös keret és űrlapsablon | Az új képernyők egységesek, kisebb a másolt kód mennyisége | A speciális naplózási élmény későbbi finomítás |
| Előírás és tényleges érték együtt látható | Az eltérés ellenőrizhető | Még nincs trend vagy szakmai kiértékelés |
| Mentés után visszairányítás | A felhasználó a mentett állapotot látja | Az ismételt beküldés védelmét ezen felül a backend adja |
| Sikerüzenet csak mentés/azonos újraküldés után | Hibás adat ne tűnjön sikeresen rögzítettnek | Ütközésnél még egyszerű 409-es szöveges válasz van |

## Ellenőrzés

A [funkcionális tesztek](../training/tests.py) ellenőrzik a válaszokat, a megjelenő mentett állapotot, részleges naplózást és a HTML-escapinget. A bejelentkezési oldal HTTP-n ellenőrzött. Teljes böngészős, mobilos és akadálymentességi teszt nincs igazolva; az előző böngészős próba eszközhibával megszakadt.

## Következő lépés

A [tervverziózás](../docs/implementation-status.md) után előtte/utána nézet és jóváhagyás. Külön használati próba kell annak mérésére, hogy a naplózás telefonon segítség nélkül végigvihető-e. Megjelenési döntések: [static](../static/README.md).
