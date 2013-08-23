from ming import Session, Document, create_datastore
from ming import schema
from ming.odm.property import Field
from models.address import Address


__author__ = 'Modulus'

bind = create_datastore("test")
session = Session(bind)


class User(Document):

    class __mongometa__:
        session = session
        name = "user"

    _id = Field(schema.ObjectId)
    firstName = Field(str)
    lastName = Field(str)
    address = Field(Address)
