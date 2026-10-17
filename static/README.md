# Megjelenés és reszponzív stílusok

[Felület](../templates/README.md) · Frissítve: 2026. október 17.

## Felelősség

Az [app.css](app.css) adja az alkalmazás színeit, térközeit, kártyáit, űrlapjait és keskeny képernyőre vonatkozó elrendezését.

## Aktuális állapot

Egy közös stíluslap működik: sötét háttér, világos szöveg, zöld kiemelés, rugalmas kártyarács. 600 px alatt a fontos sorok egymás alá rendeződnek. A beviteli mezők és gombok minimum 46 px magasak, a billentyűzetfókusz látható.

**Nincs kész:** világos téma, teljes komponenskönyvtár, mért kontraszt- és akadálymentességi audit, több eszközös vizuális ellenőrzés. A reszponzív CSS megléte nem helyettesíti ezeket.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Egy CSS-fájl, rendszerbetűtípus | Nincs külön frontend build vagy külső fontfüggőség | Növekedéskor érdemes rendezettebb komponensenkénti bontás |
| Közös színváltozók | Egy helyen módosítható az alapmegjelenés | A témaváltás még nincs kialakítva |
| Nagyobb érintési célok és egyoszlopos mobilnézet | Edzés közbeni bevitelhez használható alap | Valódi telefonos teszt még szükséges |
| Kevés vizuális elem | A rögzítés és az előírás–teljesítés összevetése kap hangsúlyt | Elemző grafikonok később kerülhetnek be |

## Ellenőrzés

A stíluslap helyi HTTP-kiszolgálása ellenőrzött. Vizuális módosításkor nézd meg a bejelentkezést, hosszú sportoló-/gyakorlatneveket, űrlaphibákat és sorozatkártyákat keskeny és széles képernyőn. A billentyűzetfókusz is maradjon látható.

## Következő lépés

Első dokumentált mobilos használati és vizuális próba, majd az ott felmerült problémák javítása. A CSS rendezett formázása is elvégezhető egy következő megjelenési munkacsomagban.
