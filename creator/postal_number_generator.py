# -*- coding: utf-8 -*-
__author__ = 'Modulus'

import codecs


class PostalNumberCreator(object):

    def __init__(self, source):
        self.source = source

    def generate(self, uniques=True):
        if self.source:
            postal_file = codecs.open(self.source, "rb", "utf-8")
            numbers = postal_file.readlines()
            if uniques:
                # filter out unique
                extracted_num = []
                for number in numbers:
                    if number not in extracted_num:
                        extracted_num.append(number)
                return extracted_num
            else:
                return numbers
        else:
            return []





