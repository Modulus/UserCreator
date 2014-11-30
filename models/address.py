from mongoengine import Document, StringField, PointField

__author__ = 'Modulus'


class Address(Document):

    meta = {
        "collection": "address"
    }

    code = StringField()
    location = StringField()
    coordinates = PointField()
