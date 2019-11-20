Geoffrey Hughes's README

For Data Comm Final Project: Geoscraping South LA



I have figured out how to gather geocoding data for a location using the Google API. This gathers a JSON file with location data that we can convert to CSV for use in the project.

My contribution has been the Google API, using the key, and starting a python script that will take in a search term and location, and then spit out places relevant to the search term within an x mile radius of the input location.

I still need to finish that very python script.

I plan to have the python script implemented, and work with my team to figure out the initial location, the radius we want to explore, and what data (if not just latitude and longitude coordinates) we need to take from the JSON file and export to CSV for use in the project.


11/19/19 UPDATE:
Updated GoogleAPI-scraper.py to not store any variables and instead take them in from a YAML document in our project folder.
This makes it a lot easier and convenient to modify in the future.
I also made it so that multiple search terms can be taken in (from the YAML file) and it outputs a CSV for each of the search terms. (Big improvement)

All these improvements were my goal for today, and now I am working on modifying the output .csv files (modifying the pandas df) to only return the column (variables) we want! This next goal should be done within a few days.
