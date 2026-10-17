# Erőemelő AI-alkalmazás – az első szakasz ütemterve (mellékprojekt)

Készült: 2026. október 17. **Verzió: 2.0** – mellékprojekt-tempóra és a dublini költözésre átdolgozva.

Kapcsolódó dokumentum: [Kutatás és megvalósítási terv](eroemelo_ai_kutatas_es_terv.md), különösen a 3.4., 4.1. és a 12–16. fejezet.

**Mi változott az 1.0-hoz képest?** A heti 25 óra helyett heti 10 + 2 órával tervez. Az interjúk és a kézi próbák a költözés elé kerültek. A 2. heti kapu helyére egy olyan validációs kapu lépett, amely a Kaizer kipróbálását és a kézi módosítás mért idejét is vizsgálja. A fejlesztési szakasz 3 hétről (kb. 60 óra) 8 hétre (kb. 80 óra) bővült, az AI-rész pedig külön szakaszba került. Az első belső próba így a 8. hét helyett a 17. munkahéten várható.

## 1. Cél és tervezési feltételezések

**Az első szakasz végén elérendő eredmény:** belső használatra alkalmas prototípus. Tárolja a meglévő tervet és a tényleges edzésnaplót, és egy kimaradt vagy áthelyezett edzésre ellenőrizhető módosítást javasol. Az edző a változtatást elfogadhatja vagy elutasíthatja; a sportoló a jóváhagyott tervet látja. Emellett legyen dokumentált külső érdeklődés, mért kézi módosítási idő, versenytársteszt és teszteset-készlet.

A fizetős külső pilot ezen a szakaszon kívül esik. A szakasz eredménye nem kész nyilvános szolgáltatás.

### Kapacitás

- Egy fejlesztővel, a te edzői közreműködéseddel számolunk; a projekt mellékprojekt.
- Heti **10 óra konkrét feladat + 2 óra tartalék**, összesen legfeljebb 12 óra.
- 17 munkahét: **170 óra tervezett feladat + 34 óra tartalék ≈ 204 óra**.
- A fő terv 240–400 órás becsléséből ez a belső próbáig tartó rész. A külső pilot előkészítése és lebonyolítása ezután további munka.
- Az interjúalanyok ideje nincs a fejlesztői órákba számolva; a szervezés és a részvételed igen.
- A technikai jártasságod, különösen a frontend és a hitelesítés terén, még nem ismert. Ezért a fejlesztési órák becslése a legbizonytalanabb rész.

| Tényleges heti kapacitás | A 204 órás keret naptári megfelelője, költözési szünet nélkül |
|---|---|
| 12 óra | 17 hét |
| 8 óra | Körülbelül 26 hét |
| 20 óra | Körülbelül 10 hét |

Kisebb kapacitásnál ugyanazokat a munkacsomagokat oszd több hétre, de a sorrendet tartsd meg. A tartalékot hibákra, tanulásra és csúszásra tartsd fenn; ne töltsd fel előre új funkciókkal.

### A költözés kezelése

A költözés pontos ideje még nincs rögzítve, ezért relatív hetekkel számolok.

- **A szakasz (1–5. hét) a költözés előtt, Magyarországon legyen.** Ide tartoznak a személyes interjúk, az időmérés, a kézi próbák és a saját sportolóiddal végzett egyeztetés. **Legkésőbb a validációs kapu (3. hét vége) teljesüljön a költözés előtt.** Ha ez nem fér bele, a 4–5. hét feladatai távolról is elvégezhetők.
- **A költözés körül 2–4 hét szünetet tervezz**, munkaórák nélkül. Ha ekkor is haladsz, az ajándék, nem elvárás.
- **A B és C szakasz (6–17. hét) helytől független.** A sportolói és edzői próbák ekkor már távolról, videóhívással vagy rövid használati teszttel zajlanak.
- **Indulás:** a 0. hét legalább 7 héttel a költözés előtt kezdődjön, hogy az A szakasz és egy hét ráhagyás beleférjen.

## 2. Áttekintő ütemezés

| Hét | Szakasz | Fókusz | Heti kézzelfogható eredmény |
|---|---|---|---|
| 0. | Előkészítés | Megkeresés | Legalább 8 edzői és 6 sportolói megkeresés, időpontok |
| 1. | A – Validáció (Magyarországon) | Probléma | Termékleírás, 10 saját eset, első 3 edzői interjú |
| 2. | A | Időmérés | További interjúk, legalább 5 mért kézi módosítás |
| 3. | A | Versenytárs és kapu | Kaizer és egy további alternatíva tesztje, **validációs kapu** |
| 4. | A | Szakmai logika | Szabálykatalógus, 20 részletes eset |
| 5. | A | Kézi folyamat | 5 eset kézi végigjátszása, külső véleményezés, adatséma-vázlat |
| — | Költözés | Szünet | 2–4 hét, tervezett munka nélkül |
| 6. | B – Technikai alap | Technikai próba | Egy sportoló teljes adatútja, **technikai kapu** |
| 7–8. | B | Adatbázis és hozzáférés | Tervverziók, edző–sportoló jogosultság |
| 9–10. | B | Naplózás és import | Mobilos napló, CSV-import/export, részleges edzés |
| 11. | B | Használati próba | Két távoli használati próba, hibajavítás, 30 eset |
| 12–14. | B | Tervmódosítás | Szabályalapú javaslat, előtte/utána nézet, jóváhagyás |
| 15–16. | C – AI és belső próba | Korlátozott AI | Szabad szöveges kérés strukturálása, két edzői próba |
| 17. | C | Lezárás | Hibajavítás, 50 eset, **belső próba kapu**, újrabecslés |

**A sorrend indoka:** először azt ellenőrizzük, hogy a módosítási folyamat értékes és időigényes-e, és hogy a legközelebbi konkurens nem oldja-e már meg. Utána rögzítjük a szakmai szabályokat és az adatokat. Az AI a már ellenőrizhető folyamatba kapcsolódik be. Így külön látható, hogy egy hiba adatkezelésből, szabályból vagy nyelvi értelmezésből ered.

## 3. Heti feladatok és elfogadási feltételek

### 0. hét – Megkeresés (kb. 3 óra, a keretbe nem számítva)

Írj legalább 8 edzőnek és 6 sportolónak, rögzített időpontkéréssel. Ne csak saját ügyfeleket keress meg: legalább 4 edző legyen tőled független. A kiinduló lista lehet a fő terv 4.2. fejezetében leírt saját edzői táblázat első sora.

### A szakasz – Validáció a költözés előtt

#### 1. hét – A probléma pontosítása

| Feladat | Tervezett idő |
|---|---|
| Egyoldalas termékleírás: célcsoport, változási helyzet, elvárt eredmény | 2 óra |
| Interjúvázlat, jegyzet- és időmérési sablon | 2 óra |
| 10 saját, személyazonosításra nem alkalmas eset leírása | 3 óra |
| Első 3 edzői interjú, közvetlen jegyzetekkel | 3 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**Elkészül:** termékleírás, 10 eset (eredeti terv, mi változott, milyen döntést hoztál, miért), 3 interjújegyzet.

**A hét akkor kész, ha:** meg tudod nevezni az első támogatott helyzetet, például „kimaradt egy edzés, és más napokon tud edzeni a sportoló”. A problémát legalább egy külső edző saját történetében is felismered.

#### 2. hét – Interjúk és időmérés

| Feladat | Tervezett idő |
|---|---|
| További 3 edzői és 3 sportolói interjú | 6 óra |
| Legalább 5 kézi tervmódosítás teljes idejének mérése (saját és külső edzőknél) | 3 óra |
| Visszatérő problémák és ellenérvek összesítése | 1 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**Az időmérés módja:** a módosítási igény megnyitásától a sportolónak kiadható, ellenőrzött tervig tart. Beleszámít a visszakeresés, az ellenőrzés és a sportoló tájékoztatása is. Minden esetnél rögzítsd az edzőt, a helyzettípust, a percet és azt, hogy havonta nagyjából hányszor fordul elő ilyen eset.

**Elkészül:** 6 edzői és 3 sportolói interjú összesítése; legalább 5 mért kézi módosítás.

#### 3. hét – Versenytársteszt és validációs kapu

| Feladat | Tervezett idő |
|---|---|
| A Kaizer kipróbálása 3 azonos erőemelő esettel | 3 óra |
| Egy további alternatíva (pl. RTS Training Lab vagy a jelenlegi táblázatos módszer) ugyanazon eseteken | 2 óra |
| Egyszerű bemutató egy régi és egy módosított tervvel | 2 óra |
| Pilotajánlat-vázlat és konkrét következő próba felajánlása | 2 óra |
| Döntési jegyzet a kapuhoz | 1 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**A versenytársteszt esetei:** (1) kimaradt edzés, és a sportoló más napon tud edzeni; (2) részben elvégzett edzés; (3) versenyfogás-változat cseréje, például szünetes helyett érintéses fekvenyomás. A 3.3. fejezet értékelési lapját használd. Ha egy terméket nem tudsz ténylegesen használni, ezt jelöld; a dokumentáció olvasása nem használati teszt.

**Validációs kapu – mindhárom feltételnek teljesülnie kell** (saját célküszöb, a mérés után finomítható):

1. **Kereslet:** legalább 2 egymástól független külső edző mutat hasonló problémát, és vállal konkrét következő próbát.
2. **Időigény:** a mért kézi módosítások mediánja **legalább 10 perc**, és az érintett edzőknél ilyen eset **havonta legalább 5-ször** fordul elő. Indoklás: havi 5 × 10 perc = 50 perc, ennek 30%-a 15 perc. Ennél kisebb időnyereségért nehéz havidíjat kérni.
3. **Megkülönböztetés:** a Kaizer (vagy a másik alternatíva) a három esetből legalább egyet láthatóan rosszabbul kezel, mint a tervezett folyamat. Ilyen lehet a változatok összekeverése, duplázás, nem átlátható változtatás vagy a terv hiányzó edzői kontrollja. Ezt egy mondatban le is tudod írni.

**Ha a kapu nem teljesül:**

| Hiányzó feltétel | Teendő |
|---|---|
| Kereslet | A 4. hét egy részében új problémafeltárás; ne kezdj fejlesztést |
| Időigény | Fordulj a heti edzői összefoglaló felé (fő terv 5.1.), vagy maradjon saját belső eszköz |
| Megkülönböztetés | Szűkíts egy olyan erőemelő-specifikus helyzetre, amelyet a konkurens rosszul kezel; ha ilyen nincs, a külső termék irányát állítsd le |

A kapu teljesülése engedély a további kísérletre, nem a piaci siker igazolása.

#### 4. hét – Edzői szabályok

| Feladat | Tervezett idő |
|---|---|
| Döntési szabályok és tiltott automatikus műveletek leírása | 6 óra |
| Az esetkészlet bővítése 20 részletes példára | 4 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**Minden szabályhoz kell:** kiváltó esemény, szükséges adat, engedett változtatás, tiltás, tisztázó kérdés és jóváhagyó szerep. Például a részben elvégzett edzésnél a teljesített sorozatok nem helyezhetők át újra elvégzendő munkaként. Különítsd el a közös korlátot és az edző személyes módszertani preferenciáját.

#### 5. hét – Kézi folyamat és átadás a költözés előtt

| Feladat | Tervezett idő |
|---|---|
| Legalább 5 eset kézi végigjátszása a javasolt folyamattal | 4 óra |
| Külső edzői véleményezés és eltérések rögzítése | 2 óra |
| Adatséma- és szerepkör-vázlat | 2 óra |
| Költözés előtti lezárás: elérhetőségek, távoli próbákra vállalt résztvevők | 2 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**A hét akkor kész, ha:** öt különböző esetben végig tudod vezetni a változtatást, és meg tudod mondani, melyik lépés automatizálható. Van legalább 2 edző és 2 sportoló, aki vállalja a későbbi távoli használati próbát. A hiányzó adat vagy panaszjelzés felismerése is helyes eredmény lehet; nem minden kérésnek kell új tervvel végződnie.

### Költözési szünet (2–4 hét)

Nincs tervezett munka. Ha mégis jut idő, csak olyat csinálj, amit a későbbi döntések nem tesznek feleslegessé. Ilyen például a választott technológia dokumentációjának olvasása vagy egy szintetikus tesztadat-készlet összeállítása.

### B szakasz – Technikai alap

#### 6. hét – Technikai próba

| Feladat | Tervezett idő |
|---|---|
| Legfeljebb 8 órás technikai próba | 8 óra |
| Funkciólista, függőségek és következő feladatok véglegesítése | 2 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**A technikai próba útja:** egy szintetikus sportoló → egy terv → egy naplózott sorozat → adatbázisból visszaolvasott eredmény, telefonról. Egy ismerős Python-megoldást próbálj ki; csak konkrét akadály esetén készíts második változatot.

**Technikai kapu:** megvan a teljes adatút, a támogatott módosítások köre és az elfogadási feltételek. Ha a próba a tartalékkal együtt sem működik, egyszerűsíts felületet vagy technológiát, és **frissítsd a 7–14. hét becslését**, mielőtt továbblépsz.

#### 7–8. hét – Tárolás, tervverziók és hozzáférés

| Feladat | Tervezett idő |
|---|---|
| Adatbázis alapentitásai és reprodukálható módosításai | 6 óra |
| Tervverziók és változási előzmények | 4 óra |
| Belépés és edző–sportoló hozzáférés | 7 óra |
| Jogosultsági és tervtörténeti ellenőrzések | 3 óra |
| **Összesen + tartalék (két hét)** | **20 + 4 óra** |

**Elkészül:** edző, sportoló, kapcsolat, gyakorlat, terv és tényleges edzés alapstruktúrája. A terv frissítése új verziót hoz létre; a korábbi teljesítés nem változik meg.

**Akkor kész, ha:** két külön tesztedzővel igazolt, hogy nem olvassák és nem módosítják egymás sportolóit. A háttérrendszer a tiltott kérést is utasítsa el; az eltérő képernyő nem elég. Ez első körös bizonyíték, nem teljes biztonsági audit. Szintetikus adatokkal dolgozz; az éles személyes adatok használatát a fő terv 11. fejezete szerint külön rendezd.

#### 9–10. hét – Naplózás és tervbevitel

| Feladat | Tervezett idő |
|---|---|
| Telefonra igazított sorozatnaplózás | 8 óra |
| Részleges edzés, újraküldés és mentési állapot kezelése | 4 óra |
| Egy dokumentált CSV-importformátum, előnézettel és exporttal | 4 óra |
| Aktuális terv és tényleges teljesítés megjelenítése | 4 óra |
| **Összesen + tartalék (két hét)** | **20 + 4 óra** |

**Elkészül:** egy program betölthető, egy edzés naplózható, a mentett adatok újranyitáskor visszajönnek. A felület megkülönbözteti a tervezett, elvégzett, kihagyott és részben elvégzett munkát. Az újraküldés nem dupláz sorozatot; sikertelen mentés nem jelenik meg sikeresként.

**Ha csúszik:** először az import kényelmi elemeit egyszerűsítsd. A megbízható mentés és a tényleges edzéstörténet maradjon meg.

#### 11. hét – Távoli használati próba

| Feladat | Tervezett idő |
|---|---|
| Két rövid, távoli használati próba sportolóval (videóhívás, saját telefonján) | 2 óra |
| A talált hibák javítása | 4 óra |
| Az esetkészlet bővítése 30 esetre | 4 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**A hét akkor kész, ha:** a résztvevő folyamatos magyarázat nélkül rögzít egy edzést. A gyorsaságot mérd, de végleges célértéket a próba eredményéből állíts.

**Opcionális, a tartalék terhére:** ismerkedés 1–2 dublini erőemelő edzővel vagy terem közösségével. Ez még nem értékesítés, csak a későbbi angol nyelvű piac első tájékozódása.

#### 12–14. hét – Szabályalapú módosítás és jóváhagyás

| Feladat | Tervezett idő |
|---|---|
| Kimaradás és áthelyezés szabályalapú feldolgozása | 10 óra |
| Javaslat, jóváhagyás és új tervverzió kezelése | 7 óra |
| Előtte/utána nézet és a ténylegesen alkalmazott szabályból készült indoklás | 7 óra |
| Alapfolyamatok, verzióütközés és 5 referenciahelyzet ellenőrzése | 6 óra |
| **Összesen + tartalék (három hét)** | **30 + 6 óra** |

**Elkészül:** strukturált kérésből konkrét, ellenőrizhető javaslat. A jóváhagyás után megjelenik az új terv; elutasításkor a jóváhagyott terv változatlanul elérhető.

**Akkor kész, ha:** legalább öt referenciahelyzet működik; nincs már teljesített sorozat automatikus duplázása; egy időközben megváltozott tervre érkező régi jóváhagyás új ellenőrzést kér. A szakmai korlát megsértése blokkolja a javaslat kiadását.

A 3→4 napos teljes áttervezés és a gyakorlatcsere a következő szakaszra marad.

### C szakasz – Korlátozott AI és belső próba

#### 15–16. hét – AI-értelmezés és edzői próba

| Feladat | Tervezett idő |
|---|---|
| Szabad szöveges kérés strukturálása és rövid magyarázat | 6 óra |
| AI-kimenet ellenőrzése, visszakérdezés és hibakezelés | 6 óra |
| Két felügyelt, távoli edzői használati próba | 4 óra |
| Idő-, költség- és javítási adatok összesítése | 4 óra |
| **Összesen + tartalék (két hét)** | **20 + 4 óra** |

**Elkészül:** például a „péntek helyett vasárnap tudok edzeni” mondatból strukturált kérés lesz. A rendszer a meglévő szabályfolyamatot használja, és megmutatja, hogyan értette a kérést. Bizonytalan dátum vagy hiányzó adat esetén visszakérdez. A modell önmagában nem írhatja át a jóváhagyott tervet.

Az API-integráció előtt legyen szerveroldali titokkezelés, beállított költségkeret és rendezett tesztadat-használat. Ha ezek hiányoznak, a folyamat helyettesítő válaszokkal tesztelhető; az AI-rész ilyenkor még nem tekinthető elkészültnek.

**Az időmérés összevetése:** a két edzői próbában ugyanúgy mérd a módosítás teljes idejét, mint a 2. héten. Ez az első összehasonlítás a kézi alappal. A kis minta miatt jelzésértékű, nem bizonyíték.

#### 17. hét – Lezárás és belső próba kapu

| Feladat | Tervezett idő |
|---|---|
| A legsúlyosabb hibák javítása | 5 óra |
| Az esetkészlet kiegészítése 50 esetre (35 fejlesztési, 15 elkülönített) | 3 óra |
| A következő szakasz újrabecslése és döntési jegyzet | 2 óra |
| **Összesen + tartalék** | **10 + 2 óra** |

**Belső próba kapu:** működik a teljes folyamat; a módosítás teljes ideje rövidebb, mint a 2. heti kézi alap; nincs ismert, nyitott kritikus hozzáférési vagy tiltott módosítási hiba. A kis próba nem igazolja a sportteljesítményre gyakorolt hatást vagy a hosszú távú megtartást.

Ha az AI nem ad érdemi értéket a strukturált űrlaphoz képest, a következő szakaszban a működő naplózást és módosítási folyamatot fejleszd tovább. Az AI minőségjavítása külön feladatként maradjon látható.

## 4. Heti munkaritmus

| Munkablokk | Idő | Tartalom |
|---|---|---|
| Hétindítás | 0,5 óra | Egy heti eredmény, konkrét feladatok és akadályok |
| Két–három fókuszblokk | 8,5 óra | A heti táblázat szerinti interjú, tervezés vagy fejlesztés |
| Ellenőrzés és heti lezárás | 1 óra | Végigpróbálás, elkészült/nem készült el, tényleges órák |
| Tartalék | 2 óra | Csúszás, váratlan hiba, tanulás |

Ez ugyanannak a heti 10 + 2 órának egy lehetséges elosztása; a tervezés és az ellenőrzés nem plusz idő. A fókuszblokk legyen legalább 3 óra, mert a fejlesztésnél a rövid, széttördelt idő sokat veszít a hatékonyságából.

Egyszerre egy fő munkacsomag legyen folyamatban.

### Rövid heti napló

```text
Hét:
Heti cél:
Elkészült eredmény / elérési hely:
Elfogadási feltétel teljesült? Milyen bizonyítékkal?
Tervezett / tényleges órák:
Felhasznált tartalék:
Külső visszajelzés:
Nyitott hibák és akadályok:
Döntés: folytatás / szűkítés / ismételt próba
Következő hét egy fő eredménye:
```

## 5. Csúszáskezelés

| Helyzet | Teendő |
|---|---|
| Egy feladat néhány órát csúszik | A heti tartalékot használd, és írd fel az okot |
| Két héten át elfogy a teljes tartalék | Becsüld újra a hátralévő feladatokat; ne tekintsd változatlannak a 17. heti határidőt |
| A költözésig nem fér bele a validációs kapu | A kaput ne hagyd ki: a hiányzó interjúkat távolról pótold, és addig ne kezdj fejlesztést |
| A költözés után hetekig nincs kapacitás | Hosszabbítsd a szünetet; a tervet heti órák, nem naptári dátumok szerint folytasd |
| Interjúalany nem ér rá | Haladj saját esetekkel, de a keresleti feltételt hagyd nyitva |
| Frontend több munkát igényel | Egyszerűsíts elrendezést és kényelmi funkciót; a mentési állapot maradjon egyértelmű |
| Túl sokféle edzői módszer kerül elő | Egy kiválasztott célprofilra és beállításkészletre szűkíts |
| Jogosultsági vagy tiltott módosítási hiba van | A javítás előzze meg a bővítést és a külső adat használatát |
| Nincs érzékelhető időnyereség | Vizsgáld az adatbevitelt és az ellenőrzési terhet; ne több AI-funkcióval próbáld elfedni |

**Először elhagyható:** részletes grafikonok, több importformátum, megjelenési finomítások, extra AI-beszélgetés, további módosítási helyzetek. **Megőrzendő alap:** helyes naplózás, jogosultság, tervverzió, szakmai korlát és jóváhagyás.

## 6. A szakasz lezárásának ellenőrzőlistája

- [ ] Dokumentáltuk, kinek és milyen konkrét helyzetben hasznos az eszköz.
- [ ] A validációs kapu mindhárom feltétele (kereslet, időigény, megkülönböztetés) teljesült, bizonyítékkal.
- [ ] Megvan a Kaizer és egy további alternatíva tesztjének értékelési lapja.
- [ ] Van legalább 5 mért kézi módosítási idő, és ehhez összevetett asszisztált idő.
- [ ] Megvan a szabálykatalógus és az 50 esetből álló induló készlet.
- [ ] Egy program importálható, és a tényleges teljesítés naplózható.
- [ ] Az elkülönített edzői fiókok hozzáférése ellenőrzött.
- [ ] A kimaradás és áthelyezés javaslata összevethető a régi tervvel.
- [ ] A jóváhagyás új tervverziót hoz létre, a múltbeli teljesítés megőrzésével.
- [ ] Az AI-kimenetet a rendszer ellenőrzi; hiba esetén a naplózás tovább működik.
- [ ] Nincs ismert, nyitott kritikus hiba a támogatott folyamatban.
- [ ] A következő szakasz (gyakoriságváltás, gyakorlatcsere, mentés-visszaállítás, külső pilot előkészítése) a próba eredménye alapján újrabecsülve.

## 7. Kapcsolat a kutatással

Ez az ütemterv a meglévő kutatási anyag végrehajtási bontása. Nem tartalmaz új piaci árakat vagy hatásossági állításokat; a szakmai és technológiai indoklások forrásai a fő dokumentumban találhatók.

| Ütemezési döntés | Indoklás helye a fő tervben |
|---|---|
| Edzői indulás és külső interjú | 4. és 13. fejezet |
| Időmérés mint kritikus feltevés | 4.1. és 15. fejezet |
| Kaizer-teszt és megkülönböztetés | 3.3. és 3.4. fejezet |
| Szabályok, hiányzó adat és felülvizsgálat | 6–7. fejezet |
| Adatbázis, verziók és AI-feladatmegosztás | 8–9. fejezet |
| Adatkezelés és funkcióhatár | 11. fejezet |
| Munkaórák és teljes projektütem | 12. fejezet |
| Tesztesetek és mérési kapuk | 13. fejezet |

A heti órabontás és a kapuk célértékei (például a 10 perces és havi 5 eses időigény-küszöb) saját tervezési javaslatok. A tényleges ráfordítás és a mérések alapján frissítendők.
