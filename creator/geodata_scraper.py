# -*- coding: utf-8 -*-
import logging
import os
from creator.postal_number_generator import PostalNumberCreator
from models.address import Address
import urllib
from bs4 import BeautifulSoup

__author__ = 'Modulus'

logger = logging.getLogger("GeodataScraper")
logger.setLevel("INFO")


def create_address(soup):
    if soup.find("table", class_="restable"):
        rows = soup.find("table", class_="restable").find_all("tr")
        if len(rows) >= 3:
            first_row = rows[1]
            geo_row = rows[2]

            # TODO: Use defaultdict
            location = first_row.contents[1].text
            code = first_row.contents[2].text
            country = first_row.contents[3].text
            county = first_row.contents[4].text
            muni = first_row.contents[5].text

            coord_str = geo_row.contents[1].text
            coords = coord_str.split("/")
            latidue = coords[0]
            latidue = latidue.replace("\xa0", "")
            longditude = coords[1]
            longditude = longditude.replace("\xa0", "")
            address = Address(location=location, code=code, country=country, municipality=muni, county=county,
                              coordinates=[latidue, longditude])
            return address
        return None
    return None

def extract_address(postal_number):

    logger.info("Extracting coordinates")

    base_url = "http://www.geonames.org/postalcode-search.html?q={query}&country=NO"
    q_url = base_url.format(query=postal_number)

    response = urllib.request.urlopen(q_url)
    html = response.read()

    soup = BeautifulSoup(html)

    address = create_address(soup)

    return address


def extract_all():
    numbers = _extract_postal_list()
    addresses = []
    for number in numbers:
        data_tuple = number.split(" ")

        if len(data_tuple) >= 1:
            code = data_tuple[0]

            address = extract_address(code)
            addresses.append(address)

    return addresses


def _extract_postal_list():
    root_dir = os.path.dirname(__file__)
    postal_generator = PostalNumberCreator(os.path.join(root_dir, "files/postnumre.txt"))

    return postal_generator.generate()


def extract_address_csv(csv_line):
    parts = csv_line.split(",")

    county = parts[0]
    municipality = parts[1]
    code = parts[2]
    location = parts[3]
    coordinates = parts[4]
    country = parts[5]

    address = Address(municipality=municipality, county=county,
                      location=location, country=country, coordinates=coordinates, code=code)

    return address


def match_class(target):
    target = target.split()

    def do_match(tag):
        try:
            classes = dict(tag.attrs)["class"]
        except KeyError:
            classes = ""
        classes = classes.split()
        return all(c in classes for c in target)

    return do_match