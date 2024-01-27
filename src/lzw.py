import string

class LZW:
  '''
  Toteuttaa Lempel-Ziv-Welch pakkausalgoritmin,
  sekä pakkaamisen että purkamisen.
  Toimii merkkijonoilla.

  Algoritmien toteuttamisessa on hyödynnetty pseudokoodia
  seuraavilta sivuilta:
    https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
    https://www2.cs.duke.edu/csed/curious/compression/lzw.html

  '''

  def __init__(self):
    pass

  def compression(self, decompressed: string):
    '''
    Lempel-Ziv-Welch kompressioalgoritmi

    Ottaa vastaan: merkkijonon
    Palauttaa: Listan indeksejä, joka on kompressoitu versio merkkijonosta

    esim.
    Parametri: "banana_bandana"
    Palauttaa: [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]
    '''

    string_table = [chr(i) for i in range(256)]
    output_file = []
  
    # for banana_bandana
    # string_table = ['a', 'b', 'd', 'n', '_']
    index = 0
    s = ""

    while index < len(decompressed):
      ch = decompressed[index]
      if s + ch in string_table:
        s = s + ch
      else:
        output_file.append(string_table.index(s))
        string_table.append(s+ch)
        s  = ch
      index += 1
    
    output_file.append(string_table.index(s))
    print(output_file)
    return output_file

  def decompression(self, compressed: list):
    '''
    Lempel-Ziv-Welch dekompressioalgoritmi

    Parametri: lista indeksejä, kompressoitu versio merkkijonosta
    Palauttaa: merkkijono joka saadaan purkamalla kompressio

    esim
    Parametri: [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]
    Palauttaa: "banana_bandana"
    '''

    # print("compr", compressed)
    output_file = []
    string_table = [chr(i) for i in range(256)]
    entry = ''
    ch = ''
    prevcode = compressed[0]
    currcode = -1
    c = ''

    index = 1
    while index < len(compressed):
      currcode = compressed[index]
      # print("currcode", currcode)

      #aion bullshittaa tän nyt
      if len(string_table)-1 < currcode:
        s = string_table[prevcode]
        s = s + c
      else:
          s = string_table[currcode]
      
      entry = s #string_table[currcode]
      # print("entr",entry)
      output_file.append(entry)
      ch = entry[0]
      string_table.append(string_table[prevcode] + ch)
      prevcode = currcode

      index += 1
    # print("opfil", output_file)
    
    decompressed = ''
    for i in compressed:
      decompressed += string_table[i]

    return decompressed


if __name__ == "__main__":
  # test_string = "banana_bandana"
  test_string = "kokkola kokakola koko kokko lakko"

  lzw = LZW()
  compr = lzw.compression(test_string)
  output = lzw.decompression(compr)

  print("compressed:", compr)
  print("after decomp:", output)
  if test_string == output:
    print("match!")

