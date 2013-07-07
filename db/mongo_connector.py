__author__ = 'JohnSigvald'

import random

from pymongo import MongoClient

class MongoConnector():

    def create_users(self, user_list):
        client = MongoClient('localhost', 27017)
        db = client.test

        db.drop()

        print(type(user_list))
        db.test.insert(user_list)
        #
        # for e in db.test.find():
        #     print(e)

    if __name__ == "__main__":
        client = MongoClient("localhost", 27017)
        db = client.test
        client.drop_database("test")

        elements = [
            {"user_name": "john", "passwd":"1234idiot", "integer": random.randint(5, 99129291911)},
            {"user_name": "karoline", "passwd": "1234haxxx000ro123", "integer": random.randint(5, 19192882233)},
            {"user_name":"kjetil", "passwod": "passvord", "integer": random.randint(5, 7892713897)}
        ]

        for element in elements:
            db.test.insert(element)

