__author__ = 'JohnSigvald'

from creator import user_generator as generator
from db.mongo_connector import MongoConnector

if __name__ == "__main__":
    generator = generator.UserGenerator("offline", ["creator/files/boy_names_ssb.html", "creator/files/girl_names_ssb.html"], ["creator/files/sur_names_1_ssb.html", "creator/files/sur_names_2_ssb.html"])
    users = generator.generate()

    print("{} names created in total...".format(len(users)))
    print("Saving to mongodb")

    db = MongoConnector()
    db.create_users(users)

    print("Saved data")

