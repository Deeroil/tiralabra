from lzw import LZW
from huffman import Huffman


if __name__ == "__main__":
    lzw = LZW()
    huffman = Huffman()

    filename = "holmes"
    with open(f"./src/tests/files/{filename}.txt") as f:
        data = f.read()

    huff_compr = huffman.compress_to_file(data, filename)
    huff_decompr = huffman.decompress_from_file(filename)

    lzw_compr = lzw.compress_to_file(data, filename)
    lzw.decompress_from_file(filename)
