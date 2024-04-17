# Toteutusraportti

Ohjelmaan tarvittavat algoritmit on toteutettu kahtena erillisenä tiedostona, jotka ajetaan erikseen. Molemmat algoritmit voi suorittaa tiedostoon, ja ne voivat tallentaa kompressoidun datan tiedostoon.

Tällä hetkellä ohjelmalle ei voi antaa syötettä komentorivin kautta, vaan valinnat tehdään suoraan ohjelmakoodin sisällä esim index.py-tiedostossa voi antaa tiedoston nimen tunnisteosan. Tiedostoja haetaan kansiosta src/tests/files/

Yksikkötestit molemmille on tehty pytest-kirjastolla

## Suorituskykyvertailu

Luonnollisella kielellä tehty vertailu:


Dracula1  4.6 kB
LZW:      3   kB    65%
Huffman:  2.7 kB    60%

holmes1   14.5 kB
LZW:      8.7  kB   60%
Huffman:  8.5  kB   58%

romeojuliet   141.7 kB  
LZW:          71.8  kB  50%
Huffman:      85.3  kB  60%

holmes2   334.1 kB  
LZW:      151.3 kB  45%
Huffman:  187.5 kB  56%

holmes3   2.0 MB
LZW:      830 kB    42%
Huffman:  1.2 MB    60%

holmes4   4.0 MB
LZW:      1.6 MB    40%
Huffman:  2.3 MB    58%

holmes    6.5 MB
LZW:      2.5 MB    38%
Huffman:  3.7 MB    57%

Lorem ipsumilla tehty vertailu
(sisältää paljon toisteisuutta)

lipsum500B 501 B
LZW:       358 B
Huffman:   305 B 

lipsum1KB  1.1 kB 
LZW:       742 B
Huffman:   637 B

lipsum4KB   4.1 kB
LZW:        2.3 kB
Huffman:    2.2 kB

lipsum16KB  16.1 kB
LZW:        13.4 kB
Huffman:    8.7 kB

lipsum1MB   1.2 MB
LZW:        7.4 kB
Huffman:    643 kB 

lipsum2MB   2.4 MB
LZW:        583.4 kB
Huffman:    1.3 MB


## Työn mahdolliset puutteet ja parannusehdotukset
- LZW-algoritmista pakkaavuuden tutkiminen

## Laajojen kielimallien käyttö

- OpenAI:n ChatGPT 3.5:sta käytin kun selvitin miten muuntaa merkkijonoesitys binääristä binääritavuiksi. 
