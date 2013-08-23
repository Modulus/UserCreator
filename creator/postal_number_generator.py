__author__ = 'Modulus'

import codecs


class PostalNumberCreator(object):

    def __init__(self, source):
        self.source = source

    def generate(self):
        if self.source:
            postal_file = codecs.open(self.source, "rb", "utf-8")
            return postal_file.readlines()
        else:
            return []





