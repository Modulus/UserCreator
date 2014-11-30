# -*- coding: utf-8 -*-
from mongoengine import Document, StringField, PointField

__author__ = 'Modulus'


class Address(Document):

    meta = {
        "collection": "address"
    }

    #Fylke in norwegian
    county = StringField(required=True)
    #Kommune in Norwegian
    municipality = StringField(required=True)
    code = StringField(required=True)
    location = StringField(required=True)
    coordinates = PointField(required=True)
    country = StringField()

    def json(self):
        return {
            "county": self.county,
            "municipality": self.municipality,
            "code": self.code,
            "location": self.location,
            "coordinates": self.coordinates,
            "country": self.country
        }

    def csv(self):
        return "{county},{municipality},{code},{location},{coordinates},{country};\n".\
            format(
                county=self.county,
                municipality=self.municipality,
                code=self.code,
                location=self.location,
                coordinates=self.coordinates,
                country=self.country,
            )