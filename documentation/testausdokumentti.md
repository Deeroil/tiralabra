# Testausdokumentti

Yksikkötestauksen kattavuusraportti:
* LWZ-algoritmia on kooda

Mitä on testattu, miten tämä tehtiin
* LWZ-algoritmissa on testattu merkkijonosyötteen pakkaamisen sekä purkamisen onnistumista erikseen sekä testaamalla onko lopputulos sama kuin alunperin oli.
* LWZ:ssa on testattu myös pakkaavuuta, toistaiseksi paras oli 68%.
* Huffman-koodausta ei ole vielä testattu muuten kuin käsin yksittäisillä syötteillä

Minkälaisilla syötteillä testaus tehtiin
*LWZ: ASCII-merkkejä sisältävillä erilaisilla syötteillä, mm. loremipsum-generaattorilla tuotettua tekstiä.

Miten testit voidaan toistaa
* suoritatmalla pytest-testit (tarkemmat ohjeet myöhemmin)

Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa
* (toteutus myöhemmin)