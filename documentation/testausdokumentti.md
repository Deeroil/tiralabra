# Testausdokumentti

Yksikkötestauksen kattavuusraportti:
* https://app.codecov.io/gh/Deeroil/tiralabra

Mitä on testattu, miten tämä tehtiin
* LWZ-algoritmissa sekä huffman-koodissa on testattu merkkijonosyötteen pakkaamisen sekä purkamisen onnistumista erikseen sekä testaamalla onko lopputulos sama kuin alunperin oli.
* Huffman-puusta on testattu mm. onko puussa tarpeeksi alkioita, toimiiko frequency list oikein ja että puun avulla luodut koodit ovat oikein.
* pakkaavuuta on myös testattu, parhaat LZW:ssä luonnollisella kielellä on ollut (ei-lorem-ipsum) 64-67%% ja Huffman-koodissa noin 56% alkuperäisestä koosta
* manuaalisesti olen testannut näitä samoja asioita myös

* tiedostojen tallentamista ja lukemista ja näistä purkamista on testattu, mutta en saanut GitHub Actionsissa tätä toimimaan, joten se puuttuu

Minkälaisilla syötteillä testaus tehtiin
* ASCII-merkkejä sisältävillä erilaisilla syötteillä, mm. loremipsum-generaattorilla tuotettua tekstiä sekä kirjoilla jotka sisältävät vain ASCII-merkistöä.

Miten testit voidaan toistaa
* suorittamalla pytest-testit ajamalla pytest src/tests