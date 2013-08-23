import os

__author__ = 'Modulus'

import unittest

from creator.postal_number_generator import PostalNumberCreator


class PostalNumberGeneratorTest(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(__file__)
        self.generator = PostalNumberCreator(os.path.join(root_dir, "files/postnumre.txt"))

    def test_generate_has_None_input_result_empty_list(self):
        self.generator = PostalNumberCreator(None)
        self.assertListEqual([], self.generator.generate())

    def test_generate_has_empty_input_empty_list(self):
        self.generator = PostalNumberCreator("")
        self.assertListEqual([], self.generator.generate())

    def test_generate_has_elements(self):
        list = self.generator.generate()
        self.assertTrue(list)
        self.assertEquals(35308, len(list), "List of postal codes is incorrect")

        for value in range(25000, 30000):
            print(list[value])
