# -*- coding: utf-8 -*-
import codecs
import os
from unittest import TestCase
from creator.geodata_scraper import extract_address, _extract_postal_list, extract_all, extract_address_csv
from creator.postal_number_generator import PostalNumberCreator
from models.address import Address

__author__ = 'Modulus'


class GeodataScraperTest(TestCase):

    def extract_coordinates(self):

        content = extract_address("5111")
        self.assertIsNotNone(content)

    def test_extract_postal_lines(self):
        numbers = _extract_postal_list()
        self.assertIsNotNone(numbers)

    def test_extract_postal_has_weird_letter(self):
        address = extract_address("9037")
        self.assertIsNotNone(address)

    def test_extract_address_csv(self):
        actual = extract_address_csv("Hordaland,Bergen,5059,Bergen,['60.393', '5.324'],Norway;")


        expected = Address(municipality="Bergen", county="Hordaland",
                           location="Bergen", country="Norway", coordinates=["60.393", "5.324"], code="5059")

        self.assertEquals(actual, expected)


    # def test_read_csv_file(self):
    #     root_dir = os.path.dirname(__file__)
    #     file_path = os.path.join(root_dir, "files/geodata.txt")
    #
    #     addresses = []
    #
    #     with codecs.open(file_path, "r", "utf-8") as file:
    #         contents = file.readlines()
    #
    #         for content in contents:
    #
