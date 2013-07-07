__author__ = 'JohnSigvald'

import unittest

from creator.user_generator import UserGenerator


class UserGeneratorOfflineTests(unittest.TestCase):

    def setUp(self):
        self.generator = UserGenerator("offline", ["../files/boy_names_ssb.html", "../files/girl_names_ssb.html"], ["../files/sur_names_1_ssb.html", "../files/sur_names_2_ssb.html"])

    def test_empty_input_empty_list(self):
        generator = UserGenerator(None, None)
        result = generator.generate()
        self.assertFalse(result, "Should be empty, no input given")

    def test_empty_source_empty_list(self):
        generator = UserGenerator("online", [])
        result = generator.generate()
        self.assertFalse(result)

    def test_generate_source_and_mode_creates_users(self):
        users = self.generator.generate()
        self.assertTrue(users, "List is empty, this should not happen!")
        self.assertEquals(2716000, len(users), "Should have this many users, check if something got added or removed from source")