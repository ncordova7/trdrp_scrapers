# trdrp_scrapers
tools used to help with Health and Space Lab research 
Suleiman Karkoutli

I refactored the weedmaps API scrapper script to use the open source Pandas package. 
This reduced the amount of lines of code needed to parse the json and makes maintaining the code easier.  
The script's logic has been implemented for our other APIs. 

Planning to do next:
I plan on incorporating the Yelp API in order to get review data for each of our dispensaries.
This will then be used in coordination with the Weedmaps API to mine sentiment. 
I also plan on writing a script to easily append our dataframes to our google cloud server databases and enforcing data integrity checks along the way. 
