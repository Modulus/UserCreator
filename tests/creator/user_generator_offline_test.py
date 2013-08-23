import os

__author__ = 'Modulus'

import unittest

from creator.user_generator import UserGenerator


class UserGeneratorOfflineTest(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(__file__)
        boy_names = os.path.join(root_dir, "files/boy_names_ssb.html")
        girl_names = os.path.join(root_dir, "files/girl_names_ssb.html")
        sur_names_1 = os.path.join(root_dir, "files/sur_names_1_ssb.html")
        sur_names_2 = os.path.join(root_dir, "files/sur_names_2_ssb.html")
        self.generator = UserGenerator("offline", [boy_names, girl_names], [sur_names_1, sur_names_2], os.path.join(root_dir, "files/postnumre.txt"))

    def test_empty_input_empty_list(self):
        generator = UserGenerator(None, None, None, None)
        result = generator.generate()
        self.assertFalse(result, "Should be empty, no input given")

    def test_empty_source_empty_list(self):
        generator = UserGenerator("online", [], [], None)
        result = generator.generate()
        self.assertFalse(result)

    def test_generate_source_and_mode_creates_users(self):
        users = self.generator.generate(60)
        actual = len(users)
        self.assertTrue(users, "List is empty, this should not happen!")
        self.assertEquals(60, actual, "Amount not expected was {}".format(actual))


