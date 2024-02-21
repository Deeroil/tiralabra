import pickle


class LZW:
    """
    Toteuttaa Lempel-Ziv-Welch pakkausalgoritmin,
    sekä pakkaamisen että purkamisen.
    Toimii merkkijonoilla.

    Algoritmien toteuttamisessa on hyödynnetty pseudokoodia
    seuraavilta sivuilta:
      https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
      https://www2.cs.duke.edu/csed/curious/compression/lzw.html

    """

    def __init__(self):
        pass

    def compression(self, decompressed: str):
        """
        Lempel-Ziv-Welch kompressioalgoritmi

        Ottaa vastaan: merkkijonon
        Palauttaa: Listan indeksejä, joka on kompressoitu versio merkkijonosta

        esim.
        Parametri: "banana_bandana"
        Palauttaa: [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]
        """

        print("compressing...")
        decomp_len = len(decompressed)
        string_table = {}
        for i in range(256):
            string_table[chr(i)] = i
        output_file = []
        index = 0
        s = ""

        while index < decomp_len:
            ch = decompressed[index]
            if s + ch in string_table:
                s = s + ch
            else:
                output_file.append(string_table[s])
                string_table[s + ch] = len(string_table)
                s = ch
            index += 1

        output_file.append(string_table[s])

        filename = "dict_loremlorem4MB"
        with open(f"compressed_{filename}_lwz.pkl", "wb") as f:
            pickle.dump(output_file, f)

        print("compr valmis")
        return output_file

    def decompression(self, compressed: list):
        """
        Lempel-Ziv-Welch dekompressioalgoritmi

        Parametri: lista indeksejä, kompressoitu versio merkkijonosta
        Palauttaa: merkkijono joka saadaan purkamalla kompressio

        esim
        Parametri: [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]
        Palauttaa: "banana_bandana"
        """

        print("decompressing...")
        output_file = []
        compr_len = len(compressed)

        string_table = {}
        for i in range(256):
            string_table[chr(i)] = i

        index_table = {}
        for i in range(256):
            index_table[i] = chr(i)

        entry = ""
        ch = ""
        prevcode = compressed[0]
        currcode = -1
        c = ""

        index = 1
        while index < compr_len:
            currcode = compressed[index]
            if len(index_table) - 1 < currcode:
                s = index_table[prevcode]
                s = s + c
            else:
                s = index_table[currcode]

            entry = s
            output_file.append(entry)
            ch = entry[0]

            stringtable_len = len(string_table)
            string_table[index_table[prevcode] + ch] = stringtable_len
            index_table[stringtable_len] = index_table[prevcode] + ch
            prevcode = currcode

            index += 1

        decompressed = ""
        for i in compressed:
            decompressed += index_table[i]

        return decompressed

    def decompress_from_file(self):
        filename = "holmes"
        with open(f"compressed_{filename}_lwz.pkl", "rb") as f:
            output = pickle.load(f)

        a = self.decompression(output)
        print("Yay done")

        with open(f"decompressed_{filename}_lwz.pkl", "w") as f:
            f.write(a)
        return a
