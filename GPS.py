__author__ = 'Mandar'
import json
import googlemaps
from googlemaps import Client
def getgeo(address):
    gmaps = Client('AIzaSyA3i4VXAqU2qmSXKQ3ve4htc_QNxLaJpW4')
    json_response = gmaps.geocode(address)
    dictionary= json_response[0]['geometry']['location']
    return dictionary[u'lat'],dictionary[u'lng']
