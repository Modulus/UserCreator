__author__ = 'Modulus'

from ming import Session, Document , create_datastore
from ming import schema
from ming.odm.property import Field

bind = create_datastore("test")
session = Session(bind)


class Address(Document):

    class __mongometa__:
        session = session
        name = "address"

    _id = Field(schema.ObjectId)
    code = Field(int)
    location = Field(str)
