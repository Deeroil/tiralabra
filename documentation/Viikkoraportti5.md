# Viikkoraportti 5

Tuntimäärä: 7,5

Meni paljon aikaa löytää ASCII-only kirjoja joilla testata LWZ-algoritmia. Useissa oli ei-ascii merkkejä.
LWZ-algoritmin pakkaavuuden testaamista.
Osalla isoista tiedostoista kesti niin monia kymmeniä minuutteja ajautua (eikä loppua näkynyt), etten ole varma onko koodissa jokin bugi.

Edistin huffmanpuusta dekompressoimista ja korjasin muutaman bugin:
  - mm. merge-funktiossa tuli minheapin vertailuoperaatiossa ongelmia, sillä tuplessa ensimmäisten alkioiden arvon ollessa sama, yritti vertailla Nodea ja merkkijonoa. Nyt Nodella on vertailua varten funktiot
  - merkkijonojen ensimmäinen kirjain dekompressoitui väärin, sillä leading zeros binääristä katosivat kokonaisluvuksi muuttamisen takia, nyt korjattu

Lisäksi Huffman-koodauksen tiedostoon tallennus toimii nyt.

Picklellä Huffman-puun tallentaminen vaikuttaa huonolta ratkaisulta, sillä se vie suuren osan tilasta, tai tallennan liikaa asioita.

esim. 1kB:n tiedostolla (lipsum1KB.txt), pakattu tiedosto on 579 tavua, mutta picklellä tallennettu huffmantree oli aluksi noin 4kB.
Sen jälkeen yritin tallentaa koko luokan ja tietojen sijaan vain listan solmuja sekä tiedon juurisolmusta, mutta koko on silti 3.4kB.

En oo varma mitä kaikkea tietoa huffman-puusta tulisi tallentaa. Vaikuttaa siltä että pelkän juurisolmun tallentaminen vaikuttaa riittävän. En tiedä tallentaako se samalla koko puun. Tällä tavalla tallennetun pickle-tiedoston koko on 2.2kB, eli kompressiota ei olla saatu.