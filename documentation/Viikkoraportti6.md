# Viikkoraportti 6

Tuntimäärä: 10,5

Toteutin LWZ:lle tiedostoon tallentamista. Jostain syystä kerran kun yritin vain purkaa tiedoston valmiiksi kompressoidusta tiedostosta, oli saadun tiedoston sisältö täysin eri kuin tarkoitettu tiedosto.
En saanut toistettua ongelmaa.

Nopeutin LWZ-algoritmin toimintaa vaihtamalla listoista dictiin.

Huffman-algoritmin nopeutus tapahtui kääntämällä yksi lista väärinpäin jotta käytin pop() enkä pop(0), ja siihen liittyvät muutokset decode-koodissa.

Pakkaaminen ja purkaminen sujuu nyt reilusti nopeammin molemmilla algoritmeilla.
Huffman-puun tallentaminen pienempään tilaan on myös toteutettu, ja docstringejä lisätty.

GHA ei antanut generoida tiedostoja tieodstoon kirjoittamisen testaamisessa, joten kommentoin kyseiset testit pois. En tiedä kannattaako sitten testata eri tavalla, esim. vain manuaalisesti.

Ensi viikolla aion viimeistellä dokumentaatiota ja mitata suorituskykyä.
