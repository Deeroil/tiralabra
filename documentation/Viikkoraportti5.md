# Viikkoraportti 5

Tuntimäärä: 5,5

Meni paljon aikaa löytää ASCII-only kirjoja joilla testata LWZ-algoritmia. Useissa oli ei-ascii merkkejä.
LWZ-algoritmin pakkaavuuden testaamista.
Osalla isoista tiedostoista kesti niin monia kymmeniä minuutteja ajautua (eikä loppua näkynyt), etten ole varma onko koodissa jokin bugi.

Edistin huffmanpuusta dekompressoimista ja korjasin muutaman bugin:
  - mm. merge-funktiossa tuli minheapin vertailuoperaatiossa ongelmia, sillä tuplessa ensimmäisten alkioiden arvon ollessa sama, yritti vertailla Nodea ja merkkijonoa. Nyt Nodella on vertailua varten funktiot
  - merkkijonojen ensimmäinen kirjain dekompressoitui väärin, sillä leading zeros binääristä katosivat kokonaisluvuksi muuttamisen takia, nyt korjattu