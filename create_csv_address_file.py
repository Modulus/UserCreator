# -*- coding: utf-8 -*-
import codecs
import logging
import os
import sys
from time import sleep
from creator.geodata_scraper import _extract_postal_list, extract_address

__author__ = 'Modulus'

logger = logging.getLogger("CSV Extractor")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
logger.addHandler(ch)

def do_magic():
    root_dir = os.path.dirname(__file__)
    file = os.path.join(root_dir, "creator/files/geodata.txt")

    postal_elements = _extract_postal_list()
    logger.info("Starting to read data")
    for postal_element in postal_elements:
        elements = postal_element.split(" ")

        if elements[0]:
            logger.info("Getting address for postal number {}".format(elements[0]))

            address = extract_address(elements[0])

            logger.info("Address extracted")
            if address:
                with codecs.open(file, "a", "utf-8") as geo_file:
                    geo_file.write(address.csv())
        else:
            logger.error("Missing postal number")

        logger.info("Finished reading number sleeping for a bit...")
        sleep(3)



def do_tromso():
    root_dir = os.path.dirname(__file__)
    file = os.path.join(root_dir, "creator/files/geodata-test.txt")
    address = extract_address("9037")

    logger.info("Address extracted")
    if address:
        with codecs.open(file, "a", "utf-8") as geo_file:
            geo_file.write(address.csv())


if __name__ == "__main__":
    do_magic()