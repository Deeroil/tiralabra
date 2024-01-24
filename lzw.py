import string


# https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
# https://www2.cs.duke.edu/csed/curious/compression/lzw.html
merkkijono = "banana_bandana"

def lzw_compression(D):
  # string_table = list(string.ascii_letters) #a-z, A-Z
  
  string_table = []
  output_file = []

  # tää on eri tavalla kuin pseudokoodissa
  for i in merkkijono:
    if i not in string_table:
      string_table.append(i)
  
  # ...nyt tulos on sama kun kovakoodasin tän samaan järjestykseen
  string_table = ['a', 'b', 'd', 'n', '_']

  index = 0

  p = merkkijono[0]

  index += 1

  while index < len(merkkijono):
    c = merkkijono[index]
    if p + c in string_table:
      p = p + c
    else:
      # encode p to output file
      code = string_table.index(p)
      output_file.append(code)
      string_table.append(p+c)
      p = c
    index += 1
  
  code = string_table.index(p)
  output_file.append(code)

  print("table", string_table)
  print("output", output_file)

if __name__ == "__main__":
  lzw_compression("moi")