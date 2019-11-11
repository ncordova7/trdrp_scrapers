# Geoffrey Hughes
# Google API - Geoscrape by Location, radius, and key term

# pip install googlemaps
# pip install prettyprint

import googlemaps
import pprint
import time

from source import scraper

# Our google API key
API_key = "AIzaSyCfCXdXfjYPd8nAii9dPFVPUjYIBzBf4vo"

# Our Google Maps client
maps = googlemaps.Client(key = API_key)

# GET Search parameters
print("WELCOME!")
print("* note: South LA we're using: 33.989421 lat, -118.301495 long")
center_lat_in = input("What latitude would you like to use for your center point: ")
center_long_in = input("What longitude would you like to use for your center point: ")
print("* note: 7 miles is about 11265 meters")
radius_in = input("How far from the center point would you like to gather from (radius in meters): ")
keyword_in = input("What keyword would you like to search for: ")
print("Searching ", radius_in, "miles surrounding", "(lat:", center_lat_in, "long:", center_long_in, ") for", keyword_in)

# Starting point
starting_point = "%s,%s" % (center_lat_in,center_long_in)
print(starting_point)

# Search places with paramets
google_places = maps.places_nearby(location = starting_point, radius = int(radius_in), open_now = False, keyword = keyword_in)


# Output in JSON
pprint.pprint(google_places)

for place in google_places['results']:

    # place ID
    this_place_ID = place['place_id']

    # Send back these fields
    this_fields = ['name', 'geometry/location/lat', 'geometry/location/lng', 'rating', 'type']

    this_place_details = maps.place(place_id = this_place_ID, fields = this_fields)

    # Print formetted results
    print(this_place_details)




""" Maybe use Sul's JSON scraper
source = "Google Maps"

gmaps = scraper.scraper(google_places, source)
gmaps.connect()
gmaps.parse()
gmaps.output("gmaps_places.csv")

"""
