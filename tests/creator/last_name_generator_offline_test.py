__author__ = 'Modulus'

import unittest

from creator.last_name_generator import LastNameGenerator


class LastNameGeneratorOfflineTest(unittest.TestCase):

    def setUp(self):
        self.generator = LastNameGenerator("offline", ["../files/sur_names_1_ssb.html", "../files/sur_names_2_ssb.html"])

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