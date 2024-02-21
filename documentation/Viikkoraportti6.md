# Viikkoraportti 6

Tuntimäärä: 6

Toteutin LWZ:lle tiedostoon tallentamista. Jostain syystä kerran kun yritin vain purkaa tiedoston valmiiksi kompressoidusta tiedostosta, oli saadun tiedoston sisältö täysin eri kuin tarkoitettu tiedosto.
En saanut toistettua ongelmaa.

Nopeutin LWZ-algoritmin toimintaa vaihtamalla listoista dictiin.

Huffman-algoritmin nopeutus tapahtui kääntämällä yksi lista väärinpäin jotta käytin pop() enkä pop(0), ja siihen liittyvät muutokset decode-koodissa.

Pakkaaminen ja purkaminen sujuu nyt reilusti nopeammin molemmilla algoritmeilla.

Huffman-puun tallentamisen tutkimista jotat tallentuisi vähempään tilaan, yritän saada tehtyä sen vielä viikon 6 aikana.