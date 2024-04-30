Az adatbázishoz tartozó táblák és rövid leírásaik. Az alkalmazás le lesz limitálva a regisztrációs és bejelentkezéses részen, hogy ne tudjon a rossz indulatú felhasználó táblákat változtatni, illetve a SQLite amit a Django használ paraméteres adatokat fog használni, így hibát fog jelezni, a rossz indulatú felhasználó ellen. 

**Players:**
    id INTEGER PRIMARY KEY
    name VARCHAR(20)
    password VARCHAR(255)

Players (játékosok) tábla eltárolja a játékos egyedi azonosítóját (id) és nevét (name), illetve a játékos által választott jelszót hashelve (password).

**Cards:**
    id VARCHAR(10) PRIMARY KEY
    name VARCHAR(255)
    description TEXT
    image VARCHAR(100)
    type VARCHAR(10)
    is_bandit BOOLEAN
    symbol VARCHAR(10)
    occurence INTEGER

**CharacterCard:**
    hit_point INTEGER

Cards (kártyák) tábla eltárolja a kártyák egyedi azonosítóját (id) kártyák és nevét (name), illetve a kártya leírását. Ezekkel az adatokkal lesz kitöltve a kártyák weboldali sablonja sablonja.

**Achievements:**
    id INTEGER PRIMARY KEY
    name VARCHAR(255)
    description TEXT

Achievements (eredmények) tábla tárolja a játékban elérhető eredmények egyedi azonosítóját (id) és nevét (name), illetve az eredmény leírását (description).

**Player_achievements:**
    player_id INTEGER
    achievement_id INTEGER
    date DATETIME

Player_achievements (játékos_eredmények) tábla egy összekötő tábla ami összeköti a játékosokat (player_id) és az ő általuk megszerzett eredményeket (achievemt_id). Amikor egy játékos teljesít egy eredményt akkor a táblába bekerül játékos_id + eredmény_id pár formában.
