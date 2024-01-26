### MÄÄRITTELYDOKUMENTTI

Opinto-ohjelma:
* Tietojenkäsittelytieteen kandidaatti

Ohjelmointikieli:
* Python, mielellään en arvioi muilla kielillä olevia projekteja

Algoritmit ja tietorakenteet ja ratkaistava ongelma:
* Toteutan pakkausalgoritmit Huffman-koodaukselle ja Lemper Ziv -algoritmille (mahdollisesti LZ77), ja vertaan niiden tuloksia samanlaisilla syötteillä.

Mitä syötteitä ohjelma saa, miten näitä käytetään:
* Ohjelma tulee saamaan syötteenä luonnollista kieltä sisältävää tekstiä. Syöte pakataan kummankin algoritmin kohdalla erikseen tiivistetympään muotoon ja tallennetaan tiedostona. Pakatusta muodosta pitää pystyä palaamaan alkuperäiseen muotoon purkamalla.

Tavoitteena olevat aika- ja tilavaativuudet:
* LZ77:n aikavaativuus on O(M) M-merkkiselle tekstisyötteelle, ja Huffman-koodaukselle O(n log n).

**Lähteet:**
* https://en.wikipedia.org/wiki/LZ77_and_LZ78
* https://en.wikipedia.org/wiki/Huffman_coding


