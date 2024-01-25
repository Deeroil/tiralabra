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
  
  # ...nyt tulos on sama kun kovakoodasin tän samaan järjestykseen
  string_table = ['a', 'b', 'd', 'n', '_']
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
      output_file.append(string_table.index(s))
      string_table.append(s+ch)
      s  = ch
    index += 1
  
  output_file.append(string_table.index(s))

  print("table", string_table)
  print("output", output_file)
  return (string_table, output_file)

def lzw_decompression(compressed, string_table):
  # lue indeksi, etsi se dictionarystä, output substring joka indeksissä.
  # first char of this substring is concat to working string
  # this new concat is added to the dict
  #decoded string becomes the current working string
  
  # print(compressed, string_table)

  string_table = ['a', 'b', 'd', 'n', '_']
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



def lzw_decompression2(compressed, string_table):
  numbers = string_table
  output_file = []
  string_table = ['a', 'b', 'd', 'n', '_']

  print(compressed)
  entry = ''
  ch = ''
  prevcode = -1
  currcode = -1

  prevcode = compressed[0]

  index = 0
  while index < len(compressed):
    currcode = compressed[index]
    entry = currcode
    output_file.append(entry)
    ch = entry[0]
    string_table.append(prevcode + ch)
    prevcode = currcode

    index += 1
  
  print("output:", output_file)
  print("str_table", string_table)

  decompressed = ''
  for i in numbers: #venaa miks tää riittää, eiks mun pitäis hyödyntää sitä myöhempää?
    decompressed += output_file[i]

  return decompressed


if __name__ == "__main__":
  test_string = "banana_bandana"
  compr = lzw_compression(test_string)
  print("")
  output = lzw_decompression2(compr[0], compr[1])

  if test_string == output:
    print("match!")