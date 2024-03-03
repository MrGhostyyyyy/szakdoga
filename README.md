# Szakdolgozat
Téma: Bang Párbaj társasjáték implementálása egy- vagy többjátékos módban  
Készítette: Sós Marcell Sándor  
Konzulens: dr. Gombos Gergő

# Bang Párbaj
{szabalyok, leiras lehet felig meddig copy-pasta}

# Backend
A játékszerver kódja Python alapú Django nevű keretrendszerrel került megvalósításra, ami localhost:8000 szervert futtat. Ez a keretrendszer képes az adatbázist kezelni, a szerverrel kommunikálókat fogadni és válaszolni nekik. Ngrok segítségével akár böngészőből is elérhetővé lehet tenni ezt a localhost-on futtatott szervert. Az ngrok-hoz regisztrálni kell és a automatikusan generált linken vagy a fiókhoz járó ingyenes linken keresztül lehet elérni az oldalt. Az én esetemben ezen a linken https://becoming-bluebird-notably.ngrok-free.app érhető el az oldal.

## Szerver elindításának parancsa
Linux:  
&emsp;`python3 manage.py runserver`  
&emsp;`ngrok http 8000 --domain becoming-bluebird-notably.ngrok-free.app`

Windows:  
&emsp;`Is this necessary?`
