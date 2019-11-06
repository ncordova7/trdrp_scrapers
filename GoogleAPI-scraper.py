# Geoffrey Hughes
# Google API - Geoscrape by Location, radius, and key term

from source import scraper


print("hello")

center_lat = input("What latitude would you like to use for your center point: ")
center_long = input("What longitude would you like to use for your center point: ")
radius = input("How far from the center point would you like to gather from (miles): ")
keyword = input("What keyword would you like to use: ")


print("Searching ", radius, "miles surrounding", "(lat:", center_lat, "long:", center_long, ") for", keyword)
