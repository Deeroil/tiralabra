import heapq


class Node:
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right


class HuffmanTree:
    def __init__(self, data):
        self.minheap = []
        self.data = data

        self.root = None
        self.nodes = []
        self.leaves = []

        for i in data:
            heapq.heappush(self.minheap, i)
            node = Node(i[0], i[1], None, None)
            self.nodes.append(node)
            self.leaves.append(node)

        print("minheap", self.minheap)
        print("nodes", self.nodes)

    # vain mergessä nyt
    def add(self, freq, char, left, right):
        # tää pitää muokata jotenkin, mihin me halutaan root?
        if not self.root:
            self.root = Node(freq, char, left, right)
            return

        node = self.root
        while True:
            if node.frequency == freq and node.character == char:
                return
            if node.frequency > freq:
                if not node.left:
                    node.left = Node(freq, char, left, right)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(freq, char, left, right)
                    return
                node = node.right

    def merge(self):
        # ei toimi näin, inner nodet pitää muistaa huomioida
        a = heapq.heappop(self.minheap)
        b = heapq.heappop(self.minheap)
        print("a", a)
        print("b", b)
        node_a = Node(a[0], a[1])
        node_b = Node(b[0], b[1])

        #lisätään inner nodea vastaava node minheappiin
        heapq.heappush(self.minheap, (a[0]+b[0], a[1]+b[1]))
        print("mergessä minheap", self.minheap)
        # self.add(a[0] + b[0], None, node_a, node_b)

        node_n = Node(a[0] + b[0], None, node_a, node_b)
        self.nodes.append(node_n)

    # def __contains__(self, value):
    #     if not self.root:
    #         return False

    #     node = self.root
    #     while node:
    #         if node.value == value:
    #             return True
    #         if node.value > value:
    #             node = node.left
    #         else:
    #             node = node.right
    #     return False

    # merkkijonoesitys alkioista listana
    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append((node.frequency, node.character))
        self.traverse(node.right, items)

    def __len__(self):
        items = []
        self.traverse(self.root, items)
        return len(items)


class Huffman:
    """
    Huffman-koodilla pakkaaminen ja purkaminen
    Tää versio ei käytössä, teen HuffmanTreessä just nyt vain
    """

    def compression(self, data):
        # eka pitäis käydä läpi montaako merkkiä tässä on :D
        n = 6  # tää perustuu nyt GeeksForGeeks esimerkkiin nii otin vaa 6

        heap = []
        for d in data:
            node = Node(d[0], d[1])
            heapq.heappush(heap, node)

        while True:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            freq_z = left[0] + right[0]
            z = Node(freq_z, None, left, right)
            heapq.heappush(heap, z)

    def decompression(self, compressed):
        pass


if __name__ == "__main__":
    example_data = [(9, "b"), (5, "a"), (12, "c"), (13, "d"), (16, "e"), (45, "f")]
    # tree = HuffmanTree(example_data)

    # while len(tree.minheap) > 0:
    #   tree.merge()
    #   print(tree)

    huff = HuffmanTree(example_data)
    # print(h.minheap)

    while len(huff.minheap) > 1:
      huff.merge()
    
    for i in huff.nodes:
      print(i.frequency, i.character)
      
      if i.left or i.right:
        print(i.left, i.right)
