# Testausdokumentti

Yksikkötestauksen kattavuusraportti:
* https://app.codecov.io/gh/Deeroil/tiralabra

Mitä on testattu, miten tämä tehtiin
* LWZ-algoritmissa sekä huffman-koodissa on testattu merkkijonosyötteen pakkaamisen sekä purkamisen onnistumista erikseen sekä testaamalla onko lopputulos sama kuin alunperin oli.
* Huffman-puusta on testattu mm. onko puussa tarpeeksi alkioita, toimiiko frequency list oikein ja että puun avulla luodut koodit ovat oikein.
* LWZ:ssa on testattu myös pakkaavuuta, toistaiseksi paras oli 68%.

Minkälaisilla syötteillä testaus tehtiin
* LWZ: ASCII-merkkejä sisältävillä erilaisilla syötteillä, mm. loremipsum-generaattorilla tuotettua tekstiä.

Miten testit voidaan toistaa
* suorittamalla pytest-testit (tarkemmat ohjeet myöhemmin)

Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa
* (toteutus myöhemmin)