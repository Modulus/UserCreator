__author__ = 'Modulus'

import random

from pymongo import MongoClient


class MongoConnector():

    def create_users(self, user_list):
        client = MongoClient('localhost', 27017)
        client.drop_database("tests")


        db = client.test

        db.test.insert(user_list)
        # for user in iter(user_list):
        #     db.test.insert(user.json())

        # #
        # for e in db.tests.find():
        #     print(e)

    if __name__ == "__main__":
        client = MongoClient("localhost", 27017)
        db = client.test
        client.drop_database("tests")

        elements = [
            {"user_name": "john", "passwd":"1234idiot", "integer": random.randint(5, 99129291911)},
            {"user_name": "karoline", "passwd": "1234haxxx000ro123", "integer": random.randint(5, 19192882233)},
            {"user_name":"kjetil", "passwod": "passvord", "integer": random.randint(5, 7892713897)}
        ]

        for element in elements:
            db.test.insert(element)

