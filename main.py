__author__ = 'JohnSigvald'

from creator import user_generator as generator
from db.mongo_connector import MongoConnector
from models.address import Address
from models.user import User

if __name__ == "__main__":
    generator = generator.UserGenerator("offline", ["creator/files/boy_names_ssb.html", "creator/files/girl_names_ssb.html"],
                                        ["creator/files/sur_names_1_ssb.html", "creator/files/sur_names_2_ssb.html"],
                                        "creator/files/postnumre.txt")
    print("Generating users")

    users = generator.generate(100)

    print("Finished generating users")


    print("Saving data")

    db = MongoConnector()
    db.create_users(users)

    print("Saved data")

