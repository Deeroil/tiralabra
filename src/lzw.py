class LZW:
    """
    Toteuttaa Lempel-Ziv-Welch pakkausalgoritmin,
    sekä pakkaamisen että purkamisen.
    Toimii merkkijonoilla jotka sisältävät vain ASCII-merkkejä.

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
        Palauttaa: Listan indeksejä, joka on kompressoitu versio merkkijonosta.

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

        print("compr valmis")
        # print("listaeka:", output_file[0])
        # print("listavika:", output_file[len(output_file) -1])
        # print("len:", len(output_file))

        return output_file

    def compress_to_file(self, data: str, filename: str):
        """
        LZW tiedostoon kompressoiminen.
        Tallentuu tiedostoksi "filename_lzw_final.bin"

        Binääridatan alkuun tallennetaan lukujen maksimikoon
        infoa 32 bittiin.

        parametrit:
            data: merkkijonoesitys kompressoitavasta datasta
            filename: tallennettavan tiedoston nimen etuosa
        """
        compressed = self.compression(data)

        biggest_number = max(compressed)
        bitlen = biggest_number.bit_length()

        asia = ""

        # bittien pituus tallennetaan 32-bit sisälle alkuun
        b = bin(bitlen)[2:]
        b = b.zfill(32)
        asia += b

        for i in compressed:
            b = bin(i)[2:]
            if len(b) < bitlen:
                b = b.zfill(bitlen)
            asia += b

        asia = "1" + asia

        binary_data = int(asia, 2)
        bytes_data = binary_data.to_bytes(
            (binary_data.bit_length() + 7) // 8, byteorder="big"
        )

        with open(f"./{filename}_lzw_final.bin", "wb") as f:
            f.write(bytes_data)

    def decompression(self, compressed: list):
        """
        Lempel-Ziv-Welch dekompressioalgoritmi

        Parametri:
            compressed: lista indeksejä, kompressoitu versio merkkijonosta

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

    def decompress_from_file(self, filename: str):
        """
        LZW tiedostostosta purkaminen.
        Luetaan tiedostosta "filename_lzw_final.bin"

        32 ensimmäistä bittiä kertoo "bitlen", jonka avulla puretaan
        binääri-informaatio takaisin listaksi.

        parametrit:
            filename: purettavan tiedoston nimen etuosa
        """
        # with open(f"{filename}_compr_lwz_TEST.pkl", "rb") as f:
        #     output = pickle.load(f)

        with open(f"./{filename}_lzw_final.bin", "rb") as f:
            output = f.read()

        binary = bin(int.from_bytes(output, byteorder="big"))
        binary = binary[3:]

        # print("TYYPPI:", type(output))

        bitlen = binary[:32]
        bitlen = int(bitlen, 2)
        binary = binary[32:]
        print(bitlen)

        lista = []
        for i in range(0, len(binary), bitlen):
            luku = ""
            add = True
            for j in range(bitlen):
                if j + i < len(binary):
                    luku += binary[j + i]
                else:
                    add = False
            if add:
                lista.append(int(luku, 2))

        # print("len:", len(lista))
        # print("listaeka:", lista[0])
        # print("listavika:", lista[len(lista) -1])

        a = self.decompression(lista)
        print("Yay done")

        with open(f"./{filename}_decompr_lwz_FINAL.txt", "w") as f:
            f.write(a)
        return a


if __name__ == "__main__":
    lw = LZW()

    string = "banana_bandana"

    name = "holmes"
    # name = "testi"
    with open(f"./src/tests/files/{name}.txt") as f:
        file = f.read()
    print("luettu")

    # lorem_ipsum = "MOI TERVE JA HYVÄÄ PÄIVÄÄ"
    # original_size = sys.getsizeof(lorem_ipsum)

    # lorem_ipsum = string

    # compr = lw.compression(file)
    # # print(compr)
    # decmp = lw.decompression(compr)
    # print(decmp)

    lw.compress_to_file(file, name)

    decmp = lw.decompress_from_file(name)

    # print(decmp)

    if file == decmp:
        print("yay")
    else:
        print("höh")
