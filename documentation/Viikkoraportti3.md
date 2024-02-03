# Viikkoraportti 3

Tuntimäärä: 8,5

Tuntui hankalalta löytää sopivia tekstitiedostoja joilla testata LWZ-algoritmin pakkaavuutta, ja alkuperäinen teksti oli usein pienempi kooltaan kuin algoritmin läpikäynyt "kompressoitu" versio.
Lisäksi osa harkitsemistani tekstisyötteistä sisälsi ei-ASCII -merkkejä, joten ne ei sopineetkaan testaamiseen nykyisen version kanssa.

Aloitin huffman-koodauksen toteuttamista ja tutkimista, se vei paljon aikaa ja on vielä niin kesken ettei sille ole yksikkötestejä

En aivan tiedä miten testata paremmin ja mikä olisi sopiva syöte jolla testata, onnistuuko mm. LZW:ssa pakkaaminen tarpeeksi hyvin jotta päästäisiin 40-60% tienoille tiedoston koossa. Tällä hetkellä paras oli noin 68%