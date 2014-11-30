from unittest import TestCase
from creator.geodata_scraper import extract

__author__ = 'Modulus'


class GeodataScraperTest(TestCase):

    def test_1(self):

        content = extract("5111")
        self.assertIsNotNone(content)
