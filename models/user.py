from mongoengine import Document, StringField, ReferenceField
from models.address import Address


__author__ = 'Modulus'


class User(Document):
    meta = {
        "collection": "user"
    }

    first_name = StringField()
    last_name = StringField()
    address = ReferenceField(Address)

    def json(self):
        return {
            "id": str(self.id),
            "firstName": self.first_name,
            "lastName": self.last_name,
            "address": self.address
        }
