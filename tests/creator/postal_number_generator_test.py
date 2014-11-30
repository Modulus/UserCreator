import os

__author__ = 'Modulus'

import unittest

from creator.postal_number_generator import PostalNumberCreator


class PostalNumberGeneratorTest(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(__file__)
        self.generator = PostalNumberCreator(os.path.join(root_dir, "files/postnumre.txt"))

    def test_generate_has_none_input_result_empty_list(self):
        self.generator = PostalNumberCreator(None)
        self.assertListEqual([], self.generator.generate())

    def test_generate_has_empty_input_empty_list(self):
        self.generator = PostalNumberCreator("")
        self.assertListEqual([], self.generator.generate())

    def test_generate_has_elements_uniques_is_false(self):
        postal_list = self.generator.generate(uniques=False)
        self.assertTrue(list)
        self.assertEquals(35308, len(postal_list), "List of postal codes is incorrect")

    def test_generate_has_elements_uniques_is_true(self):
        postal_list = self.generator.generate(uniques=True)
        self.assertTrue(list)
        self.assertEquals(4566, len(postal_list), "List of postal codes is incorrect")

        postal_list = self.generator.generate()
        self.assertTrue(list)
        self.assertEquals(4566, len(postal_list), "List of postal codes is incorrect")

