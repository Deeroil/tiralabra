import heapq

## TODO:
##    - huffman tree: traversing and adding binary values
##    - check if the tree works :D
##    - save as a binary file
##    - decompression to string
##    - add tests


class Node:
    """
    Luokka solmuille Huffman-puuta varten
    """

    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right


array = []


class HuffmanTree:
    """
    Huffman-puun luominen Huffman algoritmin soveltamiseen.

    Parametrit: data, lista tupleja.
    """

    def __init__(self, data: list):
        self.minheap = []
        self.root = None
        self.nodes = []
        self.codes = {}

        for i in data:
            heapq.heappush(self.minheap, i)
            node = Node(i[0], i[1], None, None)
            self.nodes.append(node)

        while len(self.minheap) > 1:
            self.merge()

        # print("root freq", self.root.frequency)
        # self.printCodes(self.root, "")
        self.find_codes(self.root, "")
        print("codes", self.codes)

    def merge(self):
        """
        Poistaa minimikeosta kaksi pienintä solmua a ja b.
        Lisää minimikekoon näistä johdetun solmun
        ja asettaa juurisolmun jos on sen aika
        """

        a = heapq.heappop(self.minheap)
        b = heapq.heappop(self.minheap)
        node_a = Node(a[0], a[1])
        node_b = Node(b[0], b[1])

        left = node_a
        right = node_b

        if isinstance(a[1], Node):
            left = a[1]

        if isinstance(b[1], Node):
            right = b[1]

        node_n = Node(a[0] + b[0], None, left, right)
        heapq.heappush(self.minheap, (a[0] + b[0], node_n))

        # print("node n:", node_n.frequency, node_n)
        # print("node n: left_freq", node_n.left.frequency)
        # print("node n: right_freq", node_n.right.frequency)

        self.nodes.append(node_n)

        if len(self.minheap) == 1:
            self.root = node_n

    def find_codes(self, node: Node, code: str):
        """
        Etsii polun lehtisolmuihin ja tallentaa ne self.codes -sanakirjaan.

        Parametrit:
            node: juurisolmu
            code: merkkijono johon kasataan polkuja
        """
        if not node:
            return
        if node.character is not None:
            self.codes[node.character] = code
        self.find_codes(node.left, code + "0")
        self.find_codes(node.right, code + "1")

    def traverse(self, node: Node, items: list):
        """
        Käy läpi solmut ja täyttää annetun listan niillä.

        Parametrit:
            node: juurisolmu tai käsiteltävä solmu
            items: aluksi tyhjä lista
        """
        if not node:
            return
        # print("traverse node:", node.frequency)
        self.traverse(node.left, items)
        items.append((node.frequency, node.character))
        self.traverse(node.right, items)

    def __len__(self):
        items = []
        self.traverse(self.root, items)
        # print(items)
        return len(items)


class Huffman:
    """
    Huffman-koodilla pakkaaminen ja purkaminen.
    Vielä erittäin kesken, ei osaa vielä kompressoida
    """

    def compression(self, data: str):
        """
        Huffman-koodaus, kompressio. WIP.

        Parametri: merkkijonomuodossa oleva kompressoitava data
        """
        datalist = self.create_frequencylist(data)
        tree = HuffmanTree(datalist)

        print("root", tree.root.frequency)

        # TODO: muuta nää binääritiedostoksi
        compressed = ""
        for i in data:
            print(tree.codes[i], "and", i)
            compressed += tree.codes[i]

        return compressed

    def create_frequencylist(self, data: str):
        """
        Luo frekvensseistä listan joka voidaan syöttää Huffman-puulle

        Parametri: merkkijonomuodossa oleva data
        Palauttaa: listan tupleja.

        Esimerkiksi:
        Parametri: "abac"
        Palauttaa: [(2, a), (1, b), (1, c)]
        """
        characters = []
        data_frequencies = []

        for i in range(len(data)):
            if data[i] not in characters:
                characters.append(data[i])
                data_frequencies.append((1))
            else:
                ind = characters.index(data[i])
                data_frequencies[ind] += 1

        tuple_list = []
        for i in range(len(characters)):
            tuple_list.append((data_frequencies[i], characters[i]))
        return tuple_list

    def decompression(self, compressed):
        pass


if __name__ == "__main__":
    example_data = [(9, "b"), (5, "a"), (12, "c"), (13, "d"), (16, "e"), (45, "f")]
    example_str = "bfbbfafdddfbcccffefcccffdddddbfffecfffacfbbfaafcfefafccfffcfefffdddfffefffddffffeffffbbfeeeeeeeeeeff"

    huffman = Huffman()
    huffman.compression(example_str)
