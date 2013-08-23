import os

__author__ = 'Modulus'

import unittest

from creator.user_generator import FirstNameGenerator


class FirstNameGeneratorOnlineTest(unittest.TestCase):
    def setUp(self):
        root = os.path.dirname(__file__)
        boy_names = os.path.join(root, "files/boy_names_ssb.html")
        girl_names = os.path.join(root, "files/girl_names_ssb.html")
        self.generator = FirstNameGenerator("offline", [boy_names,
                                                        girl_names])

    def test_mode_empty_empty_list(self):
        generator = FirstNameGenerator()
        result = generator.generate()
        self.assertListEqual([], result, "List should be empty, no input given")

    def test_generate_has_elements(self):
        result = self.generator.generate()
        self.assertIsNotNone(result, "List is None, should never be the case!")
        self.assertTrue(len(result) > 300, "Result should have data, it is now empty!!")

        #Print the result
        for user in result:
            print user



