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


class HuffmanTree:
    """
    Huffman-puun luominen Huffman algoritmin soveltamiseen.
    Vielä kovin kesken.
    """

    def __init__(self, data):
        self.minheap = []
        self.data = data

        self.root = None
        self.nodes = []

        for i in data:
            heapq.heappush(self.minheap, i)
            node = Node(i[0], i[1], None, None)
            self.nodes.append(node)

        while len(self.minheap) > 1:
            self.merge()

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

        heapq.heappush(self.minheap, (a[0] + b[0], a[1] + b[1]))

        node_n = Node(a[0] + b[0], None, node_a, node_b)
        self.nodes.append(node_n)

        if len(self.minheap) == 1:
            self.root = node_n

class Huffman:
    """
    Huffman-koodilla pakkaaminen ja purkaminen.
    Vielä erittäin kesken
    """

    def compression(self, data: str):
        """
        Huffman-koodaus, kompressio. WIP

        Parametri: merkkijonomuodossa oleva kompressoitava data
        """
        datalist = self.create_frequencylist(data)
        tree = HuffmanTree(datalist)

        print("root", tree.root.frequency)

        # TODO: assign binary values to letters
        #         - traverse to leaf, save path of L/R w/ 1 and 0?

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
