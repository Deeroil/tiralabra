import unittest
from ..lzw import LZW

"""
lzw_test.py

Unit tests for the lzw algorithm

"""

lorem_ipsum = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut egestas urna vitae rutrum mattis. Nunc quis porttitor enim, eget convallis arcu. Sed venenatis magna ut elit dictum aliquet. In ac nunc eget mauris dignissim rutrum ac eu est. Aenean vehicula tincidunt placerat. Fusce eu elit vestibulum tortor aliquet finibus et sed ex. Integer a turpis metus. Fusce tempus lectus quam, vel aliquam enim tempor sed. Cras eget gravida libero. Vestibulum condimentum elit a lacus semper volutpat. Duis in diam scelerisque, ultricies elit id, rutrum dolor. Nullam placerat arcu quam. Maecenas semper eu mauris eu rhoncus. Etiam malesuada lectus a blandit euismod. Duis efficitur pulvinar nulla, imperdiet dignissim neque.

    Sed dignissim ex vel quam semper aliquet. Vestibulum lacinia quam a accumsan viverra. Quisque blandit tincidunt ligula tincidunt interdum. In a semper sapien. Cras tincidunt libero dolor, in pellentesque nunc imperdiet ac. Duis nec leo libero. Sed finibus non ante ac porttitor. Aenean vestibulum nisl nec est volutpat, id semper justo mollis. Aenean eget magna purus. Morbi ipsum lectus, finibus sit amet iaculis ac, mollis eu nulla. Vestibulum quis eros in tortor aliquam ornare in congue augue. Mauris lobortis erat eu magna sollicitudin condimentum. Etiam dictum nisl in nulla egestas tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;

    Duis in faucibus dui. Proin ullamcorper ut nunc ut egestas. Aliquam nec purus eros. Ut fringilla vel erat vel lacinia. Suspendisse dapibus feugiat nisl et imperdiet. Nulla molestie lorem eu consequat sollicitudin. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vel erat malesuada, accumsan nisl at, fermentum erat. Etiam velit metus, ornare id tristique tempor, sollicitudin sit amet diam. Nam posuere venenatis rutrum. Quisque vel hendrerit lacus. Cras urna risus, vulputate non lectus sed, posuere semper nunc. Phasellus volutpat diam non metus varius malesuada. Nunc consequat orci magna, eget egestas sem dapibus quis. Integer nisl mi, porta eu neque vitae, dapibus sagittis turpis. Mauris fringilla ullamcorper felis at accumsan.

    Aliquam pellentesque nunc id augue vestibulum, vitae elementum leo tincidunt. Donec vitae lacus tempus, molestie nisl vitae, lacinia ipsum. Nam ultrices convallis felis vel suscipit. Morbi cursus faucibus consectetur. Mauris mattis eleifend tincidunt. Morbi turpis nisi, congue non tempus sit amet, scelerisque ac enim. Ut non diam in eros imperdiet varius in at sem. Fusce commodo feugiat velit, ut cursus risus euismod in. Aenean venenatis quis lectus eu pretium. Praesent tellus lectus, pretium quis gravida eu, facilisis et metus. Proin purus massa, laoreet ac luctus ut, dictum ut leo. Etiam sed rutrum nisl. Phasellus aliquet tellus vulputate metus ullamcorper bibendum.

    Cras lacus lacus, pharetra non elit a, laoreet cursus nisi. Pellentesque id tempor magna. Donec ac rhoncus velit, eu mollis dui. Proin lacinia luctus quam, in porttitor ligula viverra posuere. Vivamus pretium vestibulum scelerisque. Mauris velit turpis, tempor eu enim egestas, semper commodo mauris. Aliquam erat volutpat. 
   """
banana_string = "banana_bandana"
banana_compressed = [98, 97, 110, 257, 97, 95, 256, 110, 100, 259]

kokkola_string = "kokkola kokakola koko kokko lakko"
kokkola_compressed = [107, 111, 107, 256, 108, 97, 32, 256, 107, 97, 259, 261, 263, 111, 262, 257, 256, 32, 260, 258, 111]


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

    def test_lorem_ipsum_compresses_enough(self):
        # add some longer text here and test how much it compresses
        pass
