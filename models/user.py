from ming import Session
from ming.odm.declarative import MappedClass
from ming import schema
from ming.odm.odmsession import ODMSession
from ming.odm.property import FieldProperty, RelationProperty
from models.address import Address

__author__ = 'Modulus'


class User(MappedClass):

    class __mongometa__:
        session = ODMSession(doc_session=Session())
        name = "user"
        _id = FieldProperty(schema.ObjectId)

    firstName = FieldProperty(str)
    lastName = FieldProperty(str)
    address = FieldProperty(Address)

    def __init__(self, first_name, last_name, address):
        self.firstName = first_name.encode("utf-8")
        self.firstName = last_name.encode("utf-8")
        self.address = address
