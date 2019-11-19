# Geoffrey Hughes
# Google API - Geoscrape by Location, radius, and key term

# pip install googlemaps
# pip install prettyprint

import googlemaps
import pprint
import time
import pandas as pd
from pandas.io.json import json_normalize
import json

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
google_places = maps.places_nearby(location = starting_point, radius = int(radius_in), open_now = False, name = keyword_in)


# Output in JSON
pprint.pprint(google_places)

for place in google_places['results']:

    # place ID
    this_place_ID = place['place_id']

    # Send back these fields
    this_fields = ['name', 'geometry/location/lat', 'geometry/location/lng', 'place_id']

    this_place_details = maps.place(place_id = this_place_ID, fields = this_fields)

    # Print formetted results
    print(this_place_details)

#places_results = google_places['results']

for key in list(google_places):
    if (key != 'results' and key != 'name' and key != 'geometry/location/lat' and key != 'geometry/location/lng' and key != 'place_id'):
        del google_places[key]

places_results = google_places['results']


df = pd.DataFrame.from_dict(json_normalize(places_results), orient = 'columns')
print(df)


#df = pandas.DataFrame(google_places)
#df.to_csv()
#print(df)
#for i in google_places:
#    print(i)
filename = "google_places.csv"

df.to_csv(r"output/" + filename, header = True, index = False)


"""
# Maybe use Sul's JSON scraper
source = "Google Maps"

gmaps = scraper.scraper(google_places, source)
gmaps.connect()
gmaps.parse()
gmaps.output("gmaps_places.csv")



api = GooglePlaces(API_key)

for place in google_places:
    details = api.get_place_setails(place['place_id'], fields)
    try:
        website = details['result']['website']
    except KeyError:
        website = ""

    try:
        name = details['result']['name']
    except KeyError:
        name = ""

    try:
        address = details['result']['formatted_address']
    except KeyError:
        address = ""

    try:
        phone_number = details['result']['international_phone_number']
    except KeyError:
        phone_number = ""

    try:
        reviews = details['result']['reviews']
    except KeyError:
        reviews = []
    print("===================PLACE===================")
    print("Name:", name)
    print("Website:", website)
    print("Address:", address)
    print("Phone Number", phone_number)
    print("==================REVIEWS==================")
    for review in reviews:
        author_name = review['author_name']
        rating = review['rating']
        text = review['text']
        time = review['relative_time_description']
        profile_photo = review['profile_photo_url']
        print("Author Name:", author_name)
        print("Rating:", rating)
        print("Text:", text)
        print("Time:", time)
        print("Profile photo:", profile_photo)
        print("-----------------------------------------")


"""
