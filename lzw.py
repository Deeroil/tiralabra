import string


# https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
# https://www2.cs.duke.edu/csed/curious/compression/lzw.html

def lzw_compression(decompressed):
  # string_table = list(string.ascii_letters) #a-z, A-Z
  
  string_table = []
  output_file = []

  # tää on eri tavalla kuin pseudokoodissa
  for i in decompressed:
    if i not in string_table:
      string_table.append(i)

  #
  
  # ...nyt tulos on sama kun kovakoodasin tän samaan järjestykseen
  # string_table = ['a', 'b', 'd', 'n', '_']
  string_table = []
  index = 0

  #s = decompressed[0]
  s = ""

  while index < len(decompressed):
    ch = decompressed[index]
    if s + ch in string_table:
      s = s + ch
    else:
      # encode p to output file
      # code = string_table.index(p)
      output_file.append(s)
      string_table.append(s+ch)
      s  = ch
    index += 1
  
  output_file.append(s)

  print("table", string_table)
  print("output", output_file)
  return (string_table, output_file)

def lzw_decompression(compressed, string_table):
  # lue indeksi, etsi se dictionarystä, output substring joka indeksissä.
  # first char of this substring is concat to working string
  # this new concat is added to the dict
  #decoded string becomes the current working string
  
  # print(compressed, string_table)
  working_string = ''
  prevcode = -1
  currcode = -1

  prevcode = compressed[0]
  #???????? decode/output prevcode??
  working_string += string_table[prevcode] #näin???

  index = 0 #tai 1???
  while index < len(compressed):
    # print(compressed[index])
    currcode = compressed[index]
    entry = string_table[currcode]
    working_string += entry
    ch = entry[0]

    # lisää string_table(prevcode)+ch to dictionary???
    prevcode = currcode

    index += 1




if __name__ == "__main__":
  compr = lzw_compression("banana_bandana")
  print("")
  # lzw_decompression(compr[0], compr[1])