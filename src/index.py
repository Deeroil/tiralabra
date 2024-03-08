from lzw import LZW
from huffman import Huffman


if __name__ == "__main__":
    lzw = LZW()
    huffman = Huffman()

    # files = ["lipsum500B", "lipsum1KB", "lipsum4KB", "lipsum16KB", "lipsum1MB", "lipsum2MB"]
    # files = ["holmes0", "holmes1", "holmes2", "holmes3", "holmes4", "holmes"]
    # print(filename)

    filename = "holmes"

    # for filename in files:
    print("")
    print(filename)
    with open(f"./src/tests/files/{filename}.txt") as f:
        data = f.read()

    print("compression starting (huffman)")
    huffman.compress_to_file(data, filename)
    print("compressed")
    huff_file_decompr = huffman.decompress_from_file(filename)
    print("decompressed (huffman)")

    print("compression starting (LZW)")
    lzw.compress_to_file(data, filename)
    print("compressed")
    lzw_file_decompr = lzw.decompress_from_file(filename)
    print("decompressed (LZW)")
    # print(lzw_compr)

    if huff_file_decompr == data:
        print("decompression is same as original data (huffman)")
    else:
        print("decompression NOT same as original data (huffman)")

    if lzw_file_decompr == data:
        print("decompression is same as original data (LZW)")
    else:
        print("decompression NOT same as original data (LZW)")

    huff_compr = huffman.compression(data)
    # print("huffman compr:", huff_compr[0], huff_compr[1])

    lzw_compr = lzw.compression(data)
    # print("lzw compr:", lzw_compr)
