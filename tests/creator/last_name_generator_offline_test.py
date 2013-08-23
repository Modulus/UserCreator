import os

__author__ = 'Modulus'

import unittest

from creator.last_name_generator import LastNameGenerator


class LastNameGeneratorOfflineTest(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(__file__)
        last_names_1 = os.path.join(root_dir, "files/sur_names_1_ssb.html")
        last_names_2 = os.path.join(root_dir, "files/sur_names_2_ssb.html")
        self.generator = LastNameGenerator("offline", [last_names_1, last_names_2])

    def test_empty_inut_empty_list(self):
        generator = LastNameGenerator(None, None)
        result = generator.generate()
        self.assertListEqual([], result)

    def test_generate_has_elements(self):
        result = self.generator.generate()
        self.assertIsNotNone(result, "Result is None, nothing created!")
        self.assertTrue(len(result) > 3000, "Result has no elements!")

        #Print the result
        for element in result:
            print(element)