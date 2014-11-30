__author__ = 'Modulus'

from bs4 import BeautifulSoup
import urllib
import codecs


class LastNameGenerator(object):

    def __init__(self, mode=None, sources=None):
        self.mode = mode
        self.sources = sources

    def generate(self):
        if self.mode == "online":
            return []
        elif self.mode == "offline":
            return self.generate_offline()
        else:
            return []

    #TODO: Finish this
    def generate_online(self):
        names = []
        for source in self.sources:
            contents = urllib.request.urlopen(source)
            parser = BeautifulSoup(contents.read())
            for element in parser.find_all("tr"):
                print(element)
        return names

    def generate_offline(self):
        names = []

        for source in self.sources:
            source_content = codecs.open(source, "r", "utf-8").read()
            self.parse(source_content, names)
        return names

    def parse(self, html, output):
        parser = BeautifulSoup(html)
        trs = parser.find_all("tr")

        for tr in trs:
            tds = tr.findAll("td")
            #Name is in the third td tag, extracting
            if tds:
                output.append(tds[2].string)
