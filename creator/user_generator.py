from creator import first_name_generator

__author__ = 'JohnSigvald'

import random

from creator.generator import Generator
from creator.first_name_generator import FirstNameGenerator
from creator.last_name_generator import LastNameGenerator
from models.user import User


class UserGenerator(Generator):

    def __init__(self, mode=None, first_name_sources=None, last_name_sources=None):
        self.mode = mode
        self.first_name_generator = FirstNameGenerator(mode, first_name_sources)
        self.last_name_generator = LastNameGenerator(mode, last_name_sources)

    def create_name_list(self, first_names, last_names):
        users = []
        for last_name in last_names:
            for first_name in first_names:
                user = User(first_name, last_name)
                users.append(user)
        return users

    def generate(self):
        first_names = self.first_name_generator.generate()
        last_names = self.last_name_generator.generate()
        return self.create_name_list(first_names, last_names)






