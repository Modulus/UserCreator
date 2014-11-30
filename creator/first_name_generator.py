__author__ = 'Modulus'

from bs4 import BeautifulSoup
import urllib
import codecs


class FirstNameGenerator(object):

    def __init__(self, mode=None, sources=None):
        self.mode = mode
        self.sources = sources

    def generate(self):
        if self.mode == "online":
            return self.generate_online()
        elif self.mode == "offline":
            return self.generate_offline()
        else:
            return []

    def generate_online(self):
        names = []

        for source in self.sources:
            page_contents = urllib.request.urlopen(source)
            self.parse(page_contents, names)

        return names

    def generate_offline(self):
        names = []
        for source in self.sources:
            contents = codecs.open(source, "r", "utf-8")
            self.parse(contents, names)

        return names

    def parse(self, page_contents, output):
        parser = BeautifulSoup(page_contents.read())

        return self.extract_anchor_data(output, parser)

    def extract_anchor_data(self, output, parser):
        for link in parser.find_all("a"):
            output.append(link.string)
        return output
