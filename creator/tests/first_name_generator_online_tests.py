__author__ = 'JohnSigvald'

import unittest

from creator.first_name_generator import FirstNameGenerator


class FirstNameGeneratorOnlineTests(unittest.TestCase):
    def setUp(self):
        self.generator = FirstNameGenerator("online", ["http://www.ssb.no/a/kortnavn/navn/guttermange.html", "http://www.ssb.no/a/kortnavn/navn/pikermange.html"])

    def test_mode_empty_empty_list(self):
        generator = FirstNameGenerator()
        result = generator.generate()
        self.assertListEqual([], result, "List should be empty, no input given")

    def test_generate_has_elements(self):
        result = self.generator.generate()
        self.assertIsNotNone(result, "Result null, check connection")
        self.assertTrue(len(result) > 300)