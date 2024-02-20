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
        string_table = [chr(i) for i in range(256)]
        output_file = []
        index = 0
        s = ""

        while index < len(decompressed):
            ch = decompressed[index]
            if s + ch in string_table:
                s = s + ch
            else:
                output_file.append(string_table.index(s))
                string_table.append(s + ch)
                s = ch
            index += 1
            # print(index, "<", len(decompressed), ":", s)

        output_file.append(string_table.index(s))

        filename = "holmes"
        with open(f"compressed_{filename}_lwz.pkl", "wb") as f:
            pickle.dump(output_file, f)

        print("out noniinh")
        # print("out", output_file)
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
        string_table = [chr(i) for i in range(256)]
        entry = ""
        ch = ""
        prevcode = compressed[0]
        currcode = -1
        c = ""

        index = 1
        while index < len(compressed):
            currcode = compressed[index]
            if len(string_table) - 1 < currcode:
                s = string_table[prevcode]
                s = s + c
            else:
                s = string_table[currcode]

            entry = s
            output_file.append(entry)
            ch = entry[0]
            string_table.append(string_table[prevcode] + ch)
            prevcode = currcode

            index += 1
            # print(index, entry)

        decompressed = ""
        for i in compressed:
            decompressed += string_table[i]

        return decompressed

    def decompress_from_file(self):
        filename = "holmes"
        with open(f"compressed_{filename}_lwz.pkl", "rb") as f:
            output = pickle.load(f)

        a = self.decompression(output)
        # print("aaaA:", a)
        print("Yay done")
        # print("a", a)

        with open(f"decompressed_{filename}_lwz.pkl", "w") as f:
            f.write(a)
