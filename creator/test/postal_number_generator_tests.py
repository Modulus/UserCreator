__author__ = 'JohnSigvald'

import unittest

from creator.postal_number_generator import PostalNumberCreator


class PostalNumberGeneratorTests(unittest.TestCase):

    def setUp(self):
        self.generator = PostalNumberCreator("../files/postnumre.txt")

    def test_generate_has_None_inut_result_empty_list(self):
        self.generator = PostalNumberCreator(None)
        self.assertListEqual([], self.generator.generate())

    def test_generate_has_elements(self):
        list = self.generator.generate()
        self.assertTrue(list)
        self.assertEquals(35308, len(list), "List of postal codes is incorrect")

        for value in range(25000, 30000):
            print(list[value])