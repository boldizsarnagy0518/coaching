# Állapot, döntések és validáció

[Projektáttekintés](../README.md) · Frissítve: 2026. október 17.

## Felelősség

Elkülöníteni a működő terméket, a tervezett funkciókat és a még nem igazolt üzleti feltételezéseket. A részek README-jei a kód mellett mutatják a helyi állapotot és a döntések indokait.

## Aktuális állapot

| Dokumentum | Szerep |
|---|---|
| [Implementálási állapot](implementation-status.md) | Rövid összesítés arról, mi készült el és mi következik |
| [Validációs munkalap](validation-template.md) | Üres sablon interjúhoz, időméréshez és konkurenspróbához |
| [Aktuális ütemterv](../elso_szakasz_utemterv.md) | 17 munkahét, heti 10 + 2 óra, költözési szünet és kapuk |
| [Kutatás és termékterv](../eroemelo_ai_kutatas_es_terv.md) | Források, alternatívák, árazási és szakmai hipotézisek |

A piaci validáció még nyitott. A kód elkészítése nem helyettesíti az interjúkat, az időmérést vagy a Kaizer tényleges kipróbálását. Az előrehozott műszaki prototípus a felhasználó implementálási kérése alapján készült.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Részenkénti README | A kód megnyitásakor látható legyen, hol tartunk és miért így készült | Minden érintett funkcióváltozáskor karban kell tartani |
| Egy központi mutató | A projekt egésze áttekinthető marad | A részleteket nem másoljuk minden dokumentumba |
| Tény, terv és hipotézis elkülönítése | Ne tűnjön késznek vagy igazoltnak, ami még nincs meg | Az állapot mellé ellenőrzési bizonyíték kell |
| Relatív munkahét | A heti kapacitás és költözési dátum változhat | A naptári határidő külön egyeztetendő |

## Dokumentációs szabály a következő fejlesztésekhez

1. Minden önálló felelősségű új modul kapjon `README.md` fájlt. Üres csomagokhoz vagy minden egyes fájlhoz nem kell külön leírás.
2. Tartalmazza: **felelősség; aktuális állapot; mi hiányzik; döntés, indok és következmény; ellenőrzés; következő lépés; frissítés dátuma**.
3. Az aktuális állapotot a kódhoz igazítva írd át. Korábbi döntés megváltozásakor röviden őrizd meg, mi váltotta fel és miért.
4. A javasolt következő lépést ne írd kész funkcióként. A tesztparancs megléte nem bizonyítja a sikeres futást; jelöld a ténylegesen ellenőrzött eredményt.
5. A részletek elsődleges helye a modul README-je. A gyökérmutatót és az implementálási összesítést csak a projektállapotot érintő változásnál frissítsd.
6. Kód, teszt és a hozzájuk tartozó dokumentáció ugyanabban a változtatásban kerüljön be. Relatív linkeket használj, hogy GitHubon is működjenek.
7. Személyes adatot, jelszót és API-kulcsot ne írj a dokumentációba. Kitöltött, személyes adatot tartalmazó munkalap a Gitből kizárt `private/` mappába kerüljön.

### Új rész README-sablonja

```markdown
# A rész neve

Frissítve: ÉÉÉÉ. HH. NN.

## Felelősség
Melyik feladatot kezeli, és melyik másik részhez kapcsolódik?

## Aktuális állapot
Mi működik ténylegesen? Mi hiányzik vagy korlátozott?

## Döntések és indokok
| Döntés | Miért? | Következmény / korlát |
|---|---|---|

## Ellenőrzés
Parancs, teszt vagy kézi próba; utolsó igazolt eredmény.

## Következő lépés
A következő konkrét munkacsomag és a nyitott döntés.
```

## Ellenőrzés

Dokumentációmódosításnál a leírás és a kód összhangját, a relatív linkek célját és a Git-diffet ellenőrizd. Pusztán szöveges módosítás miatt nem szükséges új alkalmazástesztet írni.

## Következő lépés

A valós validációs adatok összegyűjtése és a kapudöntés rögzítése. A következő implementáció után a tervverziózás döntései és igazolt állapota kerüljön az edzésmodul README-jébe.
