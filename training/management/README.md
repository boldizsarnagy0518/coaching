# Kezelői parancsok és demóadat

[Edzésmodul](../README.md) · Frissítve: 2026. október 17.

## Felelősség

Kézzel indítható, reprodukálható segédműveletek. Jelenleg egyetlen parancs van: [seed_demo](commands/seed_demo.py).

## Aktuális állapot

Meglévő felhasználóhoz létrehoz egy szintetikus sportolót, egy tervet és egy edzést három előírt sorozattal. Felhasználót nem hoz létre, jelszót nem módosít, teljesítést nem naplóz. Hiányzó felhasználónál hibát jelez.

```powershell
uv run python manage.py seed_demo --username SAJAT_FELHASZNALONEV
```

A parancsot a projekt gyökeréből futtasd. Az edzés kezdeti dátuma a futtató gép aktuális dátuma.

## Döntések és indokok

| Döntés | Miért? | Következmény / korlát |
|---|---|---|
| Csak szintetikus adatok | Valós ügyféladat nélkül is bemutatható az adatfolyamat | A példasúlyok nem személyre szabott edzésajánlások |
| Meglévő fiók szükséges | A tesztadat betöltése ne változtassa a hitelesítést | A fiókot külön kell létrehozni |
| Meglévő demóelemek újrahasználata | Ismételt futtatás ne duplázza a példát | Azonosítás név/cím alapján; átnevezett adatnál új példa keletkezhet |
| Sorozatok csak új edzésnél készülnek | Újrafuttatás ne írja át a már használt demót | Nem általános javító vagy visszaállító parancs |
| Egy tranzakció | Sikertelen futás ne hagyjon félkész adatsort | Üzemeltetési mentést nem helyettesít |

## Ellenőrzés

A `test_seed_demo_is_repeatable_and_scoped_to_user` teszt ismételten futtatja a parancsot, és ellenőrzi az edzőhöz kötött létrehozást. A teljes tesztcsomag: `uv run python manage.py test training`.

## Következő lépés

Új teszthelyzetekhez névvel azonosítható szintetikus adatkészletek adhatók. CSV-import, export és adatjavító parancs még nincs.
