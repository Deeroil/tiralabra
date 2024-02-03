import unittest
import sys
from ..lzw import LZW

banana_string = "banana_bandana"
banana_compressed = [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]

kokkola_string = "kokkola kokakola koko kokko lakko"
kokkola_compressed = [107, 111, 107, 256, 108, 97, 32, 256, 107, 97, 259, 261, 263, 111, 262, 257, 256, 32, 260, 258, 111]

with open("./src/tests/loremipsum.txt") as f:
    lorem_ipsum = f.read()

with open("./src/tests/lorem_longer.txt") as f:
    lorem_longer = f.read()

with open("./src/tests/pg26096.txt") as f:
    book = f.read()

with open("./src/tests/loremlorem.txt") as f:
    loremlorem = f.read()

with open("./src/tests/customers-100.txt") as f:
    customers100 = f.read()

def utf8len(s):
        return len(s.encode('utf-8'))

class TestLZW(unittest.TestCase):
    def setUp(self):
        self.lzw = LZW()

    def test_banana_bandana_compression(self):
        compr = self.lzw.compression(banana_string)
        self.assertEqual(compr, banana_compressed)

    def test_banana_bandana_decompression(self):
        decompr = self.lzw.decompression(banana_compressed)
        self.assertEqual(decompr, banana_string)

    def test_banana_bandana_compres_and_decompres(self):
        compr = self.lzw.compression(banana_string)
        decompr = self.lzw.decompression(compr)
        self.assertEqual(banana_string, decompr)

    def test_kokkola_compression(self):
        compr = self.lzw.compression(kokkola_string)
        self.assertEqual(compr, kokkola_compressed)

    def test_kokkola_decompression(self):
        decompr = self.lzw.decompression(kokkola_compressed)
        self.assertEqual(decompr, kokkola_string)

    def test_lorem_ipsum_compresses_and_decompresses(self):
        compr = self.lzw.compression(lorem_ipsum)
        decompr = self.lzw.decompression(compr)
        self.assertEqual(lorem_ipsum, decompr)

    def test_longer_lorem_ipsum_compresses_and_decompresses(self):
        compr = self.lzw.compression(lorem_longer)
        decompr = self.lzw.decompression(compr)
        self.assertEqual(lorem_longer, decompr)

    # def test_shorter_lorem_ipsum_sizes(self):
    #     compr = self.lzw.compression(lorem_ipsum)
    #     # decompr = self.lzw.decompression(compr)
    #     original_size = sys.getsizeof(lorem_ipsum)
    #     compressed_size = sys.getsizeof(compr)
    #     self.assertEqual(original_size, compressed_size)

    # def test_longer_lorem_ipsum_sizes(self):
    #     #  this doesnt really compress :/
    #     compr = self.lzw.compression(lorem_longer)
    #     original_size = sys.getsizeof(lorem_longer)
    #     compressed_size = sys.getsizeof(compr)

    #     self.assertGreater(original_size, compressed_size)

    # def test_longer_lorem_ipsum_compresses_and_decompresses(self):
    #     # add some longer text here and test how much it compresses
    #     compr = self.lzw.compression(lorem_longer)
    #     decompr = self.lzw.decompression(compr)
    #     self.assertEqual(lorem_longer, decompr)


    def test_loremlorem_ipsum_is_(self):
        compr = self.lzw.compression(loremlorem)
        original_size = sys.getsizeof(loremlorem)
        compressed_size = sys.getsizeof(compr)
        self.assertGreater(original_size, compressed_size)

    def test_100_customers_compresses_and_decompresses(self):
        # add some longer text here and test how much it compresses
        compr = self.lzw.compression(customers100)
        decompr = self.lzw.decompression(compr)
        self.assertEqual(customers100, decompr)

    # def test_10000_customers_compresses_and_decompresses(self):
    #     # add some longer text here and test how much it compresses
    #     compr = self.lzw.compression(customers)
    #     decompr = self.lzw.decompression(compr)
    #     self.assertEqual(customers, decompr)


    # def test_book_compresses_and_decompresses(self):
    #     # add some longer text here and test how much it compresses
    #     compr = self.lzw.compression(book)
    #     decompr = self.lzw.decompression(compr)
    #     self.assertEqual(book, decompr)

    # def test_book_compresses_enough(self):
    #     # add some longer text here and test how much it compresses
    #     pass