# CSV és Google Sheets adatátadás

[Projektáttekintés](../../README.md) · Frissítve: 2026. október 17.

## Aktuális állapot

| Út | Mi működik? | Határ |
|---|---|---|
| App → CSV | Sportolónként letölthető az előírt és tényleges sorozatok naplója | Üres edzések nem szerepelnek |
| Letöltött Google Sheets CSV → app | Feltöltés, szerkezeti ellenőrzés, első 20 sor előnézete | Nincs oszlop-hozzárendelés vagy jóváhagyott import |
| Publikált Google Sheets → app | Gombnyomásra online CSV-letöltés és ugyanaz az előnézet | Valódi táblázatos próba még nincs; szimulált válasszal tesztelt |
| Privát Google Sheets → app | Következő integrációs irány | Google-hitelesítés még nincs |

## Használat

A sportoló lapján: **Napló letöltése CSV-ben**, illetve **CSV / Google Sheets előnézet**.

Kézi út: Google Sheets → Fájl → Letöltés → vesszővel tagolt értékek (.csv), az aktuális munkalapból. Utána feltöltés az alkalmazásba. A Google-fiókhoz ilyenkor nem kap hozzáférést az alkalmazás.

Online út: már publikált munkalap CSV-linkje, ilyen szerkezettel:

```text
https://docs.google.com/spreadsheets/d/e/PUBLIKALT_AZONOSITO/pub?gid=0&single=true&output=csv
```

Ez mintaszerkezet, nem valódi táblázat. A szokásos `/spreadsheets/d/…/edit` link még nem támogatott. A letöltést az alkalmazást futtató gép végzi; helyi futásnál ez a saját géped. Nincs háttérszinkron vagy visszaírás a Sheetsbe.

**Privát sportolói adatot ne publikálj a csatlakozás miatt.** A publikálás szélesebb körnek adhat hozzáférést. Privát táblázathoz most a kézi CSV-út használható. [Google publikálási útmutató](https://support.google.com/docs/answer/183965).

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Közös CSV-olvasó mindkét forráshoz | A formátumellenőrzés ugyanaz legyen | A privát kapcsolat később ugyanide csatlakozhat |
| Csak előnézet, nincs automatikus import | Az edzői táblázatok eltérő elrendezésűek | Oszlop-hozzárendelés és jóváhagyás a következő lépés |
| Csak meghatározott Google URL-ek és átirányítások | Ne lehessen tetszőleges internetes vagy helyi címet lekérni | Privát és sima megosztási linket elutasítunk |
| 1 MB, 2000 sor, 50 oszlop | Korlátozott erőforrás-használat a prototípusban | Nagy táblázatot szűkíteni kell |
| UTF-8, opcionális BOM; vessző, pontosvessző vagy tab | Google-export és gyakori CSV-változatok kezelése | Excel-munkafüzet és összevont cellák értelmezése nincs |
| Exportban képletvédelem | A felhasználói név/gyakorlat ne fusson képletként | Veszélyes kezdőkarakter elé aposztróf kerül; nem veszteségmentes adatbázismentés |

Az előnézet egyedi, nem üres fejlécet és azonos oszlopszámú sorokat vár. Nem értelmezi a képletek, színek vagy edzői elrendezések jelentését. Nem ment edzési rekordot, fájlt vagy forráslinket az alkalmazás adatbázisába; a keretrendszer átmeneti feltöltési kezelése ettől külön működik. A válasz `no-store` fejlécet kap.

Exportoszlopok: `plan`, `session`, `scheduled_date`, `exercise`, `planned_reps`, `planned_weight_kg`, `actual_reps`, `actual_weight_kg`, `rpe`, `recorded_at`. A számok tizedesponttal, a súlyok kg-ban szerepelnek; a táblázatkezelő területi beállítása számít. A dátum tervezett nap, a rögzítési idő nem az edzés tényleges kezdete. Nem naplózott sorozatnál a teljesítés üres, nulla ismétlésnél nulla.

## Ellenőrzés

`uv run python manage.py test`: 25 sikeres helyi teszt. Az új ellenőrzések: export, hozzáférés, fájlelőnézet, hibás CSV, elválasztók, méretkorlát, képletvédelem, URL- és átirányítás-korlátozás, szimulált online válasz. Élő Google-táblázatos próba még szükséges.

Kód: [transfers.py](../../training/transfers.py), [nézetek](../../training/views.py), [tesztek](../../training/test_transfers.py).

## Következő lépés

1. Anonimizált edzői minták alapján oszlop-hozzárendelés.
2. Ellenőrzés és jóváhagyás utáni import, ismételt import elleni védelemmel.
3. Privát Google-kapcsolat: felhasználói engedélyezés, csak olvasási hozzáférés, munkalapválasztás és visszavonás.
4. Később időzített frissítés, változásfelismeréssel és konfliktuskezeléssel.
