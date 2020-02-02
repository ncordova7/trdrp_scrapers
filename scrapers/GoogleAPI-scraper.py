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
import yaml


with open(r'../keys.yaml') as file:
	keys = yaml.load(file, Loader=yaml.FullLoader)


# Get google API key
API_key = keys['google']

center_lat_in = keys['google_lat']
center_long_in = keys['google_lng']
radius_in = keys['google_radius']

# Get keywords from YAML file
keywords = keys['keywords']

for keyword in keywords:
    print(keyword)


# Our Google Maps client
maps = googlemaps.Client(key = API_key)


# Starting point
starting_point = "%s,%s" % (center_lat_in,center_long_in)
print(starting_point)



for keyword in keywords:
    google_places = maps.places_nearby(location = starting_point, radius = int(radius_in), open_now = False, name = keyword)
    places_results = google_places['results']
    df = pd.DataFrame.from_dict(json_normalize(places_results), orient = 'columns')

	# RENAMING
    df = df.rename(columns={"name": "BUSINESS_NAME", "address": "ADDRESS", "state": "STATE", "city": "CITY", "zip_code": "ZIPCODE", "latitude": "LATITUDE", "longitude": "LONGITUDE"})

	# FILLING NULL VALUES WITH "NA"
    df = df.fillna("NA")

    df.to_csv(r"../output/" + "google_" + keyword + ".csv", header = True, index = False)

    print(df)
