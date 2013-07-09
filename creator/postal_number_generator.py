__author__ = 'JohnSigvald'

import codecs

from creator.generator import Generator


class PostalNumberCreator(Generator):

    def __init__(self, source):
        self.source = source

    def generate(self):
        if self.source:
            file = codecs.open(self.source, "r", "utf-8")
            return file.readlines()
        else:
            return []





