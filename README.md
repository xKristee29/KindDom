# Kindoom

Este un proiect ce vrea să-și ajute utilizatorii în viața de zi cu zi, dorind să le ofere lor, cât și celor din jurul acestora bucurie. Aplicația îi încurajază să dea dovadă de spirit civic prin fapte bune, adresate persoanelor din jurul fiecăruia dintre noi.

Proiectul are ca prim scop promovarea integrării sociale a fiecărui individ, fiind astfel un beneficiu pentru întreaga comunitate. Aceasta constă momentan în generarea unei liste de fapte bune pe care utilizatorul le va avea de făcut.

Periodic se presupune că un administrator al aplicației va actualiza fișierul `tasks.txt` astfel nu ar fi repetate faptele bune, devenind plictisitor

Alte idei care din păcate încă nu au putut fi implementate sunt:
 - Crearea unui cadru competițional, cu o tabelă, în care utilizatorii din toată lumea se pot întrece în fapte bune
 - Proiectarea unui cadru de articole cu sfaturi legate de cum se pot dezvolta pe plan personal, emoțional, toți cei care folosesc aplicația
 - Existența unui jurnal personal, în care fiecare persoană poate scrie câte o idee despre cum a fost fiecare zi din viața acesteia de la începerea folosirii programului, astfel pot reuși să-și analizeze parcursul în evoluție, observând avantajele
 - Confirmarea fiecărei fapte bune printr-un videoclip public, scurt, prin intermediul platformelor Instagram(Reels), TikTok, YouTube(Shorts), astfel fiind promovată platforma generând o posibilă reclamă în rândul apropiaților persoanei, și nu numai

## Pornirea aplicației

Pentru aceasta sunt folosite urmatoarele biblioteci din Python
```
nicegui
tinydb
```

Pentru protecția datelor de conectare, parolele sunt criptate cu ajutorul algoritmului SHA-256, unul dintre cele mai grele de descifrat forme de criptare

Pentru execuție se scriu în terminal următoarele comenzi
```
cd app/
py homepage.py
```