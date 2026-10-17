# Erőemelő AI-alkalmazás – kutatás és megvalósítási terv

Kutatás dátuma: 2026. október 16. Az árak ekkor ellenőrzött, nyilvános listaárak; a pénztárban a régió, adó és értékesítési csatorna eltérést okozhat. A saját termékre vonatkozó árak, időigények és célértékek tervezési feltételezések, nem igazolt piaci eredmények.

**Dokumentumverzió: 2.1 – kibővített döntési és megvalósítási anyag.** A 2.0 változat részletesebben vizsgálja a szakmai bizonyítékokat, a célcsoport-választás ellenérveit, a fejlesztési alternatívákat és a gazdaságosságot. A részletesebb munkabontás alapján a pilot munkaidőbecslését is módosítja; a 12. fejezet becslése az irányadó.

**A 2.1 változás:** pótló internetes ellenőrzés 2026. október 16-án. Bekerült egy egyoldalas összefoglaló és a legközelebbi talált konkurens, a Kaizer (3.4. fejezet). Az időnyereség feltevése kritikus, nem mért kockázatként van megjelölve. Bekerült a magyar piac felmérésének első lépése és egy AI-edzéstervek elfogadottságáról szóló pilotvizsgálat. Az árazási, technikai és ütemezési részek nem változtak.

### Hogyan olvasd a következtetéseket?

Négy különböző bizonyítékszint szerepel a dokumentumban:

| Jelleg | Mit jelent? | Mire alkalmas? |
|---|---|---|
| Ellenőrzött termékinformáció | Hivatalos termékoldal, árlista vagy dokumentáció | A közzétett funkció és üzleti ajánlat összehasonlítására |
| Tudományos eredmény | Azonosítható vizsgálat, ismert mintával és módszerrel | Körülhatárolt edzésélettani következtetésre |
| Saját tervezési javaslat | A forrásokból és a helyzetedből levezetett mérnöki/üzleti döntés | Kiinduló megoldás kiválasztására |
| Validálandó hipotézis | Még nem mért kereslet, árérzékenység, megtartás vagy időnyereség | A következő kísérlet megtervezésére |

A források szerint létező funkció nem jelenti, hogy a funkció jó minőségű vagy minden csomagban elérhető. A nyilvános dokumentációban nem talált funkció pedig nem tekinthető bizonyított hiánynak. A leírt versenytársakat nem vásároltam meg és nem futtattam velük többhetes kontrollált terméktesztet.

A tudományos rész célzott szakirodalmi áttekintés, nem előre regisztrált szisztematikus review. Több vizsgálatnál a nyilvános absztrakt volt a hozzáférhető bizonyíték; ahol teljes szöveg is elérhető volt, azt is felhasználtam. A rövid, kis mintás kutatásokból nem vezetek le univerzális edzésszabályokat. A piaci rész szolgáltatói forrásokra és egy nagy előfizetéses adatjelentésre épül, nem magyar vásárlói felmérésre.

**Olvasási útvonal:** üzleti döntéshez az 1–5. és 10. fejezet; szakmai működéshez a 6–7.; technikai megvalósításhoz a 8–9.; végrehajtáshoz a 12–16.; forráskritikához a 17. fejezet a leghasznosabb.

### Egyoldalas összefoglaló

**Javaslat:** erőemelő edzőknek szóló, emberi jóváhagyással működő tervmódosító asszisztens szűk, fizetős pilotja. Önálló AI-edzőt ebben a szakaszban nem javaslok.

**A koncepció három legfontosabb, még nem igazolt feltevése:**

1. Az edzők érdemi időt töltenek tervmódosítással, és ezt egy asszisztens az ellenőrzéssel együtt is csökkenti. Erre jelenleg nincs független mért adat (15. fejezet).
2. Van elég magyar edző, aki külön eszközért fizetne. Nyilvános magyar piacméret-adatot nem találtam (4.2. fejezet).
3. Az erőemelés-specifikus mélység megkülönbözteti a terméket a már létező, jóváhagyásos adaptív edzői eszközöktől (3.4. fejezet).

**Fő kockázatok:** közeli konkurens már létezik (Kaizer); a szakmai edzői szoftver alacsony áron elérhető (RTS: 20 sportoló 79 USD/hó); az AI által generált edzésterv önmagában könnyen pótolható.

**A következő két hét:** 10 saját módosítási eset leírása; legalább 4 edzői interjú, a módosítás idejét percben mérve; a Kaizer és még 2–3 konkurens kipróbálása azonos eseteken; végül folytatási döntés (16.1. fejezet).

**Továbblépési feltétel:** legalább három, tőled független edző fizet a pilotért, és mérhetően időt nyer (13. fejezet).

## 1. Javasolt döntés

Elsőként **erőemelő edzők munkáját segítő, meglévő edzésterveket módosító asszisztenst** érdemes validálni. Első felhasználója te lehetsz, majd néhány külső edző. A sportoló egyszerű mobilos felületen naplóz; az edző egy ellenőrizhető változtatási javaslatot kap, amit elfogadhat vagy szerkeszthet.

Az ajánlat: „A sportoló tényleges edzései és változó időbeosztása alapján előkészíti a következő tervmódosítást, megmutatja annak okát, és megtartja az edző programozási elveit.”

Ez egy ellenőrizendő piaci hipotézis. A kutatás nem igazolta, hogy ilyen részfunkció egyik versenytársban sincs. A lehetőséget az adott munkafolyamat jobb megoldásában kell keresni, és valódi használati próbával igazolni.

Az induló technikai megoldás saját webalkalmazás, saját adatbázis és a szolgáltató által fizetett AI API legyen. Az MCP ugyanennek a rendszernek későbbi kapcsolódási felülete lehet. A normál ügyfélnek ne kelljen fejlesztői kulcsot vagy külön AI-előfizetést kezelnie.

## 2. Mit tudunk a hátteredről?

A jelen beszélgetésben megerősítetted a hároméves edzői tapasztalatodat. Az elérhető közös előzményekből látszik a Python/MCP-alapú Business Central projekt és az AI-val támogatott fejlesztési munkafolyamatod. Az „Erőbecslés konviban” beszélgetés saját erőemelői gyakorlatot is mutat.

A „Claude profil összeállítása” beszélgetést megtaláltam, de a profil válaszszövege az elérhető eszközben csak tartalomhivatkozásként jelent meg. A teljes közös memóriát ezért nem tekintem elolvasottnak. Az előzmények nem bizonyítják az önálló frontend-, biztonsági vagy éles üzemeltetési jártasságodat. Heti időkereted, induló költségkereted, jelenlegi ügyfélszámod és külső tesztelői köröd még ismeretlen.

A releváns előnyöd az edzői döntések ismerete és a technológiai megvalósítás iránti gyakorlatias érdeklődés kombinációja. Egy kis, felügyelt pilot reális kiindulás. Egy önálló, minden helyzetet kezelő AI-edző, natív mobilalkalmazásokkal, videóelemzéssel és saját tanított modellel lényegesen nagyobb vállalkozás.

### 2.1. Hogyan hasznosítható a tapasztalatod?

A három év edzői gyakorlat akkor válik fejlesztési előnnyé, ha az ismétlődő döntéseket konkrét esetekké tudod alakítani. Például: milyen jelek miatt változtattál egy sportoló heti gyakoriságán; mikor volt a gyakorlatcsere preferencia, és mikor fájdalom miatti korlátozás; milyen adat hiányzott egy jó döntéshez. Ebből építhető tesztelhető szabálykészlet és referenciaadat.

Saját módszered kezdetben megfelelő kiindulás. A külső edzők bevonásával viszont szét kell választani a szakmailag tiltott megoldást, az adott edző preferenciáját és az egyébként elfogadható alternatívát. Két edző eltérő döntése nem feltétlenül jelent hibát. A rendszernek a felhasználó edző módszerét és döntési jogát is kezelnie kell.

| Terület | Amit a kontextus alátámaszt | Következő ellenőrzés |
|---|---|---|
| Edzői döntések megértése | Hároméves tapasztalatod van | 20 valós esethez le tudod-e írni a döntés feltételeit és indokát? |
| AI-val támogatott fejlesztés | Van közös Python/MCP-projektelőzmény | Egy kis funkciót tudsz-e hibakeresni, módosítani és tesztelni? |
| Termékfejlesztés | Van konkrét sportolói problémafelvetésed | Egy idegen edző segítség nélkül végig tudja-e használni a folyamatot? |
| Éles üzemeltetés és adatbiztonság | Nincs elég kontextus | Jogosultsági hiba, mentés-visszaállítás és szolgáltatáskiesés kezelése |
| Értékesítés | Kapcsolati kör és ügyfélszám nem ismert | Elérsz-e 10 alkalmas interjúalanyt és 3 külső fizető tesztelőt? |

**Saját értékelésem:** a fő kockázat valószínűleg a teljes szolgáltatás összerakása és működtetése: megfelelő naplózás, adatminőség, szakmai ellenőrzés, támogatás és ügyfélszerzés. Az AI-val gyorsan elkészülő prototípus ezekből csak egy részt old meg. Egy működő pilot ugyanakkor önállóan is értékes szakmai és fejlesztői portfólióeredmény lehet, még ha később nem válik nagy szoftverüzletté.

## 3. Versenytársak és árak

Az alábbi funkciók a szolgáltatók dokumentált állításai. Nem végeztem mindegyik termékben többhetes gyakorlati összehasonlítást, és a marketingállításokat nem tekintem független hatásossági bizonyítéknak.

| Termék | Fő cél és dokumentált képesség | Ellenőrzött ár | Következmény a saját termékre |
|---|---|---|---|
| JuggernautAI | Erőemelés/powerbuilding, visszajelzések alapján módosuló program | 34,99 USD/hó vagy 349,99 USD/év | Az általános adaptív erőemelő app már erős versenyt kap. [Árazás](https://www.juggernautai.app/pricing) |
| Sheiko Gold | Napi készenlétre reagáló tervezés, változó gyakoriság, gyakorlatcsere | US App Store: 19,99 USD/hó | A felsorolt alkalmazkodási ötleteid több eleme már megjelenik a piacon. [Termék](https://sheikogold.com/), [ár](https://apps.apple.com/us/app/sheiko-gold-powerlifting-ai/id1475890027) |
| Fitbod | Személyre szabás edzéselőzmények, cél, eszközök és regeneráció alapján | Weben 15,99 USD/hó; 95,99 USD/év | Szélesebb erősítő edzéses közönségért is sokoldalú termékkel versenyeznél. [FAQ](https://fitbod.me/faqs/) |
| Boostcamp | Edzésprogramok, naplózás, elemzés | Ingyenes alap; Pro 14,99 USD/hó vagy 59,99 USD/év | Egy terv és egy napló önmagában nehezen árazható prémiumként. [Pro](https://www.boostcamp.app/pro) |
| TrainHeroic | Edzői programkészítés és sportolókezelés | 5 sportoló: 17,99; 15: 34,99; 25: 44,99 USD/hó | Az edzői adminisztrációs felület is bejáratott kategória. [Árak](https://www.trainheroic.com/coach/) |
| MyStrengthBook | Egyéni edzésprogramozás és coachingüzlet | PULL: 3,99 USD/kliens/hó; PUSH: 20% bevételrészesedés | A sportolószámhoz kötött árazás és az edzőn keresztüli terjesztés releváns minták. [Árak](https://mystrengthbook.com/pricing-coaching) |
| Everfit | Coachingplatform, szövegből edzést strukturáló AI, ügyfélkommunikáció | Ingyenes alap 5 kliensig; Pro havi számlázással 29 USD/10, 49 USD/20 kliens | Az „AI edzőknek” állítás önmagában sem megkülönböztető. [Árak](https://everfit.io/pricing/), [AI](https://help.everfit.io/en/articles/9373485-introducing-ai-workout-builder) |
| RTS Training Lab | Erőemelő programozás, sportolói válaszok elemzése, szakmai támogatás | 10 sportoló: 49; 20: 79; 30: 99 USD/hó | Közvetlen szakmai összehasonlítási alap az edzői döntéstámogatáshoz. [Termék és árak](https://rtslab.reactivetrainingsystems.com/) |
| Kaizer | Edzői platform; saját állítása szerint minden naplózott edzés után újraszámolja a terhelést és ismétlést, a végső döntés az edzőé | Központi árat nem találtam; országonkénti árazást említ | A legközelebbi talált konkurens a javasolt munkafolyamathoz; lásd 3.4. [Saját összehasonlító cikke](https://kaizer.app/en/blogs/best-personal-trainer-software-2026) |

A JuggernautAI egy külön kampányoldalán eltérő ár is szerepel; itt a központi árazási oldalt vettem alapul. A Sheiko éves árát nem rögzítem egyetlen biztos összegként: az App Store leírása és vásárlási listája eltérő éves összeget mutat. Az Evolve Training Appot is kerestem, de egységesen ellenőrizhető aktuális központi havidíjat nem találtam, ezért bizonytalan árat nem vettem fel a táblázatba.

A valódi alternatíva sok edzőnél a meglévő táblázat és üzenetküldő, esetleg egy általános AI-asszisztens. A saját terméknek a váltás vagy a plusz eszköz költségét is ki kell termelnie. Az induló import/export csökkentheti ezt, de harmadik fél platformjához automatikus integrációt csak tényleges API-hozzáférés ellenőrzése után szabad ígérni.

### 3.1. Mit tanulhatunk a különböző versenytárscsoportokból?

**JuggernautAI és Sheiko Gold:** a szakmai módszer és a hozzá kapcsolódó bizalom fontos része az ajánlatnak. A következtetésem az, hogy az induló alkalmazásodnak hitelesen bemutatható döntési elvek kellenek. A felhasználónak értenie kell, milyen módszer szerint kap javaslatot. A Sheiko nyilvános leírása kifejezetten említ változó időbeosztást és gyakorlatcserét; ezeket önmagukban nem lehet egyedi újításként pozicionálni. [JuggernautAI](https://www.juggernautai.app/pricing), [Sheiko Gold](https://sheikogold.com/)

**Fitbod és Boostcamp:** a könnyen használható napló és a programhoz való hozzáférés önálló vásárlói elvárás. A tervezési következtetés az, hogy a sportoló által látott felület minősége akkor is fontos, ha az edző fizet. Ha a sorozatnaplózás kényelmetlen, kevés adat lesz, és az alkalmazkodás is gyenge lesz. [Fitbod](https://fitbod.me/faqs/), [Boostcamp](https://www.boostcamp.app/pro)

**TrainHeroic, MyStrengthBook és Everfit:** az edzői munkafolyamat sok összekapcsolódó funkcióból áll. Egy teljes platform helyettesítése jelentős fejlesztés és váltási költség. Ezért az első pilothoz egy kijelölt program és egy szűk módosítási folyamat támogatását javaslom. Az Everfit dokumentált AI-edzéskészítője szöveges programleírást is strukturál; a szabad szöveges bevitel ezért hasznos alapfunkció lehet, de önálló piaci előnyként gyenge. [TrainHeroic](https://www.trainheroic.com/coach/), [MyStrengthBook](https://mystrengthbook.com/pricing-coaching), [Everfit AI](https://help.everfit.io/en/articles/9373485-introducing-ai-workout-builder)

**RTS Training Lab:** a termék programozást, trendkövetést és sportolói reakciók alapján történő módosítást is kínál, szakmai közösséggel együtt. Saját következtetésem: az edzői célcsoportban is létezik komoly, szakterületre épülő konkurencia. A „döntéstámogatás” kategóriáját nem tekinthetjük üresnek. [RTS](https://rtslab.reactivetrainingsystems.com/)

### 3.2. Összehasonlítható edzői költség: 20 aktív sportoló

Az alábbi számítás az előző árlistákból származik, kedvezmény és esetleges adó nélkül. Nem állítja, hogy a csomagok funkcionálisan egyenértékűek.

| Rendszer | 20 sportoló kiszolgálásának publikált havi alapára | Számítás |
|---|---:|---|
| TrainHeroic | 44,99 USD | 25 férőhelyes csomag szükséges |
| Everfit Pro | 49 USD | 20 klienses, havi számlázású csomag |
| MyStrengthBook PULL | 79,80 USD | 20 × 3,99 USD |
| RTS Training Lab | 79 USD | 20 sportolós csomag |

Ez két külön ártesztet indokol. Ha a saját alkalmazás kivált egy meglévő rendszert, a teljes platform árához viszonyítják. Ha kiegészítő eszköz, a meglévő előfizetésen felül kell értéket teremtenie. Ugyanaz a 15–25 ezer Ft-os havidíj e két helyzetben nagyon eltérően hathat. Az interjúban ezért a jelenlegi szoftverköltséget és a tervezett használati módot is rögzíteni kell.

### 3.3. A tényleges versenytársteszt terve

A következő kutatási lépés 3–4 kiválasztott termék azonos eseteken történő kipróbálása legyen; ezek egyike a Kaizer legyen (3.4. fejezet). A vizsgálatot külön, jogosult hozzáféréssel lehet elvégezni; az alábbi táblázat tesztterv, nem elvégzett összehasonlítás.

| Teszthelyzet | Mit kell mérni? | Mi számít jó eredménynek? |
|---|---|---|
| Egy négynapos terv bevitele | Idő, kézi javítások, elvesző mezők | Az edző módszere és a gyakorlatváltozatok megmaradnak |
| Egy edzés kihagyása | Áttervezési idő, szükséges kézi lépések | A változás átlátható, nem duplikálódik munka |
| Átállás három edzésnapra | Elosztás és terhelés változása | Érthető, mi maradt meg és miért |
| Gyakorlatcsere | Előzmények és terhelés kezelése | A változatok adatai nem keverednek ellenőrizetlenül |
| Hiányos RPE-adat | A rendszer kérdez-e, vagy feltételez? | A bizonytalanság látható |
| Fájdalomjelzés | Automatikus és emberi lépések | Nem történik indokolatlan, magabiztos terhelési előírás |
| Edző felülír egy javaslatot | Visszakereshetőség és későbbi használat | Megmarad a döntés és annak hatóköre |
| Kilépés a rendszerből | Adatkinyerés és átvihetőség | A sportoló naplója hozzáférhető marad exportként |

Értékelési lap: termékverzió, csomag, teszt dátuma, bemeneti eset, eltelt idő, kézi módosítások, bizonytalan eredmény, bizonyító képernyőkép. A hiányzó funkciót csak kipróbálás vagy egyértelmű dokumentáció után jelöljük hiányként.

### 3.4. Pótló ellenőrzés: a legközelebbi konkurens és a megkülönböztetés

A 2.1-es ellenőrzés az edzői munkafolyamatra koncentrált. Fő kérdése: létezik-e már olyan eszköz, amely a sportoló visszajelzései alapján tervmódosítást javasol, és ezt az edző hagyja jóvá. A források többsége szolgáltatói blog vagy összehasonlító oldal; ezek egy része konkurens által írt marketinganyag. Ezért az alábbiak kipróbálandó állítások, nem igazolt tények.

| Termék | Talált állítás | Forrás jellege |
|---|---|---|
| Kaizer | Minden naplózott edzés után újraszámolja az e1RM-et, a terhelést és az ismétlést; a végső döntés az edzőé. A jóváhagyási folyamatot a cikk nem részletezi. | Saját blog. [Forrás](https://kaizer.app/en/blogs/best-personal-trainer-software-2026) |
| RTS Training Lab | Sportolói válasz alapján történő módosítást és monitorozó mutatókat említ; AI-t nem. A módosítási döntés a leírás alapján az edzőé. A sportolóknak a napló ingyenes. | Hivatalos termékoldal. [Forrás](https://rtslab.reactivetrainingsystems.com/) |
| TrueCoach, Everfit, TrainHeroic | Összehasonlító cikkek szerint az AI legfeljebb terv- vagy szöveggenerálásra szolgál. A TrainHeroicnál szabályalapú RPE-autoreguláció szerepel. | Harmadik fél, részben konkurens. [Trainerfu](https://www.trainerfu.com/blog/everfit_alternatives/), [Everfit blog](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach) |
| JuggernautAI, Titans Grip, Strength Coach AI | Adaptív programozás közvetlenül a sportolónak; edzői felületet vagy jóváhagyási folyamatot nem találtam. | Értékelések, áruházi leírás. [GGR](https://garagegymreviews.com/juggernautai-review), [Titans Grip](https://www.titans-grip.com/blog/best-powerlifting-app-2026/) |

**Következtetés:** a „visszajelzés alapján módosít, az edző dönt” mintát a Kaizer a saját leírása szerint már kínálja. Szakmai ajánlások is ebbe az irányba mutatnak: érdemi változtatásnál és fájdalomjelzésnél maradjon edzői jóváhagyás. [Coaching Portal](https://coachingportal.io/blog/ai-fitness-coaching-trends) Ez a koncepciót nem cáfolja, de az 5. fejezet négy képessége önmagában nem elég megkülönböztetés.

**A megkülönböztetés lehetséges alapjai** (saját tervezési javaslat, validálandó):

- **Erőemelés-specifikus logika:** versenyfogás-változatok elkülönítése, RPE/RIR-adatok forrása és megbízhatósága, versenyre hangolás, a kimaradt munka blokkcél szerinti kezelése. Egy általános edzői platform ezt jellemzően nem modellezi részletesen.
- **Az edző saját módszerének befogadása:** a programozási logikát nem egy beépített képlet adja (pl. NSCA-táblázat); az edző szabályai és tiltásai határozzák meg.
- **Átlátható különbségnézet és indoklás:** az edző látja, mi változott és melyik szabály miatt.
- **Magyar nyelv és személyes bevezetés:** kezdeti hozzáférési előny, de önmagában könnyen másolható.

**Teendő:** a Kaizert a 3.3. fejezet teszttervével, azonos erőemelő eseteken kell kipróbálni. Ha erőemelő esetekben is jól teljesít, a saját terméket szűkebbre kell pozicionálni, vagy inkább a heti edzői összefoglaló irányába kell fordítani (5.1. fejezet).

## 4. Edzők vagy sportolók?

| Irány | Ki fizet és miért? | Indulási előny | Legnagyobb nehézség | Értékelés |
|---|---|---|---|---|
| Edzői asszisztens | Edző; időnyereség, áttekinthetőbb döntések | Saját edzői rutinból kiindulhatsz, kevés vevővel validálható | Különböző módszerek, váltási ellenállás, szakmai kontroll | Elsőként ezt tesztelném |
| Önálló adaptív app rendszeresen edző sportolóknak | Sportoló; használható terv és gyors alkalmazkodás | Világos, napi probléma | Meglévő appok, megtartás, bizalom, ügyfélszerzés | Második lépcsőnek jó |
| App pusztán érdeklődőknek | Kezdő; eligazodás, motiváció | Szélesebb elméleti közönség | Bizonytalan edzési szokás és fizetési hajlandóság | Túl tág induló célcsoport |
| AI-val támogatott saját coaching | Saját ügyfeled; személyes edzői szolgáltatás | Kis fejlesztéssel is valódi munkafolyamat tesztelhető | A bevétel továbbra is az idődhöz kötődik | A legjobb első kísérleti kör, ha vannak ügyfeleid |

Az első külső edzői célcsoportot így írnám le: 10–30 aktív erőemelő/erőfejlesztő sportolóval dolgozik, rendszeresen módosít terveket, több adatforrásból rakja össze a helyzetet, és hajlandó egy új eszközt kipróbálni. Ez kutatási célprofil, nem ellenőrzött piacméret.

Ha a későbbi sportolói irányt választod, a „már legalább néhány hónapja rendszeresen edz, ismeri az alapgyakorlatokat, de változik az időbeosztása” szegmens konkrétabb, mint az általános érdeklődő. A magyar nyelv és közeli kapcsolatok jó induló hozzáférést adhatnak; a magyar nyelv önmagában könnyen másolható előny.

### 4.1. Miért előnyös az edzői indulás, és mikor lenne mégis rossz döntés?

Az edzői indulás mellett a következő érvek szólnak: saját tapasztalatodból tudsz referenciaeseteket adni; az edző értékeli a javaslatot, így korán felismerhető a hiba; az időnyereség pénzügyi értékké fordítható; kevés ügyfél is elég egy első használati mintához. Ezek tervezési érvek, nem bizonyított magyar piaci adatok.

**Kritikus, nem mért feltevés:** az időnyereség-érvhez nem találtam független mérést arról, hány percet töltenek az edzők tervmódosítással. A „heti 10+ óra adminisztráció” típusú adatok edzői szoftvert árusító cégektől származnak, és a teljes adminisztrációra vonatkoznak, nem kifejezetten a tervmódosításra. [Példa szolgáltatói állításra](https://www.trainerfu.com/blog/how-ai-fitness-coaching-saves-trainers-10-hours-per-week/) A 10. fejezet árazási és értékajánlati logikája nagyrészt erre épül, ezért az interjúk első mérési célja ennek percben való rögzítése legyen.

Az ellenérvek ugyanilyen fontosak. Az edző lehet elégedett a jelenlegi rendszerével. A módosítás az egyik legértékesebb szakmai feladatának tűnhet, amelyet nem akar átadni. Egy új alkalmazás kezdetben extra adminisztrációt okozhat. Ha minden ügyfél teljesen más módszert akar, az alkalmazás könnyen egyedi fejlesztési szolgáltatássá válik.

| Amit a kutatásban tapasztalsz | Következmény |
|---|---|
| Edzők visszatérő, időigényes problémát mutatnak, és hajlandók adatot behozni | Folytatható az edzői asszisztens |
| Edzők főként áttekintést kérnek, programozást nem adnának át | Elemző és összefoglaló termékre szűkítés |
| Sportolók már aktívan keresnek megoldást, de az edzők nem érdeklődnek | Szűk sportolói pilot indokolt lehet |
| Csak a te ügyfeleid használják, külső edző nem fizet | Belső coachingeszközként értékesíthető közvetetten |
| Minden edző külön funkciórendszert kér | Egységes célprofil vagy termékhatár hiányzik |
| A fő probléma az alapadatok hiánya | Előbb a naplózási és visszajelzési folyamatot kell megoldani |

### 4.2. Piacméret helyett ellenőrizhető elérési terv

Nem találtam olyan ellenőrzött, kellően szűk nyilvános adatot, amelyből megbízhatóan kiszámítható a fizetőképes magyar erőemelő edzők száma. Egy általános globális fitneszpiaci méret ezt nem pótolja. Az induló tervezéshez az elérhető ügyfelek számát kell alulról felépíteni.

Példaforgatókönyv: 40 releváns edzőből 20 beszélgetés, ezekből 8 bemutató, 5 pilot és 3 fizetős folytatás. Ezek kísérleti tervezési számok, nem várható konverziók. A lista személyes kapcsolatokból, termekből, edzői képzésekből és szakmai közösségekből állhat össze. Minden szakaszban külön rögzítsd, miért esett ki valaki.

Ha harminc fizető edző a következő üzleti cél, és a tényleges folyamatban a megfelelően megszólított edzők 10%-ából lesz előfizető, körülbelül 300 megfelelő érdeklődő kell. A 10% itt pusztán számítási feltétel. Ez teszi láthatóvá, hogy a fejlesztés mellett az ügyfélszerzéshez is rendszeres idő kell.

**Első lépés a magyar piac felméréséhez:** a 2.1-es ellenőrzés sem talált nyilvános adatot a magyar erőemelő szövetség(ek) versenyzői, egyesületi vagy edzői létszámáról. Megjegyzés: magyar versenyeket több szervezet is rendez. Javasolt kiindulás egy saját táblázat, amely legalább 40 releváns edzőt tartalmaz. Lehetséges források: hazai versenyek eredménylistái és az ott feltüntetett egyesületek, az [OpenPowerlifting](https://www.openpowerlifting.org/) magyar versenyzői adatai, a szövetségek közvetlen megkeresése, erőemelésre szakosodott termek, valamint edzői képzések és közösségek. Minden sorban szerepeljen a forrás, a becsült sportolószám, a jelenleg használt eszköz és az elérés módja. Ha 40 releváns edző sem azonosítható, ez önmagában erős jelzés a szűk piacra.

### 4.3. Mit mondanak az előfizetéses alkalmazások adatai?

A RevenueCat 2026-os jelentése több mint 115 ezer alkalmazás adatait elemzi, jellemzően 2025-ös időszakkal. Az AI-kategóriában a havi előfizetések 12 hónapos megtartási mediánja 6,1%, a nem AI-kategóriában 9,5%. A minta RevenueCatot használó, aktivitási/bevételi küszöböt teljesítő alkalmazásokat tartalmaz; nem a teljes apppiacot, és nem külön a magyar erőemelő SaaS-okat. Az összefüggés nem bizonyítja, hogy az AI okozza az alacsonyabb megtartást. [Jelentés és módszertan](https://www.revenuecat.com/state-of-subscription-apps)

Saját következtetésem: az induló fő mutató a visszatérő használat és a fizetős megújítás legyen. Az első edzésterv elkészítése csak az első értékpillanat. A második és harmadik értékpillanat a hétköznapi változások kezelése, az edzői időnyereség és az előzmények folyamatos használhatósága.

Az éves díj előre pénzt hozhat, de a tényleges használat csökkenését elfedheti. Emiatt külön kell mérni a fizető státuszt, a naplózott edzést és az elvégzett edzői felülvizsgálatot.

## 5. Mitől legyen értékes?

A megkülönböztetést négy egymáshoz kapcsolódó képességre építeném:

1. Az edző meglévő programját és szabályait fogadja be.
2. A ténylegesen elvégzett munkát külön kezeli az előírt tervtől.
3. Csak a szükséges változásokat javasolja, az eredeti cél megtartásával.
4. Megmutatja a régi és új terv különbségét, az adatokat, az indokot és a bizonytalanságot.

Példa: „A pénteki edzés kimaradt, vasárnap tudok menni, jövő héttől négy nap fér bele.” Az asszisztens azonosítja a kimaradt edzést, megvizsgálja a következő alkalmakat és a blokk célját, majd módosítási javaslatot készít. Az edző egy képernyőn láthatja, melyik gyakorlat hova kerül és hogyan változik a terhelés.

A siker mércéje az legyen, hogy a javaslat ellenőrzése és javítása együtt kevesebb idő, mint a kézi újratervezés. A jó szöveges magyarázat ezt önmagában nem bizonyítja.

### 5.1. Három termékváltozat ugyanarra a problémára

| Változat | Mit csinál a termék? | Miért lehet jó? | Miért lehet kevés? |
|---|---|---|---|
| Heti edzői összefoglaló | Kiemeli a kimaradásokat, eltéréseket és figyelmet igénylő sportolókat | Viszonylag könnyen ellenőrizhető, kisebb beavatkozás | Az átírás még az edzőre marad |
| Tervmódosítási asszisztens | Az összefoglaló után konkrét változtatást készít elő | Közvetlenül a munkafolyamat időigényét célozza | Megbízható adat és pontos szakmai keret kell |
| Önálló sportolói tervező | Közvetlenül kiadja a következő edzést | Kevesebb napi edzői közreműködés, szélesebb elérés | Több önálló döntés, nagyobb minőségi és támogatási teher |

A fejlesztést az első változatból a második felé építeném. Így a rendszer már akkor tesztelhető, amikor a módosításokat még kézzel végzed. A harmadik változatnak csak akkor van erős alapja, ha a másodiknál már ismert, milyen esetekben lehet megbízni a javaslatokban.

### 5.2. Mit mutasson a felület?

Edzői főnézet: melyik sportoló igényel figyelmet, mi változott, milyen adat hiányzik, és melyik tervmódosítás vár jóváhagyásra. Ne egyszerűen sok grafikont mutasson; a felület a következő szükséges döntést tegye láthatóvá.

Sportolói főnézet: mai edzés, következő sorozat, előző releváns teljesítmény, gyors naplózás és „változott a helyzetem” gomb. Rövid beviteli lehetőségek: másik nap, kevesebb idő, eszközhiány, gyakorlatpreferencia, fájdalomjelzés. Szabad szöveg legyen választható kiegészítés.

Módosítási kártya: érintett napok és gyakorlatok; előző/új előírás; a döntéshez használt adatok; ismeretlen tényezők; edzői szabály; jóváhagyás/szerkesztés/elutasítás. A magyarázat a ténylegesen alkalmazott szabályból és adatokból készüljön. Ne engedjük, hogy a modell utólag olyan szakmai okot találjon ki, amely nem szerepelt a döntésben.

## 6. Mit jelent a „folyamatosan tanuló” alkalmazás?

Három eltérő szintet érdemes külön kezelni.

**Tartós memória:** tárolja a terveket, elvégzett sorozatokat, RPE-t, időbeosztást, preferenciákat és edzői döntéseket. Ez adatbázis-kezelés, nem modellbetanítás.

**Személyenkénti alkalmazkodás:** frissíti a teljesítménybecslést és a következő javaslatok paramétereit. Figyeli például a cél-RPE és a tényleges RPE eltérését, a teljesítési arányt és a gyakorlatonkénti trendet. Ehhez kezdetben szabályok és statisztikák is elegendők. Egyetlen rossz nap nem bizonyít tartós visszaesést; hiányzó adatból sem szabad hamis pontosságú következtetést levonni.

**A teljes termék fejlesztése:** az elfogadott, szerkesztett és elutasított javaslatokat értékeled, majd verziózott szabályokat vagy modelleket javítasz. Az edzői elfogadás folyamatminőséget jelezhet, de nem bizonyít jobb sporteredményt. A hosszú távú eredményeket és a különböző sportolói csoportokat külön kell vizsgálni.

Az MVP-be az első két szint kell. Saját nyelvi modell tanítása és automatikus, éles önátírás nem indokolt. Modellfinomhangolás később, megfelelő jogalappal gyűjtött, jó minőségű adatok és elkülönített értékelési készlet mellett mérlegelhető.

Az autoreguláció szakmailag kutatott megközelítés. Egy 21 edzett férfival végzett, nyolchetes vizsgálatban az RPE- és százalékos terhelésadás mellett is javult az erő, a csoportok közötti különbség nem volt szignifikáns. Ez támogatja az RPE használhatóságát, de nem bizonyítja egy AI-alkalmazás fölényét, és nem általánosítható automatikusan minden sportolóra. [Helms és munkatársai, 2018](https://pubmed.ncbi.nlm.nih.gov/29628895/)

### 6.1. Részletesebb szakirodalmi alap és korlátok

**Gyakoriság és volumen.** Saric és munkatársai 27 edzett férfit osztottak heti három vagy hat edzésre, hat héten át, azonos edzésvolumennel. Mindkét csoport erősödött; nem találtak szignifikáns csoportkülönbséget az erőfejlődésben. Ez rövid, férfi résztvevőkre korlátozott vizsgálat, nem egyéni optimumot meghatározó szabály. [Saric és munkatársai, 2019 – nyilvános absztrakt](https://pubmed.ncbi.nlm.nih.gov/30363041/)

Terméktervezési következtetésem: a napok számának változását elsősorban ütemezési és terheléselosztási problémaként kezeljük. Külön döntés legyen a heti munka mennyisége. A kutatás nem bizonyítja, hogy minden erőemelőnél bármely gyakoriság felcserélhető, vagy hogy a volumen korlátlanul besűríthető rövid edzésekbe.

**RIR-becslés pontossága.** Egy 58 résztvevős vizsgálatban a becslések a bukáshoz közeledve és későbbi sorozatokban pontosabbak voltak. A vizsgált körülmények között a nem és az edzésmúlt nem mutatott szignifikáns hatást a hibára. A feladatok bicepszhajlítást, tricepszletolást és ülő evezést tartalmaztak; ez korlátozza a közvetlen általánosítást versenyfelhúzásra. [Remmert, Laurson és Zourdos, 2023 – absztrakt](https://pubmed.ncbi.nlm.nih.gov/37036795/)

Terméktervezési következtetésem: egy önbevallott RPE/RIR érték hasznos jel, de nem műszeres mérés. A rendszer tárolja, ki adta meg, melyik sorozatra vonatkozik, és ténylegesen megadott vagy becsült érték-e. A sorozat-RPE és a teljes edzésre vonatkozó RPE külön mező legyen.

**Nem garantált, hogy a pontosság pusztán idővel javul.** Egy kilenc edzett férfival végzett, hathetes fekvenyomásos vizsgálatban az abszolút RIR-becslési hiba nem javult szignifikánsan. A kis minta miatt ez sem végleges válasz, de indokolja, hogy a „több napló = automatikusan jobb mérés” feltételezést ne vegyük készpénznek. [Remmert és munkatársai, 2023 – kiadói absztrakt](https://journals.sagepub.com/doi/10.1177/00315125231189098)

**Újabb, részben eltérő eredmény.** Egy 2025-ös, tízhetes vizsgálatot 31 edzett résztvevő fejezett be. A változó RIR-cél és az állandó 1 RIR mellett nem találtak szignifikáns különbséget az erő- és izomméret-változásban; a változó csoport átlagos edzés-RPE-je alacsonyabb volt. Bizonyos RIR-becslések javultak a változó csoporton belül, de a pontosság változásának csoportközi különbsége nem volt szignifikáns. A résztvevők visszajelzést és részleges felügyeletet is kaptak. [Martikainen és munkatársai, 2025 – teljes szöveg](https://link.springer.com/article/10.1007/s42978-025-00338-8)

Saját következtetésem a két pontossági kutatásból: érdemes oktatást és visszajelzést adni, de a rendszer ne emelje automatikusan egy adat megbízhatóságát pusztán a használati hetek száma alapján. A felhasználóhoz kötött, ellenőrizhető konzisztenciát kell mérni.

**Fáradás és bukáshoz való közelség.** Refalo és munkatársai 24 edzett nőnél és férfinál, hat fekvenyomás-sorozatos protokollban nagyobb akut fáradást mértek a bukáshoz közelebbi végrehajtásnál. A vizsgálat egy meghatározott gyakorlatra és rövid regenerációs időszakra vonatkozott. [Refalo és munkatársai, 2023 – teljes szöveg](https://link.springer.com/article/10.1186/s40798-023-00554-y)

Terméktervezési következtetésem: az elvégzett súly × ismétlés × sorozat mellett a terhelés szubjektív nehézsége is releváns lehet. Ebből nem vezethető le univerzális 48 órás pihenőszabály minden sportolóra és minden gyakorlatra. Az alkalmazás ne állítson objektíven mért regeneráltságot olyan adatokból, amelyek csak közvetett jelek.

### 6.2. Következtetések a személyre szabás működésére

Javasolt első állapotmodell gyakorlatonként: utolsó releváns teljesítmények; előírt és tényleges nehézség; teljesített/tervezett munka; hiányzó adatok; változat; utolsó frissítés; edzői korlátozások. A „készenlét” kezdetben több külön megfigyelésként jelenjen meg, ne megmagyarázhatatlan 0–100-as pontszámként.

A kevés adattal rendelkező sportolónál a kiinduló tervet az edző vagy jóváhagyott sablon adja. Az első hetek célja a rögzítés és a nagy eltérések felismerése. Több adat után is csak ott szűküljön a bizonytalanság, ahol valóban összehasonlítható sorozatok vannak. A gyakorlat, ismétléstartomány, végrehajtás és a körülmények változása csökkentheti az összehasonlíthatóságot.

Az e1RM becslésnél minden érték mellett tárolni kell a képlet vagy módszer verzióját és a forrássorozatot. Az e1RM trend ne jelenjen meg megmért versenymaximumként. Gyakorlatcsere után új adatsor vagy kifejezetten jelölt kapcsolat kell; a szünetes és érintéses fekvenyomás nem ugyanaz az adatpont.

A személyre szabás bizonyításához hasonlítsuk össze a rendszert egy egyszerű alappal: az edző eredeti terve és előre rögzített, személyes előzmény nélküli módosítási szabályok. Ha az előzmények hozzáadása nem javítja a döntések használhatóságát vagy az időigényt, a többletbonyolultság még nem indokolt.

### 6.3. Hogyan fejlődjön a termék az edzői döntésekből?

Elutasításkor választható okok: hibás adat; nem megfelelő gyakorlat; túl nagy változtatás; módszertani preferencia; hiányzó kontextus; helyes javaslat, de rossz időzítés. Ezek különböző hibák, más javítást igényelnek. A puszta „elfogadta/nem fogadta el” címke kevés.

Az edző egy javításnál jelölhesse, hogy az csak az adott alkalomra, a sportolóra, a blokkra vagy a saját módszerére vonatkozik. Egy egyszeri kivételt nem szabad automatikusan minden jövőbeli edzésre alkalmazni. Globális szabályváltozást ellenőrzött kiadásként, tesztkészleten lefuttatva vezetnék be.

A kutatási vagy modellfejlesztési adatfelhasználás célját külön kell meghatározni. Attól, hogy valaki a szolgáltatáshoz feltölti az edzésnaplóját, még nem indokolt minden jövőbeli tanítási célra felhasználni. Az edző saját sablonjainál és harmadik féltől származó fizetős programoknál a felhasználási jogosultságot is tisztázni kell.

## 7. Alkalmazkodás az általad felvetett helyzetekhez

Az alábbiak javasolt termékviselkedések; a konkrét terhelési határokat edzői protokoll és tesztelés határozza meg.

| Esemény | A rendszer feladata | Fontos korlát |
|---|---|---|
| Heti 3 napról 4 napra váltás | Meglévő munka elosztása, rendelkezésre álló idő és pihenőnapok figyelembevétele | A plusz nap nem jelent automatikusan egyharmaddal több terhelést |
| Kimarad egy edzés | Jelölje kimaradtként; vizsgálja meg, mit indokolt áthelyezni vagy elhagyni | Ne torlódjon össze automatikusan az összes elmaradt munka |
| Edzés eltolódik | A tényleges dátumok alapján újraellenőrzi a következő napokat | A naptári hét nem feltétlenül azonos az élettani terhelési egységgel |
| Gyakorlatcsere | Cél, eszköz, mozgásváltozat és korlátozás alapján előre elfogadott alternatívák | Az egyik változat súlyát vagy e1RM-jét ne másolja át vakon a másikra |
| RPE a vártnál magasabb | Rögzíti az eltérést; szabály alapján javaslatot készít | Egy adatpont nem elég új hosszú távú profilhoz |
| Fájdalom/sérülés jelzése | Jelölés, érintett automatikus terhelésemelés leállítása, emberi felülvizsgálat | Nem diagnosztizál; nem nyilvánít egy helyettesítő gyakorlatot automatikusan biztonságosnak |
| Hosszabb szünet | Friss állapotfelmérés és edzői visszatérési terv | Ne folytassa automatikusan az utolsó munkasúlyokkal |

Kezdetben minden szakmai módosítás kerüljön jóváhagyásra. Később az edző által beállított kereteken belül egyes egyszerű változások automatizálhatók, de minden változás legyen naplózott és visszavonható.

### 7.1. Esettanulmány: három napról négyre váltás

Illusztratív helyzet: hétfő–szerda–péntek helyett hétfő–kedd–csütörtök–szombat fér bele. Az alkalmazás először azt tisztázza, mikortól érvényes a változás, hány perc áll rendelkezésre, és egyszeri vagy tartós módosításról van-e szó. Ezután megkülönbözteti a fő gyakorlatokat, a kiegészítő munkát és az edző által rögzített prioritásokat.

Javasolt feldolgozás: csak a jövőbeli edzéseket érinti; egy kijelölt tervezési időablakban újraosztja a munkát; ellenőrzi az edző által beállított pihenési és terhelési korlátokat; megmutatja, mely nap változott. Ha a megadott feltételek mellett nem fér el a terv, ezt jelezze, és kérjen döntést az elhagyható elemekről. A heti naptár kitöltése nem lehet fontosabb az edzői korlátoknál.

### 7.2. Esettanulmány: kimaradás és részleges edzés

„Kimaradt az edzés” és „csak a fő gyakorlatot csináltam meg” két eltérő esemény. Előbbinél a tervezett edzés státusza változik; utóbbinál az elvégzett sorozatokat meg kell tartani, és csak a fennmaradó munkát kell értékelni. A részben teljesített edzés teljes áthelyezése duplázást okozna.

Elfogadási feltétel: a már elvégzett sorozat egyszer szerepel az összesítésben; az elhagyott és áthelyezett munka megkülönböztethető; a sportoló következő nézete ugyanazt a jóváhagyott tervverziót mutatja, mint az edzőé.

### 7.3. Esettanulmány: gyakorlatcsere és fájdalom

Elsőként a csere oka legyen strukturált adat: foglalt eszköz, hiányzó eszköz, személyes preferencia, edzői döntés vagy panasz. Az eszközhiány és a fájdalom nem azonos döntési út. Előbbinél egy előre jóváhagyott helyettesítési lista segíthet; utóbbinál a rendszer rögzítse a jelzést és irányítsa emberi felülvizsgálatra.

A termék nem következtethet arra, hogy egy mozgás panaszmentes vagy megfelelő, pusztán azért, mert hasonló izomcsoportot dolgoztat. A szakember által megadott korlátozás külön adat, érvényességi idővel és forrással. Ez a funkcióhatár teszi lehetővé, hogy a pilotban a sérüléses jelzéseket kezeljük, miközben a rehabilitációs döntés felelőse egyértelmű marad.

### 7.4. Változtatási szintek

| Szint | Példa | Kezdeti jóváhagyás |
|---|---|---|
| Adatrögzítés | Sportoló kijavít egy elírt ismétlést | Megerősítés és változásnapló |
| Ütemezési javaslat | Következő edzés új napra kerülne | Edző |
| Szakmai módosítás | Terhelés, volumen vagy gyakorlat változna | Edző |
| Korlátozott eset | Fájdalom, hosszabb kihagyás, egymásnak ellentmondó adatok | Emberi felülvizsgálat, szükség esetén megfelelő szakember |

Az automatizálás bővítése esetcsaládonként történjen. A jól működő naptáráthelyezés nem igazolja, hogy a sérülés utáni terhelési döntés is automatizálható.

## 8. API, saját kulcs vagy MCP?

Az API a modellhívás egyik technikai útja. Az API-kulcs hitelesítési eszköz. Az MCP pedig olyan protokoll, amellyel egy AI-kliens adatokat és műveleteket érhet el. Az előfizetés ettől külön üzleti döntés. [MCP-architektúra](https://modelcontextprotocol.io/docs/learn/architecture)

| Megoldás | Fizetési modell | Felhasználói élmény | Javaslat |
|---|---|---|---|
| Saját app + szolgáltatói API-kulcs | Az ügyfél neked fizet; az AI-használatot te fizeted | Egyszerű belépés, saját felület | Ezt választanám az első fizetős termékhez |
| Saját app + ügyfél API-kulcsa | Neked szoftverdíj, AI-szolgáltatónak használati díj | Kulcs, számlázás, limitek kezelése | Legfeljebb technikai pilothoz vagy külön üzleti igényhez |
| MCP egy meglévő AI-klienshez | Saját szolgáltatási díj és a kliens feltételei szerinti AI-hozzáférés | A felhasználó AI-kliensből dolgozik | Edzői haladó funkciónak vagy saját prototípushoz jó |
| ChatGPT-csomag használata saját appban | Külön támogatott integráció és jogosultság kell | Potenciálisan kényelmes, de hozzáférésfüggő | Ne erre alapozd az induló üzleti modellt |

MCP esetén sem kötelező fogalmilag Codex: a választott kliensnek kell támogatnia a kapcsolatot. A kliensmodell költségét annak hozzáférési modellje viseli; a te háttérrendszered és az esetleges külön modellhívásaid ettől még költségesek. Az MCP önmagában nem indít időzített elemzést és nem ad modell-előfizetést. Az ütemezést a saját alkalmazásodnak vagy a kliens támogatott funkciójának kell biztosítania.

Az OpenAI aktuális dokumentációja már leír olyan Sign in with ChatGPT lehetőséget, amely nyílt forrású, helyben futó alkalmazásokban a felhasználó ChatGPT-csomagját használja jogosult kérésekhez. Fizetős vagy távolról hosztolt appokra külön érdeklődési folyamatot jelöl. Ezért nem pontos az, hogy előfizetéshez kapcsolódó használat soha nem lehetséges; viszont erre nem szabad általánosan hozzáférhető SaaS-alapként számítani. [Hivatalos áttekintés](https://developers.openai.com/siwc/token-sharing-open-source), [korlátozások](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations)

## 9. Technikai első verzió

Javasolt felépítés: telefonra optimalizált webfelület → Python háttérrendszer → PostgreSQL adatbázis, szabálymotor és AI-szolgáltatás. Az MCP később a háttérrendszer ellenőrzött műveleteit teheti elérhetővé. Ne legyen külön üzleti logika az MCP-ben és az alkalmazásban.

Pythonhoz a FastAPI/Pydantic ésszerű kiindulópont strukturált bemenetekkel; a végleges keretrendszer a tényleges jártasságodtól függjön. A Supabase egy lehetséges menedzselt PostgreSQL és hitelesítési megoldás, Pro csomagja jelenleg 25 USD/hótól indul. [FastAPI](https://fastapi.tiangolo.com/features/), [Supabase](https://supabase.com/pricing)

Az edzői első prototípushoz egyszerű webes űrlapok elegendők lehetnek. A sportolói változatnál fontosabb a gyors sorozatnaplózás, a nagy érintési célok és a megbízható mentés, mint a látványos chat. Az első pilotban legyen legalább helyi piszkozat és biztonságos újraküldés; teljes offline szinkron későbbi fejlesztés lehet. Natív iOS/Android alkalmazás az első validációhoz nem szükséges.

Minimum adatok: felhasználó és edző–sportoló jogosultság; sportolóprofil; gyakorlatkatalógus és változatok; tervverziók; tervezett edzések; elvégzett edzések és sorozatok; rövid állapotjelzések; módosítási események; javaslatok és jóváhagyások; AI-használati és döntési napló.

Az AI értelmezheti a természetes nyelvű kérést és megírhatja a magyarázatot. A számszerű tervet a szabálymotor állítsa elő vagy ellenőrizze. Típusellenőrzés mellett szükség van szakmai ellenőrzésekre is: attól, hogy egy válasz érvényes JSON, még lehet rossz edzésterv.

Egy módosítás folyamata: kérés → strukturált esemény → aktuális állapot betöltése → javaslat → szabályellenőrzés → előtte/utána nézet → jóváhagyás → új tervverzió. Régi tervverzióra érkező jóváhagyásnál újraellenőrzés kell; kétszer elküldött napló ne hozzon létre dupla edzést.

A befejezett edzéstörténetet egy új terv ne írja át. Az LLM ne kapjon szabad SQL- vagy adminisztrátori hozzáférést. Az API-kulcs a szerveren maradjon. Modellhiba esetén a naplózás és a már jóváhagyott terv továbbra is működjön.

### 9.1. Technológiai alternatívák és választási indokok

| Felépítés | Mikor jó választás? | Többletteher | Javaslat |
|---|---|---|---|
| Egyszerű Python webes prototípus | Saját használat, kézi felügyelet, belső döntési kísérlet | Később a mobilos napló és jogosultságok fejlesztése | Korai működési bizonyítékhoz |
| Django + PostgreSQL + egyszerű webfelület | Egy fejlesztő, sok adatkezelő képernyő, adminisztráció | Az API és a gazdag mobilos interakció külön kialakítása | Erős alternatíva Python-központú induláshoz |
| FastAPI + külön mobilbarát frontend + PostgreSQL | API-központú rendszer, későbbi MCP és többféle kliens | Két technológiai réteg, több összekapcsolási pont | Akkor választanám, ha a frontend is kezelhető számodra |
| Menedzselt adatbázis/hitelesítés + saját alkalmazás | Üzemeltetési feladatok egy részének átadása | Szolgáltatói költség, beállítások és jogosultságok helyes kezelése | Pilothoz praktikus lehet |
| Natív vagy közös mobilkódbázisú app | Bizonyított mobilos használat, indokolt eszközintegráció | Kiadási, áruházi és platformtesztelési munka | Megtartási bizonyíték után újraértékelendő |

A Django beépített adatmodell- és adminisztrációs lehetőségeket ad; ez csökkentheti egy egyfejlesztős adatkezelő alkalmazás kezdeti összerakási munkáját. Az adminfelület viszont nem kész sportolói termékfelület. A fenti választási értékelés saját következtetés a dokumentált képességekből. [Django áttekintés](https://docs.djangoproject.com/en/5.2/intro/overview/)

A FastAPI korábbi ajánlása tehát nem kizárólagos döntés. Két napos technikai próbában érdemes egy sportoló, egy terv és egy naplózott sorozat teljes útját elkészíteni a számodra ismerősebb megoldással. A könnyebben módosítható és hibakereshető változat fontosabb lehet, mint az elméletileg elegánsabb architektúra.

### 9.2. Adatmodell – mit miért kell külön tárolni?

| Entitás | Fontos adatok | Indok |
|---|---|---|
| Edző–sportoló kapcsolat | Szerep, jogosultság, kezdet/vég | Az adathozzáférés ne a kliens által megadott sportolóazonosítótól függjön |
| Sportolóprofil | Cél, elérhetőség, eszközök, tapasztalat | A tartós körülmények elkülönülnek egyetlen edzés megjegyzésétől |
| Gyakorlat és változat | Azonosító, végrehajtás, eszköz, kapcsolódó alternatívák | Elkerülhető az eltérő változatok összekeverése |
| Tervverzió | Blokk, cél, szerző, verzió, hatály | Visszakereshető, mi volt érvényes az adott edzéskor |
| Tervezett edzés/sorozat | Dátum, célismétlés, terhelés, cél-RPE | Önállóan elemezhető az előírás |
| Elvégzett edzés/sorozat | Valós időpont, súly, ismétlés, RPE, státusz | A tényleges munka nem vész el újratervezéskor |
| Állapotjelzés | Forrás, időpont, típus, érvényesség | A régi jelzést nem tekinti örökké aktuálisnak |
| Változtatási kérés | Ok, kívánt dátumok, érintett tervverzió | Később rekonstruálható a döntés kiváltó oka |
| Javaslat és döntés | Különbség, szabályverzió, elfogadó, szerkesztés oka | Mérhető a minőség és az edzői felülbírálat |
| Technikai futás | Modellverzió, időigény, tokenhasználat, hibakód | Megérthető a költség és a hibák eredete |

Az első import legyen dokumentált saját CSV-séma, mintaállománnyal és mezőellenőrzéssel. Az „akármilyen Excel/PDF tervet hibátlanul megérti” külön projekt: egy cellában lehet több gyakorlat, százalék, RPE, megjegyzés vagy képlet. Import után kötelező legyen az értelmezett terv előnézete. Az eredeti fájlhoz való visszahivatkozás segíthet hibakereséskor, a megőrzési szabályok keretein belül.

### 9.3. Az AI és a szabálymotor pontos feladatmegosztása

**Nyelvi feladatok:** a sportoló kérésének értelmezése, a hiányzó információ felismerése, edzői megjegyzések összefoglalása, a jóváhagyott módosítás magyarázata. **Számítási feladatok:** sorozatösszesítés, terhelésváltozás, időpontok, egységváltás, verziókezelés és szakmai korlátok ellenőrzése.

Az első verzióban a tervjavaslatok alapját az edző által jóváhagyott műveletek adják: áthelyezés, megengedett csere, megadott kereten belüli módosítás. A modell ezeket strukturáltan kérheti; az alkalmazás dönti el, végrehajthatók-e. A szabad szöveges napló tartalma adat, nem az alkalmazás jogosultságait módosító utasítás.

A strukturált modellkimenet segít a formai ellenőrzésben, de a hivatalos dokumentáció is jelzi, hogy továbbra is tartalmazhat tartalmi hibát. Ezért a sémaellenőrzés után üzleti és szakmai ellenőrzés szükséges. [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

Javasolt belső műveletek: `get_athlete_state`, `record_training_event`, `propose_plan_change`, `validate_plan_change`, `approve_plan_change`, `export_training_history`. Az elnevezések tervpéldák. A jóváhagyás legyen elkülönített jogosultságú művelet; az AI által készített javaslat ne hagyhassa jóvá önmagát.

### 9.4. Memória, keresés és modellcsere

Az edzéssorozatok és tervek strukturált adatbázis-lekérdezésből jöjjenek. Hosszabb edzői jegyzeteknél később dokumentumkeresés is indokolt lehet, de kezdetben a sportolóhoz rendelt rövid összefoglaló és a legutóbbi releváns események elegendőek lehetnek. A teljes élettörténet minden kérésbe küldése költséges és nehezebben ellenőrizhető.

Minden összefoglaló hivatkozzon az alapul szolgáló adat időpontjára. Az új, jóváhagyott információ felülírhat egy régi preferenciát, de a rendszernek tudnia kell, miért változott. Az egészségügyi korlátozások ne veszítsenek el érvényes feltételeket egy tömörítés során.

A modellhívást saját kis szolgáltatási réteg mögé tenném, hogy a szolgáltató vagy modell cseréje ne érintse a teljes terméket. Ez nem igényel több szolgáltatós működést az első napon. A kiválasztást saját magyar nyelvű esetkészlet, késleltetés, számlázott használat és hibaarány alapján kell elvégezni.

### 9.5. Jogosultság és üzemeltetés

Minden olvasás és írás szerveroldalon ellenőrizze a sportoló–edző kapcsolatot. A Supabase soralapú jogosultságkezelése segíthet, de az adminisztratív/service-role hozzáférés megkerülheti ezeket a szabályokat. A kulcs megfelelő elhelyezése önmagában nem elég: a háttérrendszer jogosultságait is tesztelni kell. [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security)

Szükséges üzemi viselkedések: duplán küldött esemény egyszeri feldolgozása; lejárt javaslat újraellenőrzése; időzóna és kg/lb egyértelmű kezelése; hálózathiba utáni mentési státusz; működő export; kipróbált adat-visszaállítás; modellhiba esetén a jóváhagyott terv elérhetősége.

A változásnapló megőrzése és a személyes adatok törlése nem jelenthet ellentmondást. Törléskor a személyes tartalmat és a kapcsolható azonosítókat a meghatározott rend szerint kell kezelni; a technikai események megmaradása csak megfelelő, személyhez nem kapcsolható vagy jogszerűen megőrzött formában indokolt.

## 10. AI-költség és árazás

Az alábbi példa rövid kontextusú standard szöveges használattal, kedvezmény nélkül számol. Feltételezés sportolónként: havi 60 kérés, kérésenként átlagosan 5000 bemeneti és 1000 számlázott kimeneti token; összesen 300 000 és 60 000 token. A kimeneti keretbe a számlázott gondolkodási tokeneket is bele kell számolni.

| Példamodell | Input/output USD / 1 millió token | Havi példaköltség | Ötszörös használat |
|---|---|---|---|
| GPT-6 Luna | 0,10 / 0,50 | 0,06 USD | 0,30 USD |
| GPT-6.1 Sol | 2 / 10 | 1,20 USD | 6 USD |

Ez kizárólag modellhasználat, nem teljes alkalmazásköltség és nem sporttudományi alkalmassági teszt. Az újrapróbálkozás, hosszabb kontextus, eszközök, más feldolgozási mód és további elemzések növelhetik a számlát. Modellválasztás előtt saját esetkészleten kell mérni a minőséget. [API-árazás](https://developers.openai.com/api/docs/pricing)

Az egyszerű naplóbevitelnél modellhívás sem feltétlenül kell. A szabálymotor, a tömör állapotösszefoglaló és a csak eseménykor végzett újratervezés csökkentheti a költséget. Legyen felhasználónkénti használatmérés, korlát és előre látható keret. A „korlátlan AI” induláskor rosszul tervezhető kötelezettség.

**Javasolt ártesztek, nem végleges árlista:**

| Ajánlat | Tesztár | Mit tartalmazzon? |
|---|---|---|
| Külső edzői, négyhetes pilot | 9900 Ft + alkalmazandó áfa, legfeljebb 10 sportoló | Bevezetés, korlátozott működő eszköz, rendszeres visszajelzés |
| Edzői alap | 14 900 Ft + alkalmazandó áfa / hó, 10 aktív sportolóig | Tervezés, napló, javaslatok, a sportolói hozzáférés benne van |
| Edzői nagyobb csomag | 24 900 Ft + alkalmazandó áfa / hó, 25 aktív sportolóig | Ugyanaz a munkafolyamat nagyobb kerettel; fedezetet külön mérni |
| Későbbi önálló sportolói termék | 3990 és 5990 Ft/hó bruttó árpont tesztelése | Adaptív terv és napló; személyes emberi coaching külön szolgáltatás |

A havi díj illik a folyamatos alkalmazkodáshoz. Éves csomagot megtartási tapasztalat után vezetnék be, például 10 havi díjért. Egyszeri díj sablonért vagy programért működhet; folyamatos AI-szolgáltatáshoz az élettartam-ajánlat korlátlan jövőbeli költséget vállalna. Az edző és a hozzá tartozó sportoló ugyanazért az alapfunkcióért ne fizessen kétszer.

Az árat az időnyereséghez is mérd. Például havi négy óra megtakarítás, 6000 Ft/óra feltételezett időértékkel 24 000 Ft értéket jelent. Ez számítási példa, nem állítás az edzők tényleges óradíjáról. Ha az eszköz csak tíz percet spórol, más az értékajánlat.

**Óvatos fedezeti példa:** 14 900 Ft havi nettó díj; edzőnként átlag 10 aktív sportoló; sportolónként 600 Ft változó technikai költségkeret; edzőnként 3000 Ft támogatási munka becsült értéke; havi 40 000 Ft fix technikai költség. Ezek saját tervezési feltételezések, nem szolgáltatói ajánlatok.

| Fizető edző | Havi nettó árbevétel | Maradék a fenti tételek után |
|---|---|---|
| 10 | 149 000 Ft | 19 000 Ft |
| 30 | 447 000 Ft | 137 000 Ft |
| 50 | 745 000 Ft | 255 000 Ft |

A maradékból még nincs levonva a fejlesztés, ügyfélszerzés, könyvelés, adózás, fizetési díjak és egyéb vállalkozási költség. Ez nem nyereség-előrejelzés. A példában a felsorolt tételek fedezéséhez legalább hét edző kell. Harminc ügyfél elvesztett vagy megnyert munkaideje is jelentős lehet. Az egységgazdaságot az aktív sportolók számán és a tényleges supportidőn kell ellenőrizni.

### 10.1. Melyik árazási egység illik a termékhez?

| Modell | Mi szól mellette? | Mi szól ellene? | Induló döntés |
|---|---|---|---|
| Havidíj sportolói kerettel | Tervezhető számla; az edző a kezelt ügyfélkörhöz köti az értéket | A teljes keretet kihasználó edző drágább lehet, mint az átlag | Ezt tesztelném elsőként |
| Díj minden aktív sportoló után | A költség és a bevétel együtt nőhet | Változó havi számla; pontosan definiálni kell az aktív státuszt | Későbbi túllépési díjhoz alkalmas |
| Korlátlan sportoló fix áron | Egyszerű ajánlat | A nagy ügyfelek támogatása és használata elviheti a fedezetet | Pilotban kerülendő |
| AI-kreditek vagy tokenek | A közvetlen modellköltséghez igazítható | Az edző nem tokenben gondolkodik; gátolhatja a hasznos használatot | Belső költségmérésnek jó, fő árazásnak gyenge |
| Éves előrefizetés | Korábbi pénzbevétel, kisebb havi fizetési súrlódás | Korai terméknél hosszú vállalás és visszatérítési kérdések | Csak bizonyított használat után |
| Egyszeri licenc | Könnyen érthető egyszeri vétel | A hosztolás, AI és támogatás folyamatos költség | Ehhez a szolgáltatáshoz nem javasolt |

Az aktív sportoló jelentését az ajánlatban kell rögzíteni: például olyan profil, amelynek az adott számlázási időszakban élő programja és naplózási hozzáférése van. Az archivált profil megőrzését és visszaaktiválását külön szabály kezeli. Az archiválás ne járjon adatvesztéssel, de a csomagkorlát se legyen félreérthető.

A 10 és 25 sportolós csomagot **ártesztként** kezelném. A próba tartalmazzon konkrét szolgáltatási leírást és fizetési lehetőséget. A „mennyit fizetnél?” kérdésnél erősebb bizonyíték az, hogy az edző a látott munkafolyamat után ténylegesen előfizet-e. A feltételek legyenek egyértelműek: pilotidőszak, keret, támogatás, lemondás, adat-hozzáférés a próba után.

### 10.2. Érzékenységvizsgálat: mikor működnek a javasolt árak?

Az alábbi saját számítás azt mutatja, mi történik **teljes sportolói keret kihasználásakor**. Mindkét csomagnál 3000 Ft/hó támogatási munkaértékkel számol; ez a nagyobb csomagnál optimista lehet. A sportolónkénti összeg technikai költségkeret, nem pusztán tokenköltség. A valós számot a pilot méri meg.

| Változó technikai költség / sportoló / hó | 14 900 Ft-os, 10 fős csomag havi hozzájárulása | 24 900 Ft-os, 25 fős csomag havi hozzájárulása | 40 000 Ft fix költséghez szükséges edzők, csak az adott csomagból |
|---|---|---|---|
| 200 Ft | 9900 Ft | 16 900 Ft | 5 / 3 |
| 600 Ft | 5900 Ft | 6900 Ft | 7 / 6 |
| 1200 Ft | −100 Ft | −8100 Ft | Egyik sem fedezi a fix költséget |

Képlet: **havi hozzájárulás = nettó csomagár − aktív sportolók × változó technikai költség − támogatási munka értéke**. A táblázatban a „hozzájárulás” a fix költségek előtt maradó összeg. Ez még nem számviteli eredmény.

Az alapforgatókönyvben a 25 fős csomag 15 további sportolóért csak 1000 Ft-tal nagyobb havi hozzájárulást ad. Ez jelzi, hogy a csomagkedvezmény túl nagy lehet. Lehetséges válasz a magasabb nagycsomagár, kisebb keret vagy sportolónkénti túllépési díj. Árat emelni viszont csak igazolt érték mellett érdemes; a költségalap önmagában nem bizonyít fizetési hajlandóságot.

Ha a 40 000 Ft fix költségen túl **havi 400 000 Ft alapítói munkakeretet** is szeretnél kitermelni, összesen 440 000 Ft hozzájárulás kellene. A 600 Ft-os alapforgatókönyvben ez 75 teljesen kihasznált kiscsomag vagy 64 nagycsomag. A 200 Ft-os forgatókönyvben 45, illetve 27. Ezek tisztán egyféle csomaggal számolt példák, nem értékesítési előrejelzések; adózás, ügyfélszerzés és több egyéb költség még hiányzik belőlük. A 400 000 Ft nem nettó fizetés. Az alapítói keret a már külön elszámolt támogatási munka mellett végzett termék- és üzleti munkára értendő, hogy ne számoljuk ugyanazt a munkaórát kétszer.

**Készpénz és munkaidő külön mérése:** ha te támogatod az ügyfeleket, a 3000 Ft becsült időérték lehet, nem ténylegesen kifizetett összeg. Ettől a munka még erőforrást köt le. A pénzügyi napló ezért mutassa a bankszámláról kimenő költséget és a ráfordított perceket is.

### 10.3. Ügyfélszerzés és megtartás hatása

Saját számpélda: ha egy fizető edző megszerzése a hirdetés, bemutató és értékesítési munka együtt számított értékével 30 000 Ft, akkor 5900 Ft havi hozzájárulással körülbelül **5,1 hónap** kell a megszerzés megtérüléséhez, még a fix költségek elosztása előtt. A korai lemondás ezt könnyen meghiúsíthatja. A személyes kapcsolaton keresztül szerzett ügyfél sem automatikusan ingyenes: a bemutató és a betanítás idejét is mérni kell.

Kezdetben kevés adatból ne számolj hosszú távú ügyfélértéket. Kövesd külön az indulási hónap szerinti csoportokat: hányan fizettek először, hányan aktívak a második és harmadik hónapban, miért mondanak le, és mennyi támogatást igényelnek. Az előfizetés megmaradása és a tényleges használat külön mutató; az éves előrefizetés például önmagában nem bizonyít heti használatot.

**Árazási döntés a pilot végén:** ha a felhasználók időt nyernek és fizetnek, de a támogatás sok, előbb a bevezetést és a termék érthetőségét javítsd. Ha kevés időt nyernek, az alacsonyabb ár nem biztos, hogy megmenti az ajánlatot. Ha csak a nagy ügyfelek veszteségesek, a csomagkeretet és a nagycsomag árát módosítsd, ne az egész terméket ítéld életképtelennek.

## 11. Adatok és a sérüléses funkció határa

A sérülésre és egészségi állapotra vonatkozó információ különleges védelmet igénylő egészségügyi adat lehet. A tervezésben tisztázni kell az edző és a szoftverszolgáltató adatkezelői/adatfeldolgozói szerepét, a jogalapot és az egészségügyi adatok kezelésének külön feltételét; a kifejezett hozzájárulás egy lehetséges feltétel, nem minden kötelezettséget helyettesítő megoldás. Szükséges az adatminimalizálás, jogosultságkezelés, megőrzési rend, export és törlési folyamat. [EU adatvédelmi tájékoztató](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm), [adatvédelmi alapelvek](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en)

A modellhez a feladathoz szükséges adat menjen, lehetőleg név és elérhetőség nélkül. A pszeudonimizálás nem teljes anonimizálás. Az OpenAI API alapértelmezés szerint nem használja modelltréningre a küldött adatokat, de ettől még lehet adatmegőrzés; a visszaélés-monitorozási naplók alapértelmezett ideje legfeljebb 30 nap, kivételekkel. A fogyasztói AI-kliens adatkezelését nem szabad automatikusan az API-éval azonosnak venni. [OpenAI adatkezelés](https://developers.openai.com/api/docs/guides/your-data)

Az első verzió célja edzéstervezési segítség legyen. Sérülésdiagnózis, rehabilitációs előírás vagy gyógyulási ígéret érdemben módosíthatja a termék szakmai és szabályozási helyzetét. Az EU-s szoftverbesorolásban a tényleges rendeltetés és az állítások is számítanak; egy felelősségkizáró mondat nem oldja meg ezt. [MDCG 2019-11 rev.1](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=md_mdcg_2019_11_guidance_qualification_classification_software_en.pdf)

### 11.1. Mit jelent ez konkrétan a pilotban?

Az alábbi lista saját terméktervezési munkacsomag, nem teljes jogi megfelelőségi audit:

1. Készíts adatleltárt: mely mező miért kell, ki látja, meddig őrzöd, és melyik szolgáltatóhoz kerül. A szabad szöveges megjegyzésbe is kerülhet egészségi adat.
2. Az edző csak a hozzá rendelt sportoló adataihoz férjen hozzá. A hozzárendelés megszűnésének legyen tesztelt folyamata; a sportoló saját hozzáférése külön kezelendő.
3. Teszteld az exportot és törlést a naplókra, AI-összefoglalókra és mentési rendre is. A törlés feltételeit és esetleges megőrzési kötelezettségeit előre tisztázd.
4. A rendszerfejlesztési tesztekhez elsőként szintetikus vagy megfelelően előkészített adatot használj. Valós történetek átvétele előtt rendezd a felhasználásuk feltételeit.
5. Legyen ténylegesen kipróbált adatmentés, visszaállítás és incidenskezelési elérhetőség. A mentés megléte nem bizonyítja, hogy helyreállítható.
6. Az edzéstámogatás célú adatkezelést és a későbbi, felhasználókon átívelő modellfejlesztést kezeld külön. Az egyikből ne következzen automatikusan a másik.

### 11.2. AI-átláthatóság és termékígéret

Az Európai Bizottság tájékoztatója szerint az AI Act 50. cikkének átláthatósági szabályai 2026. augusztus 2-től alkalmazandók. Többek között a közvetlen AI-interakcióról való tájékoztatást érintik; a pontos kötelezettség a szereptől, felhasználástól és kivételektől függ. Ez nem jelenti azt, hogy minden edzésapp automatikusan magas kockázatú rendszer. [Bizottsági iránymutatás](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)

Saját termékjavaslat: a felületen külön állapot legyen az „AI-javaslat”, az „edző által módosított” és az „edző által jóváhagyott” terv. A jóváhagyó személy és időpont a tényleges műveletből származzon. A sportolóval kommunikáló AI ne keltsen olyan benyomást, hogy az üzenetet az edző személyesen írta. A jóváhagyás nélküli vázlat ne jelenjen meg végleges edzésutasításként.

A sérüléses helyzetekre az első verzió vállalható ígérete: rögzíti a jelzést, korlátozza az automatikus módosítást, és az edzőhöz irányítja az esetet. Ennek megvalósítása nem ugyanaz a fejlesztési feladat, mint diagnózis vagy rehabilitációs program készítése. A külső pilot előtt a tényleges funkciók és termékállítások alapján érdemes célzott adatvédelmi és besorolási felülvizsgálatot kérni.

## 12. Megvalósítási ütem és költségkeret

### 12.1. Részletes munkabontás

A külső edzőkkel használható, szűk pilot becsült munkaigénye **240–400 fókuszált óra**, ha az alap Python-fejlesztési eszközöket már használod. A korábbi 160–280 órás becslést a részletes munkabontás alapján módosítom: a bevezetés, az értékelés és az üzemeltetési feladatok több munkát jelentenek. Az alacsonyabb tartomány inkább erősen szűkített belső prototípushoz lehet elég. Ez saját tervezési becslés, nem külső fejlesztői árajánlat.

| Munkacsomag | Kézzelfogható eredmény | Becsült óra |
|---|---|---|
| Problémafeltárás | Interjújegyzetek, mért alapfolyamat, pilotajánlat | 16–24 |
| Szakmai szabályok | Döntési feltételek, tiltások, referenciaesetek | 24–40 |
| Adatmodell és hozzáférés | Verziózott tervek, napló, edző–sportoló jogosultság | 24–40 |
| Backend és AI-folyamat | Eseményfeldolgozás, szabályellenőrzés, javaslat és jóváhagyás | 32–56 |
| Egyszerű mobilbarát felület | Naplózás, edzői áttekintés, módosítások megjelenítése | 40–64 |
| Értékelés és hibajavítás | Szakmai tesztkészlet, jogosultság és hibakezelés ellenőrzése | 24–40 |
| Üzembe helyezés | Naplózás, költségkorlát, mentés, visszaállítás, alapfolyamatok | 16–24 |
| Pilot támogatása | Betanítás, mérések, interjúk, kisebb javítások | 24–32 |
| **Részösszeg** |  | **200–320** |
| **20% tartalékkal** |  | **240–384; tervezéshez kerekítve 240–400** |

Feltételezés: egy fejlesztő, egy egyszerű importformátum, néhány ismert edzéssablon, mobilbarát webfelület és kézi pilotértékesítés. A becslés nem tartalmaz natív mobilappokat, videófeldolgozást, teljes fizetési/számlázási integrációt, minden konkurensből automatikus importot vagy hosszabb szakmai hatásossági vizsgálatot. Külső szakértői felülvizsgálat és szerződéses munka ideje külön egyeztetendő.

### 12.2. Heti kapacitás és ütemezés

Az első szakasz részletes feladatai, órakeretei és elfogadási feltételei külön dokumentumban olvashatók, mellékprojekt-tempóra (heti 10 + 2 óra) és a költözéshez igazítva: [Az első szakasz ütemterve](elso_szakasz_utemterv.md).

| Rendelkezésre álló idő | Becsült munkaidőből adódó időtáv a pilot lezárásáig |
|---|---|
| Heti 8 óra | 30–50 hét |
| Heti 15 óra | 16–27 hét |
| Heti 25 óra | 10–16 hét |

Ezek kapacitással osztott becslések. A tesztelők elérhetősége, technológiatanulás és külső felülvizsgálat hosszabbíthatja a naptári időt. A négyhetes pilotnak valóban négy hétig kell futnia, akkor is, ha a fejlesztés gyorsabb. Az alábbi **16 hetes mintaütemezés heti körülbelül 25 órával** tervez; kisebb kapacitásnál ugyanazok a kapuk hosszabb idő alatt teljesülnek.

1. **1–2. hét:** 6 edzői és 6 sportolói interjú; konkrét közelmúltbeli módosítások; időmérés; első fizetési hajlandósági teszt. Többségük ne kizárólag saját ügyfél legyen.
2. **3–4. hét:** felügyelt kézi próba; közös adatséma; néhány saját vagy engedéllyel átadott terv; 30–50 tipikus és szélsőséges esetből tesztkészlet. Először bizonyítsd, hogy a döntési logika hasznos.
3. **5–10. hét:** napló, egyszerű import/export, edzői áttekintés, kimaradás/áthelyezés/napváltás/gyakorlatcsere, módosítási nézet és jóváhagyás. Kezdetben kevés jól ismert programozási sablon. A negyedik funkciót el lehet hagyni, ha az első három még nem megbízható.
4. **11–12. hét:** kis körös belső használat; szakmai és jogosultsági ellenőrzés; idő- és költségmérés; adatmentés és visszaállítás kipróbálása. Sikertelen kritikus ellenőrzés esetén a külső indulás halasztandó.
5. **13–16. hét:** négyhetes fizetős külső pilot, heti visszajelzés és folytatási döntés. A hathetes megtartási megfigyelés, ha szükséges, a 18. hétig tart.

### 12.3. Mire költs először?

**Költségforgatókönyvek saját munkával:** az interjús/kézi validációhoz 0–30 ezer Ft többletkeret lehet elég meglévő eszközökkel. Egy kis hosztolt pilot technikai működésére kezdetben 15–50 ezer Ft/hó keretet terveznék, használattól függően. Háromhavi technikai tartalék így 45–150 ezer Ft. Ezek becslések, nem teljes vállalkozásindítási költségek; jogi, könyvelői, biztonsági vagy külső fejlesztői munkára külön ajánlat kell. A saját munkaidő gazdasági értéke várhatóan lényegesen nagyobb a szerverköltségnél.

Az egyes szakaszokhoz külön költési döntés tartozzon:

| Szakasz | Milyen bizonyíték után lépj tovább? | Mire indokolt költeni? |
|---|---|---|
| Interjú és kézi próba | Több edző ugyanazt a konkrét problémát mutatja | Interjú, munkafolyamat dokumentálása, egyszerű bemutató |
| Belső prototípus | A kézi támogatással megoldott folyamat mérhetően hasznos | Minimális adatbázis, felület, AI-kísérletek |
| Külső fizetős pilot | Van vállalt részvétel, tisztázott adatkezelés és működő ellenőrzés | Stabil hosztolás, mentés, célzott szakértői ellenőrzés |
| Bővítés | Használat, fizetős folytatás és elfogadható ügyfélenkénti költség | Jobb betanítás, megbízhatóság, keresett integrációk |

A kis technikai költség nem jelenti, hogy a projekt olcsó a saját idődhöz képest. Például 300 óra, feltételezett 5000 Ft/óra alternatív munkaértékkel 1,5 millió Ft gazdasági ráfordítás. Ez nem kifizetendő számla vagy állítás a tényleges óradíjadról, hanem a döntéshez hasznos összehasonlítás.

## 13. A validáció kérdései és döntési kapui

Interjúban ne azzal kezdj, hogy „használnál-e AI-appot?”. Kérj konkrét történetet: mikor borult fel utoljára a terv, mit módosított, hány perc alatt, milyen adatokból, mit nem adna át egy rendszernek. Kérd meg, hogy mutassa meg a jelenlegi munkafolyamatot, és azonosítson egyetlen visszatérő drága problémát.

Ajánlott pilotcélok, saját döntési küszöbként:

- Legalább három, tőled független edző ténylegesen fizet a kipróbálásért. A saját ügyfelek elégedettsége nem helyettesíti ezt.
- Az összes ellenőrzési és javítási időt beleszámolva legalább 30%-kal rövidebb a kiválasztott módosítási folyamat, több alkalom mediánjában.
- A javaslatok legalább 80%-a lényegi szakmai átírás nélkül használható. Ez működési cél, nem klinikai minőségmutató.
- Négy–hat hét után a bevont edzők többsége heti rendszerességgel használja, és legalább három vállal fizetős folytatást.
- A sportolók tényleges edzéseinek legalább 70%-a naplózott, amennyire ez a pilotban ellenőrizhető. Alacsony adatminőségnél előbb a naplózást javítsd.
- Minden előre rögzített kritikus teszteset sikeres; nincs idegen sportoló adatához hozzáférés vagy ellenőrizetlen, tiltott módosítás. Ez szükséges, de nem bizonyítja minden jövőbeli hiba kizárását.

Ha az edzők értékelik az összefoglalókat, de elutasítják a tervmódosítást, szűkíts az elemzésre. Ha az adatbevitel elmarad, egyszerűsítsd a felületet. Ha csak a saját ügyfeleid használják, az eszköz maradhat értékes belső coachingsegéd, de a külön szoftverüzlet még nincs igazolva. Ha a javaslatok ellenőrzése több munka, mint a kézi tervezés, ne skálázd az automatizálást.

Erőnövekedésre és sérüléskockázatra vonatkozó hatásossági állításokhoz hosszabb követés és megfelelő vizsgálat kell; a kis pilot elsődlegesen használhatóságot, folyamatminőséget és fizetési hajlandóságot mérjen.

### 13.1. Interjúterv: viselkedést vizsgálj, ne udvarias érdeklődést

Javasolt edzői interjú, 30–40 perc:

1. Hány sportolóval dolgozik, milyen eszközökkel, és milyen gyakran ír át programot?
2. Mutassa meg a legutóbbi konkrét esetet, amikor kimaradás, változó edzésnap vagy gyakorlatcsere miatt módosított. Személyes adatok megmutatása nem szükséges.
3. Milyen információt keresett vissza, és mi volt a döntés legnehezebb része?
4. Mennyi idő a módosítás, az ellenőrzés és a sportoló tájékoztatása együtt?
5. Milyen hibát nem fogadna el akkor sem, ha a rendszer gyorsabb?
6. Melyik jelenlegi eszközéhez ragaszkodik, és mitől lenne elfogadható egy új felület?
7. Egy konkrét bemutató után vállalna-e fizetős, időben behatárolt pilotot a megadott feltételekkel?

Sportolói interjúban a naplózás legyen központi: mikor írja be az adatot, mit hagy ki, mi történik gyenge internetnél, és hogyan jelzi a terv változását. Az edző vásárlási szándéka kevés, ha a sportoló nem tudja rendszeresen használni az eszközt.

A mintába kerüljön eltérő ügyfélszámú edző, táblázatot használó és meglévő coachingappért fizető személy. A hat edző és hat sportoló kezdő feltáró minta; nem reprezentatív kutatás. Rögzítsd a visszautasításokat és azokat az eseteket is, ahol a probléma ritka vagy jelentéktelen. Ezzel csökkenthető, hogy csak az ötletet támogató történeteket gyűjtsd.

### 13.2. Milyen legyen a szakmai tesztkészlet?

Induló javaslat **50 verziózott eset**, többféle sportolóval és edzői módszerrel. Ez a minimum működési ellenőrzés kiindulópontja, nem a rendszer teljes megbízhatóságának igazolása. Egy lehetséges felosztás:

| Esetcsalád | Darab | Mit kell ellenőrizni? |
|---|---|---|
| Áthelyezés és kimaradás | 10 | Csak jövőbeli munka változik, nincs túlzsúfolás vagy duplázás |
| Gyakoriság és időkeret | 8 | A rendelkezésre álló napok és percek ténylegesen teljesülnek |
| Részleges teljesítés | 6 | Az elvégzett sorozatok nem ismétlődnek automatikusan |
| Gyakorlatcsere | 8 | Ok, felszerelés és edzői engedély alapján történik |
| Hiányzó vagy ellentmondó adat | 6 | A rendszer tisztáz vagy tartózkodik a módosítástól |
| Fájdalom és korlátozás | 6 | A tiltott automatikus döntés blokkolva marad |
| Verzióütközés és hozzáférés | 6 | Nincs elavult jóváhagyás vagy idegen adathoz hozzáférés |
| **Összesen** | **50** |  |

Egy eset tartalmazza a kiinduló tervet, tényleges naplót, változtatási kérést, engedélyezett és tiltott kimeneteket, valamint az értékelési indokot. Több szakmailag megfelelő válasz is lehet; egyetlen mintaszöveg szó szerinti követése gyenge minőségmérés.

A készletből például 35 eset szolgálhat fejlesztésre, 15 elkülönített ellenőrzésre. Ugyanannak az esetnek az apró átfogalmazásai ne kerüljenek mindkét halmazba. A kritikus jogosultsági és tiltási szabályokat ezen felül külön, minden kiadásnál futó tesztekkel is vizsgáld. A hibákból keletkező új esetek bővítsék a regressziós készletet; idővel új, korábban nem látott ellenőrző esetek is kellenek.

A generatív modellek változó kimenete miatt a fontos eseteket több futással is értékeld, és a legsúlyosabb hibát se tüntesd el egy átlagban. Az OpenAI értékelési útmutatója feladatspecifikus, folyamatos értékelést és emberi ellenőrzéshez igazított minősítést javasol. A konkrét fenti esetfelosztás saját javaslat. [Értékelési alapelvek](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

Kezdetben saját, egyszerű Python-alapú tesztfuttató és verziózott esetfájlok elegendők. A szakmai döntést ember minősítse; az automatikus ellenőrzés a számokat, korlátokat és jogosultságokat vizsgálja. Második edző legalább az elkülönített eseteket és a vitás döntéseket nézze át, hogy ne kizárólag a saját preferenciáidhoz illeszkedést mérd.

### 13.3. Hogyan mérd az időnyereséget és az elfogadhatóságot?

Rögzítsd előre a kezdő- és végpontot. A mérés a kérés megnyitásától az ellenőrzött, kiadható tervig tartson; az AI-ra várakozás, javítás és magyarázatírás is beleszámít. A gyors generálás önmagában nem a teljes munkafolyamat gyorsulása.

Az induló összehasonlításhoz minden edző végezzen néhány hasonló nehézségű esetet saját megszokott eszközzel és az asszisztenssel. Váltogasd a sorrendet; ugyanazon eset ismétlésekor a tanulási hatást külön kezeld. Ez kis használhatósági vizsgálat, nem szigorú hatásossági kísérlet. Edzőnként és esetcsaládonként mutasd az időket, ne csak az összevont átlagot.

Példa: 10 perc kézi munka helyett 7 perc teljes asszisztált munka 30% időmegtakarítás. Ha a generálás egy perc, de az ellenőrzés és javítás tíz, a folyamat összességében lassult.

Javasolt minősítési kategóriák:

- **Elfogadható:** szakmai változtatás nélkül kiadható; apró megfogalmazási javítás megengedett.
- **Javítandó:** érdemi terhelés-, sorrend-, gyakorlat- vagy ütemezési változtatás kell.
- **Elutasított:** a javaslat nem oldja meg a kérést vagy újratervezést igényel.
- **Kritikus hiba:** jogosultságot, kifejezett tiltást vagy más előre meghatározott biztonsági feltételt sért.

A 80%-os elfogadhatósági cél az első kategória aránya az összes, előzetesen a támogatott körbe sorolt kérésből. A hibás vagy hiányzó javaslatot ne hagyd ki a nevezőből. A tisztázást igénylő és eleve kizárt helyzeteket külön kövesd. Kritikus hiba esetén a százalékos cél teljesülése nem elég az induláshoz.

### 13.4. Pilotmérési lap és döntés

| Mutató | Operatív meghatározás | Miért kell? |
|---|---|---|
| Aktivált edző | Legalább egy programot betöltött, sportolót kapcsolt hozzá és végigvitt egy módosítást | A regisztráció gyenge bizonyíték |
| Heti aktív edző | Az adott héten érdemi áttekintést vagy módosítási munkát végzett | A háttérben megnyíló oldal ne számítson használatnak |
| Naplózási arány | Rögzített tényleges edzések / az egyeztetés alapján ténylegesen elvégzett edzések | A tervezett edzésszám más nevező, kihagyáskor torzít |
| Módosítás teljes ideje | Kéréstől a kiadható tervig eltelt munka és várakozás | Az ellenőrzési teher is számít |
| Elfogadási arány | Lényegi szakmai javítás nélküli javaslatok / támogatott kérések | A szakmai használhatóságot méri |
| Költség | AI, hosztolás és támogatási percek, edzőnként | Kimutatja a költséges ügyfeleket és folyamatokat |
| Fizetős folytatás | Tényleges megújítás vagy konkrét fizetett következő időszak | Elkülöníti a szándékot a vásárlástól |

Az újratervezési események ritkák is lehetnek. Ha a négyhetes pilotban csak néhány fordul elő, ne állíts megbízható elfogadási százalékot. Hosszabbítsd a megfigyelést vagy egészítsd ki felügyelt, előre elkészített esetekkel; a szimulált és az éles használati adatot tartsd külön.

**Folytatás:** több külső edző fizet, időt nyer, visszatér, és a költség kezelhető. **Szűkítés:** csak bizonyos esetekben hasznos; ezekre koncentrálj. **Belső eszközzé alakítás:** neked értékes, külső kereslet nem igazolt. **Leállítás vagy új célcsoport:** nincs visszatérő probléma, nincs fizetési hajlandóság, vagy az ellenőrzés tartósan több munka, mint a megoldás.

## 14. Konkrét első munkacsomag

A következő vállalható eredmény egyetlen teljes munkafolyamat: meglévő négynapos terv → kimaradt edzés és új elérhetőség → ellenőrizhető javaslat → edzői jóváhagyás → friss terv → tényleges napló. Ehhez 2–3 edzői példa, 5–10 sportolónyi pilotadat és jól meghatározott szabályok elegendőbbek, mint egy nagy általános funkciólista.

Az első verzióból elhagynám a közösségi feedet, étrendtervezést, viselhető eszközöket, videós technikaértékelést, saját modellt, edzői piacteret és teljesen önálló sérüléskezelést. Ezek közül egyik sem szükséges annak ellenőrzéséhez, hogy a kiválasztott tervmódosítási folyamatért fizetnek-e.

A hároméves edzői tapasztalatoddal és az elérhető technikai előzmények alapján a leginkább indokolható következő lépés egy saját szakmai logikádra épülő, ember által felügyelt pilot. A vállalkozási döntést az első külső fizető edzők, a megtakarított idő és a használatból mért költség alapján érdemes meghozni.

## 15. Döntési és kockázati nyilvántartás

Az alábbiak tervezési kockázatok; bekövetkezési valószínűségükre még nincs mért adat. A cél az, hogy előre meghatározzuk, mely eredmény változtatná meg a tervet.

| Feltevés vagy döntés | Fő kockázat | Mit figyelj? | Mikor változtass? |
|---|---|---|---|
| Az edző a legjobb első vevő | Nehezen elérhető, ragaszkodik a jelenlegi eszközéhez | Interjú, bemutatóból pilot, fizetős folytatás | Ha több releváns interjú után sincs fizető érdeklődő, vizsgáld újra a problémát és az elérést |
| A tervmódosítás gyakori probléma | A funkció túl ritkán szükséges | Valós módosítások száma és ideje | Ha ritka, az összefoglalás vagy adminisztráció lehet jobb belépő |
| A tervmódosítás sok időt visz el (**kritikus, nem mért**) | Független adat nincs; csak szolgáltatói állítás | Percben mért módosítási idő edzőnként | Ha a jelenlegi kézi módosítás néhány perc, az időnyereség nem lehet fő érv |
| Létező megoldáshoz képest megkülönböztethető | Közeli konkurens (pl. Kaizer) jól kezeli az erőemelő eseteket is | Azonos esetekkel végzett versenytársteszt (3.3–3.4.) | Ha nincs érdemi különbség, szűkíts vagy válts összefoglaló jellegű termékre |
| A sportoló naplóz | Túl sok adatbeviteli teher | Tényleges edzések naplózása, hiányzó mezők | Alacsony naplózásnál csökkents mezőt, lépést és várakozást |
| Az edzői ellenőrzés gyors | Minden javaslatot újra kell gondolni | Teljes ellenőrzési és javítási idő | Ha nincs időnyereség, szűkíts a jól ellenőrizhető műveletekre |
| Az AI megbízhatóan értelmez | Félreértés vagy kitalált indok | Elkülönített esetkészlet, kritikus hibák | A problémás eseteket tereld strukturált űrlapra vagy emberhez |
| A csomagár fedezi a szolgáltatást | Sok sportoló és támogatás elviszi a fedezetet | Költség eloszlása, nagy felhasználók | A pilotban mért használat alapján változtass keretet és árat |
| Egy fejlesztő fenntarthatóan üzemeltet | Javítás és támogatás kiszorítja a fejlesztést | Heti időbontás és hibák ismétlődése | Előbb egyszerűsíts és stabilizálj, csak utána adj funkciót |
| A szakmai módszer átadható | Más edzők eltérő elvek szerint dolgoznak | Elutasítások okai, edzők közötti eltérés | Válaszd külön a kötelező korlátot és a konfigurálható preferenciát |
| A szolgáltatói integráció tartós | Modell, ár vagy hozzáférés változik | Kiadási változások és saját teszteredmények | Modellcsere csak újraértékelés után; naplózás AI nélkül is működjön |

### 15.1. Mely döntések legyenek könnyen visszafordíthatók?

Az első modell, a csomagár, a pilot létszáma és a támogatott esetek köre módosítható. Ezeket ne építsd túl mereven a rendszerbe. Az adatstruktúra, tervverziók, jogosultságok és a tényleges edzéstörténet helyes kezelése tartós alap; ezeken a kezdeti gyorsítás később drága lehet.

Saját prioritás: először megbízható adatrögzítés és felülvizsgálható javaslat, utána kényelmi automatizálás. Ebből következik az is, hogy a sportoló adata ne függjön egy adott modell beszélgetési memóriájától.

### 15.2. Mi jelenthet tartós versenyelőnyt?

Az AI-modellhez való hozzáférés más fejlesztőknek is elérhető. Tartósabb előny lehet a jó naplózási élmény, az edzők által megértett és elfogadott döntési logika, a valós hibákból bővített esetkészlet, a bevezetés egyszerűsége és a szakmai bizalom. Ezek a használat során épülnek, és külön munkát igényelnek.

Ezt egy 2025-ös pilotvizsgálat is alátámasztja. A nyilvános összefoglaló szerint a strukturált tervvel edző szabadidős sportolók negyede AI által generált tervet használt. A tapasztalt edzők gyakran nem tudták megkülönböztetni az AI-val és az ember által írt terveket. A vizsgálat kis mintás és előzetes jellegű, a teljes szöveget nem értem el. Saját következtetésem: egy elfogadható edzésterv generálása már alacsony belépési korlát, ezért az előny a munkafolyamatban, az edzői kontrollban és az adatminőségben lehet, nem a tervgenerálásban. [Wachholz és mtsai., 2025](https://pubmed.ncbi.nlm.nih.gov/40082991/)

Az összegyűjtött adatmennyiség önmagában nem előny. Következetlen RPE, hiányzó sorozatok és dokumentálatlan gyakorlatcserék mellett több adat több zajt is jelenthet. A felhasználók feletti nagyobb kontroll vagy az export megnehezítése helyett a jobb eredmény és a kisebb munkateher tartsa meg az ügyfelet.

## 16. Indulási terv és nyitott kutatási kérdések

### 16.1. Az első két hét kézzelfogható eredménye

Az alábbi sorrend heti körülbelül 15–25 óra rendelkezésre álló időt feltételez. Ha kevesebb időd van, a sorrend maradjon, a naptár nyúljon.

| Lépés | Elkészülő anyag | Döntési haszon |
|---|---|---|
| 1. Nap: célhelyzet | Egyoldalas leírás: kinek, milyen változáskor, milyen eredményt ad az app | Nem csúszik szét általános fitneszplatformmá |
| 2–3. nap: saját esetek | 10 valós módosítás leírása, azonosítható személyes adatok nélkül | Kiderül, milyen döntések ismétlődnek |
| 3–7. nap: külső interjúk | Legalább 4 edzői és 4 sportolói interjú; további időpontok | Ellenőrizhető, másoknál is létezik-e a probléma |
| 5–8. nap: folyamatmérés | Néhány felügyelt eset kézi megoldással, időméréssel | Lesz összehasonlítási alap |
| 8–10. nap: bemutató | Egy végigkövethető tervváltoztatási példa, akár kézi háttérmunkával | A felhasználó a konkrét értékre reagál |
| 10–12. nap: műszaki próba | Egy sportoló, egy terv és egy sorozat teljes útja | Felmérhető a tényleges technológiai nehézség |
| 12–14. nap: ajánlat és döntés | Rögzített pilotfeltételek, vállalt részvétel, folytatás vagy szűkítés | Elkerülhető a bizonyíték nélküli hosszú fejlesztés |

A két hét végén még nem szükséges kész nyilvános alkalmazás. A fontos eredmény az ellenőrzött probléma, a kipróbált munkafolyamat és a következő ráfordítás indoka. Ha nincs érdeklődés, dokumentáld, hogy a probléma, a megoldás, az ár vagy az elérés miatt nincs.

### 16.2. Milyen kutatás hiányzik még a biztosabb döntéshez?

| Nyitott kérdés | Miért nem válaszolja meg a jelen kutatás? | Következő bizonyíték |
|---|---|---|
| Fizetnének-e ezért magyar edzők? | Külföldi listaár nem magyar kereslet | Konkrét fizetős pilotajánlat és vásárlás |
| Mennyi időt visz el ma egy tervmódosítás? | Csak szolgáltatói, általános adminisztrációs becslés található | Percben mért esetek interjúkban és kézi próbában |
| Hány elérhető magyar erőemelő edző van? | Nyilvános szövetségi létszám- és edzőszám-adatot nem találtam | A 4.2. fejezet szerinti saját lista |
| Jobb-e a kiválasztott folyamat a konkurenseknél? | Nyilvános funkcióleírásból nem mérhető használhatóság | A 3.3. fejezet azonos esetekkel végzett gyakorlati tesztje |
| Elég gyakori-e az újratervezés? | Nincs valódi használati eseményszám | Négy–hat hét megfigyelés több edzőnél |
| Mekkora a fejlesztési tanulási igényed? | A közös projektelőzmény nem teljes kompetenciafelmérés | A kétnapos teljes folyamatpróba eredménye |
| Melyik modell elég jó? | Az API árlista csak költséget mutat | Ugyanazon magyar esetkészleten mért minőség és teljes költség |
| Mely felhasználók maradnak meg? | Nagy aggregált előfizetéses jelentésből nem vezethető le a saját megtartás | Többhavi, indulási csoportok szerinti saját adat |
| Javítja-e a sportteljesítményt? | A hivatkozott edzéskutatások nem ezt az alkalmazást vizsgálták | Hosszabb követés, megfelelő összehasonlítás és vizsgálati terv |

### 16.3. Feltételes döntés a te helyzetedre

**Ha van heti 15–25 órád és elérsz néhány külső edzőt:** indokolható egy szűk, edzői asszisztens pilotjának felépítése. A három év szakmai tapasztalatodat döntési esetekben, szabályokban és személyes bevezetésben hasznosítsd.

**Ha heti legfeljebb 5–8 órád van:** először saját edzői eszköz, kézi import és egy-két jól meghatározott módosítási helyzet legyen a cél. A teljes külső szolgáltatás hosszú ideig elhúzódhat; az első hasznos eredményt kisebb munkacsomagból érdemes megszerezni.

**Ha nincs külső tesztelői hozzáférés:** előbb az elérést validáld. A piac felé vezető csatorna hiánya olyan bizonytalanság, amelyet további programozás nem old meg.

**Ha erős közvetlen sportolói közösséged van, de az edzők nem érdeklődnek:** újraértékelhető az önálló sportolói célcsoport, szűk szakmai felhasználásra és külön minőségbiztosítással. Ebben az esetben a felügyelet, a felhasználói támogatás és a közvetlen ügyfélszerzés gazdaságosságát újra kell tervezni.

A jelenlegi bizonyítékok alapján a vállalható első cél: **néhány külső edző által fizetve használt, mérhetően időt megtakarító módosítási asszisztens**. Az önálló AI-edző ennek későbbi, külön bizonyítékot igénylő termékiránya lehet.

## 17. Forrásjegyzék és forráskritika

Az alábbiak az anyagban hivatkozott fő források, 2026. október 16-i ellenőrzéssel. A csoportosítás a felhasználásukat mutatja. A közvetlen forráslinkek az érintett állítások mellett is megtalálhatók. Az árakat és platformfeltételeket tényleges fejlesztési vagy beszerzési döntéskor újra kell ellenőrizni.

### 17.1. Versenytársak – hivatalos ajánlatok

| Forrás | Mire használtam? | Korlát |
|---|---|---|
| [JuggernautAI árlista](https://www.juggernautai.app/pricing) | Erőemelő fogyasztói ajánlat és listaár | Szolgáltatói állítás; kampányár eltérhet |
| [Sheiko Gold](https://sheikogold.com/) és [US App Store](https://apps.apple.com/us/app/sheiko-gold-powerlifting-ai/id1475890027) | Adaptív funkciók és havi ár | Az éves árhoz eltérő adat szerepelt |
| [Fitbod FAQ](https://fitbod.me/faqs/) | Személyre szabás és webes árazás | Értékesítési csatornánként eltérhet |
| [Boostcamp Pro](https://www.boostcamp.app/pro) | Ingyenes/fizetős alternatíva | Nem termékminőségi teszt |
| [TrainHeroic Coach](https://www.trainheroic.com/coach/) | Sportolói keretek és havidíjak | Funkció- és csomagkülönbségek számítanak |
| [MyStrengthBook](https://mystrengthbook.com/pricing-coaching) | Edzői üzleti modell | PULL és PUSH eltérő ajánlat |
| [Everfit árazás](https://everfit.io/pricing/) és [AI Workout Builder](https://help.everfit.io/en/articles/9373485-introducing-ai-workout-builder) | Edzői platform és AI-funkció | Az AI-funkció nem igazolt autonóm edző |
| [RTS Training Lab](https://rtslab.reactivetrainingsystems.com/) | Erőemelő edzői összehasonlítás | Nem független hatásossági bizonyíték |
| [Kaizer összehasonlító cikk](https://kaizer.app/en/blogs/best-personal-trainer-software-2026) | Legközelebbi talált konkurens; más platformok AI-funkcióiról szóló állítások | Saját marketinganyag; konkurensekről szóló állításai ellenőrizendők |
| [Trainerfu](https://www.trainerfu.com/blog/everfit_alternatives/), [Everfit blog](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach), [Coaching Portal](https://coachingportal.io/blog/ai-fitness-coaching-trends) | Edzői platformok AI-funkciói, jóváhagyási gyakorlat | Harmadik fél vagy konkurens által írt anyag |

### 17.2. Piaci és sporttudományi háttér

| Forrás | Kapcsolódó kérdés | Fontos korlát |
|---|---|---|
| [RevenueCat: State of Subscription Apps](https://www.revenuecat.com/state-of-subscription-apps) | AI-appok megtartása és előfizetéses környezet | A vizsgált platformmintából nem következik a saját termék eredménye |
| [Helms és mtsai., 2018](https://pubmed.ncbi.nlm.nih.gov/29628895/) | RPE- és százalékalapú terhelés | Kis minta, rövid időtáv |
| [Saric és mtsai., 2019](https://pubmed.ncbi.nlm.nih.gov/30363041/) | Gyakoriság azonos volumen mellett | Nem általános szabály minden gyakoriságváltásra |
| [Remmert és mtsai., 2023 – RIR-pontosság](https://pubmed.ncbi.nlm.nih.gov/37036795/) | RIR mint bemeneti adat | Vizsgált gyakorlatok és körülmények korlátozzák az általánosítást |
| [Remmert és mtsai., 2023 – hathetes vizsgálat](https://journals.sagepub.com/doi/10.1177/00315125231189098) | A becslési pontosság fejlődése | Nagyon kis minta; nyilvános absztrakt |
| [Refalo és mtsai., 2023](https://link.springer.com/article/10.1186/s40798-023-00554-y) | Bukáshoz való közelség és akut fáradás | Akut vizsgálat, nem hosszú távú sérüléskutatás |
| [Martikainen és mtsai., 2025](https://link.springer.com/article/10.1007/s42978-025-00338-8) | Változó és állandó RIR | Nem egy AI-algoritmus hatásossági tesztje |
| [Wachholz és mtsai., 2025](https://pubmed.ncbi.nlm.nih.gov/40082991/) | AI által generált edzéstervek elfogadottsága és edzői megítélése | Kis mintás pilot; a teljes szöveget nem értem el |

### 17.3. Technológiai dokumentáció

| Forrás | Döntési szerep |
|---|---|
| [MCP-architektúra](https://modelcontextprotocol.io/docs/learn/architecture) | A kapcsolódási protokoll szerepe |
| [Sign in with ChatGPT](https://developers.openai.com/siwc/token-sharing-open-source) és [korlátok](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations) | Előfizetéshez kötődő integráció feltételei |
| [OpenAI API-árazás](https://developers.openai.com/api/docs/pricing) | Példa modellhasználati költség |
| [OpenAI adatkezelés](https://developers.openai.com/api/docs/guides/your-data) | Modelltréning és megőrzés megkülönböztetése |
| [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Strukturált kimenet lehetősége és korlátja |
| [Értékelési alapelvek](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Feladatspecifikus tesztelés |
| [FastAPI](https://fastapi.tiangolo.com/features/) és [Django](https://docs.djangoproject.com/en/5.2/intro/overview/) | Python keretrendszerek összehasonlítása |
| [Supabase árak](https://supabase.com/pricing) és [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) | Menedzselt adatbázis és jogosultság |

A dokumentált technikai képesség nem bizonyítja, hogy az adott megoldás a te időkereteddel a leggyorsabban megépíthető. Ezt a kis technikai próba és a saját esetkészlet alapján kell eldönteni.

### 17.4. Adatvédelem és rendeltetés

- [EU vállalkozói GDPR-tájékoztató](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm) és [adatvédelmi alapelvek](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en): az adatkezelési tervezés alapjai.
- [MDCG 2019-11 rev.1](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=md_mdcg_2019_11_guidance_qualification_classification_software_en.pdf): szoftver rendeltetése és orvostechnikai besorolása.
- [AI Act átláthatósági iránymutatás](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations): az AI-interakció és eredet jelölésének szabályozási háttere.

Ezek a források a tervezési kérdések azonosítását segítik. A végleges funkciók, szerepek, adatáramlások és marketingállítások alapján kell elvégezni az adott termék konkrét felülvizsgálatát.
