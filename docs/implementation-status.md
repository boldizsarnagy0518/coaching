# Implementálási állapot

2026. október 17. Az aktuális, 17 munkahétre átdolgozott ütemterv az irányadó.

Az egyes részek részletes állapota és döntési indoklása a [modulonkénti README-mutatóból](../README.md) érhető el. A [dokumentációs szabály](README.md) alapján ezek a későbbi fejlesztésekkel együtt frissítendők.

## Elkészült első műszaki munkacsomag

- Django 5.2, helyi SQLite, verziózott adatbázis-migráció.
- Bejelentkezés és minden alkalmazásnézetben szerveroldali edzői adatelkülönítés.
- Sportoló, terv, edzés és előírt sorozat létrehozása.
- Tényleges teljesítés külön rekordban: ismétlés, kg, opcionális sorozat-RPE.
- Mobilbarát szerveroldali felület, mentési visszajelzés és részleges naplózottság.
- Azonos beküldés ismétlése nem dupláz; eltérő beküldés nem írja felül a korábbi teljesítést.
- Szintetikus demóadat létrehozása meglévő fiókhoz, jelszóváltoztatás nélkül.
- Automatikus funkcionális és hozzáférési tesztek, GitHub Actions munkafolyamat.

Ez előrehozott technikai alap a felhasználó implementálási kérése alapján. Nem igazolja a validációs kapu teljesülését, és nem jelenti a 6–10. hét összes feladatának befejezését.

## Nyitott validáció

- Saját valós esetek dokumentálása; nincs kitalált interjú vagy ügyféladat.
- Edzői/sportolói interjúk és legalább 5 teljes kézi módosítás időmérése.
- Kaizer és egy további alternatíva tényleges kipróbálása.
- Kereslet, időigény és megkülönböztetés kapujának bizonyítékai.

## Következő műszaki munkacsomag

1. Edzéstervek változtathatatlan verziói és a verzióhoz kapcsolt előírások.
2. Kimaradás/áthelyezés strukturált kérése, javaslat, előtte/utána és edzői jóváhagyás.
3. Elavult verzióra érkező jóváhagyás elutasítása; naplózott teljesítés megőrzése.

## Még nincs kész

Sportolói saját belépés; CSV-import/export; múltbeli napló korrekciós folyamata; teljes offline működés; tervverziók; automatikus újratervezés; AI/MCP; számlázás; nyilvános telepítés; üzemeltetési mentés-visszaállítás és teljes adatkezelési folyamat.

A mostani felület edzői használatra készült: az edző rögzíti a sportoló adatait. Az alkalmazás nem módosít automatikusan terhelést és nem ad sérüléskezelési tanácsot. Valós sportolói adatok éles szolgáltatására még nem alkalmas.
