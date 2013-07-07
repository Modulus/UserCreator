__author__ = 'JohnSigvald'

from bs4 import BeautifulSoup
import urllib2

from creator.generator import Generator


class LastNameGenerator(Generator):

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

    def generate_online(self):
        names = []
        for source in self.sources:
            contents = urllib2.urlopen(source)
            parser = BeautifulSoup(contents.read())
            for element in parser.find_all("tr"):
                print(element)
        return names

    def generate_offline(self):
        names = []

        for source in self.sources:
            source_content = open(source, "r").read()
            self.parse(source_content, names)
        return names

    def parse(self, html, output):
        parser = BeautifulSoup(html)
        trs = parser.find_all("tr")

        for tr in trs:
            tds = tr.findAll("td")
            #Name is in the third td tag, extracting
            if tds:
                output.append(str(tds[2].contents))
