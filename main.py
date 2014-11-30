__author__ = 'Modulus'

from creator import user_generator
from db.mongo_connector import create_users


if __name__ == "__main__":
    generator = user_generator.UserGenerator("offline", ["creator/files/boy_names_ssb.html", "creator/files/girl_names_ssb.html"],
                                        ["creator/files/sur_names_1_ssb.html", "creator/files/sur_names_2_ssb.html"],
                                        "creator/files/postnumre.txt")
    # generator.
    print("Generating users")

    users = generator.generate(amount=10)

    print("Finished generating users")

    print("Saving data")

    create_users(users)

    print("Saved data")

