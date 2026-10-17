# Sportolók, tervek és edzésnapló

[Projektáttekintés](../README.md) · Frissítve: 2026. október 17.

## Felelősség

A sportoló → terv → edzés → előírt sorozat → tényleges teljesítés folyamat. Jelenleg az edző rögzíti az adatokat; a sportolónak nincs saját fiókja.

## Aktuális állapot

| Alrész | Működik | Még hiányzik |
|---|---|---|
| Sportoló | Név, edzőhöz rendelés, saját lista | Részletes profil, sportolói belépés |
| Terv és edzés | Tervcím, edzésnév és tervezett dátum | Tervverzió, kimaradás és áthelyezés |
| Előírt sorozat | Szabad szöveges gyakorlatváltozat, ismétlés, kg | Gyakorlatkatalógus, csere és cél-RPE |
| Tényleges teljesítés | Ismétlés, kg, opcionális RPE, rögzítési idő | Utólagos javítás, külön tényleges edzésidőpont |
| Beküldés | Ismételt azonos kérés nem dupláz; ütközéskor 409 | Naplókorrekciós munkafolyamat |
| Hozzáférés | Minden alkalmazásnézet szűr a bejelentkezett edzőre | Megosztott coaching, sportolói szerep |

Fő fájlok: [models.py](models.py) az adatok, [forms.py](forms.py) a bevitel, [views.py](views.py) a folyamat és jogosultság, [urls.py](urls.py) az útvonalak, [tests.py](tests.py) az ellenőrzések.

## Adatkapcsolatok

`User → Athlete → TrainingPlan → TrainingSession → PlannedSet → SetLog`

Egy előírt sorozathoz legfeljebb egy teljesítés kapcsolható. Az előírt és a tényleges értékek külön mezőkben, külön rekordban vannak. A napló létrehozása nem módosítja az előírást. Ez **nem** teljes auditnapló vagy változtathatatlan tervtörténet: ezek még nincsenek megvalósítva.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Előírás és teljesítés szétválasztása | Összehasonlítható marad, mit kért az edző és mi történt | Tervmódosításhoz később verziókapcsolat kell |
| Egy naplórekord sorozatonként | Egyértelmű első naplózási modell és adatbázisban kikényszeríthető korlát | Extra próbálkozás és javítás még nem kezelhető külön eseményként |
| Egyedi beküldési UUID | Hálózati újraküldés ne hozzon létre új teljesítést | Azonos UUID és azonos adat ismétlése elfogadott; más tartalom ütközés |
| Adatbázis-tranzakció és egyediségi korlát | A duplázást ne csak a felület előzze meg | A párhuzamos kérések terheléses vizsgálata még hiányzik |
| Edzői szűrés szerveroldalon | A kliens által küldött sportolóazonosító nem jogosultság | Minden új olvasó/író nézetnél ugyanez szükséges |
| Tényleges ismétlés lehet nulla, RPE elhagyható | Sikertelen sorozat és hiányzó becslés is rögzíthető | A naplózott sorozat nem feltétlenül sikeresen teljesített sorozat |
| Súly decimális kg-ban | Az előírás és teljesítés pontosan összevethető | Font és mértékegységváltás nincs |
| Kapcsolatoknál `PROTECT` | Ne lehessen véletlenül láncoltan törölni az előzményeket | A végleges adatvédelmi törlési folyamat külön fejlesztés |

Az 1–100 célismétlés, 0–100 tényleges ismétlés és 1–10 RPE **beviteli korlát**, nem szakmai terhelésajánlás. A formai érvényesség nem bizonyítja egy edzésterv megfelelőségét.

## Ellenőrzés

`uv run python manage.py test training` a projekt gyökeréből. A modul két tesztfájlja összesen 26 tesztet tartalmaz:

- [tests.py](tests.py), 14 teszt: a teljes létrehozási út, az idegen edző hozzáférésének tiltása, az újraküldés, az ütközések, hibás értékek, opcionális RPE, részleges naplózás, CSRF, HTML-escaping és a demóadat ismételhetősége.
- [test_transfers.py](test_transfers.py), 12 teszt: CSV-export és -előnézet, URL- és átirányítás-korlátozás, hozzáférés, valamint az, hogy az előnézet oldal első megnyitásakor nem jelenik meg hibaüzenet.

Utolsó helyi eredmény: 26/26 sikeres.

## Következő lépés

Új alrész: [CSV és Google Sheets](../docs/data-transfer/README.md). A `transfers.py` közös CSV-olvasót és korlátozott online letöltést ad; a nézetek saját sportolóhoz kötött exportot és csak olvasható előnézetet biztosítanak. A tesztek száma és eredménye az Ellenőrzés részben szerepel.

Tervverziók, majd strukturált áthelyezési kérés, ellenőrizhető javaslat és edzői jóváhagyás. A mostani modul nem tervez újra, nem hív AI-t és nem ad sérüléskezelési tanácsot.

Kapcsolódó részletek: [adatbázismigrációk](migrations/README.md), [demóadat](management/README.md), [felület](../templates/README.md).
