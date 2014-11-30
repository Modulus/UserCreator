# -*- coding: utf-8 -*-
import os
from unittest import TestCase
from creator.geodata_scraper import extract_address, _extract_postal_list, extract_all
from creator.postal_number_generator import PostalNumberCreator

__author__ = 'Modulus'


class GeodataScraperTest(TestCase):

    def extract_coordinates(self):

        content = extract_address("5111")
        self.assertIsNotNone(content)

    # def test_extract_all(self):
    #     all_numbers = extract_all()
    #     self.assertIsNotNone(all_numbers)

    def test_extract_postal_lines(self):
        numbers = _extract_postal_list()
        self.assertIsNotNone(numbers)

    def test_write_to_file(self):
        root_dir = os.path.dirname(__file__)
        file = os.path.join(root_dir, "files/geodata.txt")

        postal_elements = _extract_postal_list()

        for postal_element in postal_elements:
            elements = postal_element.split(" ")

            address = extract_address(elements[0])
            if address:
                with open(file, "a") as geo_file:
                    geo_file.write(address.csv())

    def test_extract_postal_has_weird_letter(self):
        address = extract_address("9037")
        self.assertIsNotNone(address)