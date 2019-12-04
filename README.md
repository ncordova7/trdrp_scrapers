# Geo-Scraping South Los Angeles Toolset

![alt text][logo]

[logo]: https://d2mpqlmtgl1znu.cloudfront.net/AcuCustom/Sitename/DAM/017/LosAngeles_with_palms_Adobe.jpg

## What is this?

This toolset is a wrapper around the GoogleMaps, Yelp, Weedmaps, and LA City/County SODA API to help you scrape and aggregate spatial data for further analysis 

## How do I use this?

Follow instructions below to run our program
 
1. Download Python 3.7.4
2. cd into the repo run `pip install -r requirements.txt` on command line
3. Gather API Keys (Google, Yelp, SODA)
4. Open keys.yaml with a text editor and make changes to keywords for Google and Yelp scrapes
5. If running windows, double click scrape.bat. If running Mac or Linux, double click scrape.sh.
6. Look inside output folder for csv's containing scrape 

##### NOTE
If you would like to run each scrape individually, after finishing step 4, use command line to cd into the scrapers folder and run a python command to run specified scraper.

If you have no clue where to start for getting API keys please see below links

- [SODA API](https://dev.socrata.com/docs/app-tokens.html)
- [Google Places API](https://uaelementor.com/docs/get-google-places-api-key/)
- [Yelp API](https://rapidapi.com/blog/yelp-fusion-api-profile-pull-local-business-data/)
- [WeedMaps](https://stackoverflow.com/questions/50105364/scraping-menu-data-from-weedmaps)

If you are having issues running any of these files please feel free to email me at camargop@chapman.edu

## Uses for a program like this

Although this toolset was primarily made for Chapman's Crean College Health and Space Lab, it can be used for any location that each site hosts data for. For example: If you wanted to scrape location data of parks in Chicago, you would change the google latitude and longitude to the center point within Chicago and adjust the scrape radius.  

#### Elevator Pitch
Problem: Public Health and Public Admin Analysts are often frustrated by the effort it takes to manually record property types and locations for specific cities.
Solution: Our scrapers eliminate that problem!
Value: With our repo, you can spend less time collecting data and more time conducting analysis.
