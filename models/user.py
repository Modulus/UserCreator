__author__ = 'JohnSigvald'

import jsonpickle


class User():

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name.encode("utf-8")
        self.last_name = last_name.encode("utf-8")
        self.address = address

    def json(self):
        return jsonpickle.encode(self)