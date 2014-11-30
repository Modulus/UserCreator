__author__ = 'Modulus'


def extract(postal_number):
    base_url = "http://www.geonames.org/postalcode-search.html?q={query}&country=NO"
    q_url = base_url.format(query=postal_number)

    return q_url