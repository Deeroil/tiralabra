import unittest
from ..huffman import Huffman, HuffmanTree

banana_string = "banana_bandana"
banana_compressed = [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]

kokkola_string = "kokkola kokakola koko kokko lakko"
kokkola_compressed = [
    107,
    111,
    107,
    256,
    108,
    97,
    32,
    256,
    107,
    97,
    259,
    261,
    263,
    111,
    262,
    257,
    256,
    32,
    260,
    258,
    111,
]


# https://www.youtube.com/watch?v=0kNXhFIEd_w
example_freqlist = [(9, "b"), (5, "a"), (12, "c"), (13, "d"), (16, "e"), (45, "f")]
example_str = "bfbbfafdddfbcccffefcccffdddddbfffecfffacfbbfaafcfefafccfffcfefffdddfffefffddffffeffffbbfeeeeeeeeeeff"
example_codes = {"f": "0", "c": "100", "d": "101", "a": "1100", "b": "1101", "e": "111"}

hw_str = "Hello world!"
hw_freqlist = []
hw_codes = {}


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
