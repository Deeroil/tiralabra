import unittest
from ..huffman import Huffman, HuffmanTree

banana_string = "banana_bandana"
kokkola_string = "kokkola kokakola koko kokko lakko"

# https://www.youtube.com/watch?v=0kNXhFIEd_w
example_freqlist = [(9, "b"), (5, "a"), (12, "c"), (13, "d"), (16, "e"), (45, "f")]
example_str = "bfbbfafdddfbcccffefcccffdddddbfffecfffacfbbfaafcfefafccfffcfefffdddfffefffddffffeffffbbfeeeeeeeeeeff"
example_codes = {"f": "0", "c": "100", "d": "101", "a": "1100", "b": "1101", "e": "111"}

hw_str = "Hello world!"
hw_freqlist = []
hw_codes = {}

with open("./src/tests/files/lipsum500B.txt") as f:
    lorem_ipsum = f.read()

with open("./src/tests/files/lorem_longer.txt") as f:
    lorem_longer = f.read()

with open("./src/tests/files/loremlorem.txt") as f:
    loremlorem = f.read()

with open("./src/tests/files/customers-100.txt") as f:
    customers100 = f.read()


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = Huffman()
        self.hufftree = HuffmanTree(example_freqlist)
        # self.hufftree = HuffmanTree()

    def test_freq_list_creates_correct_tuplelist(self):
        flist = self.huffman.create_frequencylist(example_str)
        example_freqlist.sort()
        flist.sort()
        self.assertEqual(flist, example_freqlist)

    def test_huffmantree_root_is_right(self):
        root = self.hufftree.root
        freq = root.frequency
        self.assertEqual(freq, 100)

    def test_huffmantree_len_is_right(self):
        length = len(self.hufftree)
        self.assertEqual(length, 11)

    def test_huffmantree_codes_len_is_right(self):
        self.assertEqual(len(self.hufftree.codes), 6)

    def test_huffmantree_codes_are_right(self):
        self.assertEqual(self.hufftree.codes, example_codes)

    def test_huffman_lipsum500B_decompresses_right(self):
        compr = self.huffman.compression(lorem_ipsum)
        decompr = self.huffman.decompression(compr)
        self.assertEqual(lorem_ipsum, decompr)

    def test_huffman_customers_decompresses_right(self):
        compr = self.huffman.compression(customers100)
        decompr = self.huffman.decompression(compr)
        self.assertEqual(customers100, decompr)

    def test_huffman_loremlorem_decompresses_right(self):
        compr = self.huffman.compression(loremlorem)
        decompr = self.huffman.decompression(compr)
        self.assertEqual(loremlorem, decompr)

    def test_huffman_lorem_longer_decompresses_right(self):
        compr = self.huffman.compression(lorem_longer)
        decompr = self.huffman.decompression(compr)
        self.assertEqual(lorem_longer, decompr)

    def test_huffman_saves_to_file_and_then_decompresses_from_it_right(self):
        self.huffman.compress_to_file(lorem_ipsum, "src/tests/test_generated/lorem")
        decompr = self.huffman.decompress_from_file("src/tests/test_generated/lorem")
        self.assertEqual(lorem_ipsum, decompr)
