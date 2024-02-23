import heapq


class Node:
    """
    Luokka solmuille Huffman-puuta varten
    """

    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right

    def __lt__(self, obj):
        if not isinstance(obj, Node):
            return True
        else:
            return False

    def __gt__(self, obj):
        return not self.__lt__(obj)


class HuffmanTree:
    """
    Huffman-puun luominen Huffman algoritmin soveltamiseen.

    Parametrit: data, lista tupleja.
    """

    def __init__(self, data: list):
        self.minheap = []
        self.root = None
        self.codes = {}

        for i in data:
            heapq.heappush(self.minheap, i)

        while len(self.minheap) > 1:
            self.merge()

        self.find_codes(self.root, "")
        # print("codes", self.codes)

    def merge(self):
        """
        Poistaa minimikeosta kaksi pienintä solmua a ja b.
        Lisää minimikekoon näistä johdetun solmun
        ja asettaa juurisolmun jos on sen aika
        """

        a = heapq.heappop(self.minheap)
        b = heapq.heappop(self.minheap)
        left = Node(a[0], a[1])
        right = Node(b[0], b[1])

        if isinstance(a[1], Node):
            left = a[1]

        if isinstance(b[1], Node):
            right = b[1]

        node_n = Node(a[0] + b[0], None, left, right)
        heapq.heappush(self.minheap, (a[0] + b[0], node_n))

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

        self.traverse(node.left, items)
        items.append((node.frequency, node.character))
        self.traverse(node.right, items)

    def decode(self, node: Node, path: list, output: list):
        """
        Käy läpi solmut annetussa järjestyksessä ja tallentaa saadun merkkijonon

        Parametrit:
            node: juurisolmu tai käsiteltävä solmu
            path: binääriesitys koodeista
            output: lopullinen tulos
        """

        if not node:
            return

        if node.character is not None:
            output.append(node.character)
            return

        if len(path) == 0:
            return

        if path[-1] == "0":
            path.pop()
            self.decode(node.left, path, output)
        elif path[-1] == "1":
            path.pop()
            self.decode(node.right, path, output)
        else:
            print("path[0]", path[0])

    def store_tree(self, node: Node, output: list):
        """
        Varastoi huffmanpuun listaksi.

        Parametrit:
            node: juurisolmu tai käsiteltävä solmu
            output: lista johon tallennetaan solmuja kuvaavat bitit

        Mukailee C#-pseudokoodia täältä:
        https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree
        """
        if not node:
            return

        if node.character is not None:
            charnum = ord(node.character)
            binary = bin(charnum)[2:].zfill(8)
            output.append("1" + binary)

        else:
            output.append("0")
            self.store_tree(node.left, output)
            self.store_tree(node.right, output)

    def __len__(self):
        items = []
        self.traverse(self.root, items)
        return len(items)


class Huffman:
    """
    Huffman-koodilla pakkaaminen ja purkaminen.
    Vielä erittäin kesken, ei osaa vielä kompressoida
    """

    def bytes_helper(self, data: str):
        """
        Muuntaa merkkijonoesityksen binääristä tavuiksi.
        Huom. lisää annetun binäärin alkuun luvun 1, jotta alussa
        olevat 0-bitit eivät katoa.

        Parametri: merkkijonoesitys binääristä

        Palauttaa: tavun

        esimerkki:
        Parametri: "001"
        Palauttaa: tavun, joka kuvastaa binäärilukua "1001"
        """

        # print("data", data)
        data = "1" + data
        binary_data = int(data, 2)
        bytes_data = binary_data.to_bytes(
            (binary_data.bit_length() + 7) // 8, byteorder="big"
        )
        return bytes_data

    def compression(self, data: str):
        """
        Huffman-koodaus, kompressio. WIP.

        Parametri: merkkijonomuodossa oleva kompressoitava data
        """
        datalist = self.create_frequencylist(data)
        tree = HuffmanTree(datalist)

        compressed = ""
        for i in data:
            compressed += tree.codes[i]

        bytes_data = self.bytes_helper(compressed)
        return (bytes_data, tree)

    def compress_to_file(self, data: str, filename: str):
        output = self.compression(data)

        bytes_compr = output[0]
        tree = output[1]

        stored_tree = []
        tree.store_tree(tree.root, stored_tree)

        string_tree = ""
        for i in stored_tree:
            string_tree = string_tree + i

        tree_bytes = self.bytes_helper(string_tree)

        with open(f"./{filename}_huffman.bin", "wb") as f:
            f.write(bytes_compr)

        with open(f"{filename}_hufftree_compr.bin", "wb") as f:
            f.write(tree_bytes)

        return True

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

    def open_stored_tree(self, treelist: list):
        """
        Purkaa huffman-puuta kuvaavan yksinkertaistetun puun listasta.
        Huom: lista on käännetty väärinpäin ja käsitellään lopusta alkaen.

        Parametrit:
            treelist: käännetty lista kaikista puussa käsiteltävistä biteistä.
                esim. ["0", "1", "1", ..., "0"]

        Mukailee C#-pseudokoodia täältä, tosin lista on käännetty ja mukautukset siihen liittyen
        https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree
        """
        if treelist[-1] == "1":
            treelist.pop()

            byte = ""
            for _ in range(8):
                byte = byte + treelist.pop()
            char = chr(int(byte, 2))

            return Node(None, char)
        elif treelist[-1] == "0":
            treelist.pop()

            left = self.open_stored_tree(treelist)
            right = self.open_stored_tree(treelist)

            return Node(0, None, left, right)

    def decompression(self, compressed):
        bytes_data = compressed[0]
        tree = compressed[1]
        path = self.bytes_to_reversed_list_helper(bytes_data)

        output = []
        while len(path) > 0:
            tree.decode(tree.root, path, output)

        print("decoded")
        output_str = ""
        for i in output:
            output_str += i
        return output_str

    def bytes_to_reversed_list_helper(self, data):
        binary = bin(int.from_bytes(data, byteorder="big"))
        binary = binary[3:]

        binlist = []
        for i in binary:
            binlist.append(i)
        binlist.reverse()
        return binlist

    def decompress_from_file(self, filename):
        with open(f"./{filename}_huffman.bin", "rb") as f:
            compressed = f.read()

        with open(f"./{filename}_hufftree_compr.bin", "rb") as f:
            tree_from_file = f.read()

        huff = HuffmanTree([(0, 0)])
        path = self.bytes_to_reversed_list_helper(compressed)

        treelist = self.bytes_to_reversed_list_helper(tree_from_file)
        root = self.open_stored_tree(treelist)

        output = []
        print("gonna decode")
        while len(path) > 0:
            huff.decode(root, path, output)
        print("decoded")

        output_str = ""
        for i in output:
            output_str += i
        return output_str
