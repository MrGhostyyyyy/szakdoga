# Szakdolgozat
Téma: Bang Párbaj társasjáték implementálása egy- vagy többjátékos módban  
Készítette: Sós Marcell Sándor  
Konzulens: dr. Gombos Gergő

# Bang Párbaj
{szabalyok, leiras lehet felig meddig copy-pasta}

# Backend
A játékszerver kódja Python alapú Django nevű keretrendszerrel került megvalósításra, ami localhost:8000 szervert futtat, amit egy ngrok nevű alkalmazás segítségével lehet az interneten keresztül elérhetővé tenni. Ez a keretrendszer képes az adatbázist kezelni, a szerverrel kommunikálókat fogadni és válaszolni nekik.

## Szerver elindításának parancsa
Linux:  
&emsp;`python3 manage.py runserver {portszam}`  
&emsp;`ngrok vmi`

Windows:  
&emsp;`Is this necessary?`

## gameserver mappa
`manage.py, __init\__.py, asgi.py, settings.py, urls.py, wsgi.py` a Django által generált scriptek, amikkel dolgozni kell és úgynevezett alkalmazásokkal (apps) ki kell egészíteni.

### manage.py
A szervert elindítja és a megadott paramétereket alkalmazza.

### __init__.py
A Python kötelező fájlja, ami jelzi a Interpreternek, hogy ez a mappa egy csomagként (package) kezelendő.

### asgi.py
TBD or researched

### settings.py
A Django szerver beállításait és konstansait tartalmazó file. Ha módosításokat szeretnénk végrehajtani a szerverrel kapcsolatban, akkor ebben kell módosítani a módosításra szoruló változót.

### urls.py
A Django szerveren keresztül elérhető URL-ek, amikkel a weboldalt lehet navigálni.

### wsgi.py
TBD or researched

## achievements mappa(?)

## 