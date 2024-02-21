import heapq
import pickle
import sys


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
        # print("traverse node:", node.frequency)
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

    # TODO: erottele (de)compression ja (de)compress to file
    def compression(self, data: str):
        """
        Huffman-koodaus, kompressio. WIP.

        Parametri: merkkijonomuodossa oleva kompressoitava data
        """
        datalist = self.create_frequencylist(data)
        tree = HuffmanTree(datalist)
        # print("root", tree.root.frequency)

        compressed = ""
        for i in data:
            compressed += tree.codes[i]

        # keep the leading zeros while converting to int
        compressed = "1" + compressed

        binary_data = int(compressed, 2)
        bytes_data = binary_data.to_bytes(
            (binary_data.bit_length() + 7) // 8, byteorder="big"
        )

        # print("\nbytes", bytes_data)
        return (bytes_data, tree)

    def compress_to_file(self, data: str, filename: str):
        output = self.compression(data)

        bytes_compr = output[0]
        tree = output[1]

        with open(f"./{filename}_huffman.bin", "wb") as f:
            f.write(bytes_compr)

        with open(f"{filename}_hufftree.pkl", "wb") as f:
            pickle.dump(tree.root, f)

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

    def decompression(self, compressed):
        bytes_data = compressed[0]
        tree = compressed[1]
        binary = bin(int.from_bytes(bytes_data, byteorder="big"))
        binary = binary[3:]
        # print("bin", binary)

        path = []
        for i in binary:
            path.append(i)

        path.reverse()

        output = []
        while len(path) > 0:
            tree.decode(tree.root, path, output)

        print("decoded")
        output_str = ""
        for i in output:
            output_str += i
        return output_str

    def decompress_from_file(self, filename):

        with open(f"./{filename}_huffman.bin", "rb") as f:
            compressed = f.read()

        with open(f"./{filename}_hufftree.pkl", "rb") as f:
            root = pickle.load(f)

        huff = HuffmanTree([(0, 0)])
        bytes_data = compressed
        binary = bin(int.from_bytes(bytes_data, byteorder="big"))
        binary = binary[3:]

        path = []
        for i in binary:
            path.append(i)

        path.reverse()

        output = []
        print("gonna decode")
        while len(path) > 0:
            huff.decode(root, path, output)
        print("decoded")

        output_str = ""
        for i in output:
            output_str += i
        return output_str
