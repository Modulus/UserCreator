__author__ = 'Modulus'

import random


from creator.first_name_generator import FirstNameGenerator
from creator.last_name_generator import LastNameGenerator
from creator.postal_number_generator import PostalNumberCreator
from models.user import User
from models.address import Address


class UserGenerator(object):

    def __init__(self, mode=None, first_name_sources=None, last_name_sources=None, postal_source=None):
        self.mode = mode
        self.first_name_generator = FirstNameGenerator(mode, first_name_sources)
        self.last_name_generator = LastNameGenerator(mode, last_name_sources)
        self.postal_code_generator = PostalNumberCreator(postal_source)

    def create_postal_info(self, postal_codes):
        if postal_codes and len(postal_codes) >= 2:
            a_index = random.randint(0, len(postal_codes) - 1)
            postal_line = postal_codes[a_index]
            postal_list = postal_line.split(" ", 2)
            address = Address(dict(code=postal_list[0], location=postal_list[1]))
            return address
        return None

    def create_name_list(self, first_names, last_names, postal_codes, amount=-1):
        users = []
        if amount < 0:
            for last_name in last_names:
                for first_name in first_names:
                    address = self.create_postal_info(postal_codes)
                    user = User(dict(firstName=first_name, lastName=last_name, address=address))
                    users.append(user)
        else:
            for index in range(0, amount):
                last_n_index = random.randint(0, len(last_names))
                first_n_index = random.randint(0, len(first_names))
                address = self.create_postal_info(postal_codes)
                user = User(dict(firstName=first_names[first_n_index], lastName=last_names[last_n_index], address=address))
                users.append(user)
        return users

    def generate(self, amount=-1):
        first_names = self.first_name_generator.generate()
        last_names = self.last_name_generator.generate()
        postal_codes = self.postal_code_generator.generate()

        if amount > 0:
            return self.create_name_list(first_names, last_names, postal_codes, amount)
        else:
            return self.create_name_list(first_names, last_names, postal_codes)






