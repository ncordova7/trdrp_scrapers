import requests
import json
import datetime
import pandas as pd
from pandas.io.json import json_normalize
import copy


class scraper:

    #constructor method

    def __init__(self, json_site, source):
        current = datetime.datetime.now()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

        self.date = current.strftime("%m-%d-%Y")
        self.json_site = json_site
        self.source = source
        self.resp = requests.get(json_site, headers = headers)
        self.dataframe1 = pd.DataFrame()


    def connect(self):

        if self.resp:
            print('Successfully connected to site!') #status 200
        else:
            print('An error occurred, please check internet connection and try rerunning the script')
            exit()


    def parse(self):
        count = 0
        #data converted into json
        data = self.resp.json()
        #grab the list of stores from nested json
        stores = data['data']['listings']

        #convert stores json into a pandas dataframe
        df = pd.DataFrame.from_dict(json_normalize(stores), orient = 'columns')

        #dictionary of features from json
        desired_features = {"name" :1, "address": 2, "longitude": 3, "latitude" : 4,
        					"state": 5, "city": 6, "zip_code": 7}

        #, "ranking" : 8, "rating": 9, "web_url": 10, "reviews_count": 11, "license_type" : 12, "type": 13, "retailer_services": 14

        #loop through defined features and if a column is not there create one and put null values
        for i in desired_features:
            if(i not in df.columns):
                df[i] = None

        #drop columns not desired
        for i in df.columns:
            if(i not in desired_features):
                df = copy.deepcopy(df.drop(columns = [i]))

        #add date column
        df["DATE_SCRAPED"] = self.date
        df["SOURCE"] = self.source
        #print("Dispensaries Scraped Dimensions (rows by columns): ", df.shape)

        # RENAMING
        df = df.rename(columns={"name": "BUSINESS_NAME", "address": "ADDRESS", "state": "STATE",
    													  "city": "CITY", "zip_code": "ZIPCODE", "latitude": "LATITUDE", 
    													  "longitude": "LONGITUDE"})

        # FILLING NULL VALUES WITH "NA"
        df = df.fillna("NA", inplace = True)

        #ERROR HERE. GET NONE TYPE 
        # cols = ['BUSINESS_NAME', 'ADDRESS', 'STATE', 'CITY', 'ZIPCODE', 'LATITUDE', 'LONGITUDE','DATE_SCRAPED','SOURCE']
        # df.reindex(columns = cols)

        #df = df[['BUSINESS_NAME', 'ADDRESS', 'STATE', 'CITY', 'ZIPCODE', 'LATITUDE', 'LONGITUDE','DATE_SCRAPED','SOURCE']]
        
        #ERROR HERE. GET NONE TYPE 
        self.dataframe1 = df

        #THIS METHOD GIVES ME THE SAME ERROR
        #self.dataframe1[['BUSINESS_NAME', 'ADDRESS', 'STATE', 'CITY', 'ZIPCODE', 'LATITUDE', 'LONGITUDE','DATE_SCRAPED','SOURCE']]


    def output(self, filename):
    	
    	# self.dataframe1 = self.dataframe1.rename(columns={"name": "BUSINESS_NAME", "address": "ADDRESS", "state": "STATE",
    	# 												  "city": "CITY", "zip_code": "ZIPCODE", "latitude": "LATITUDE", 
    	# 												  "longitude": "LONGITUDE"})

    	# self.dataframe1 = self.dataframe1.fillna("NA", inplace = True)

    	# self.dataframe1[['BUSINESS_NAME', 'ADDRESS', 'STATE', 'CITY', 'ZIPCODE', 'LATITUDE', 'LONGITUDE','DATE_SCRAPED','SOURCE']]
    	self.dataframe1.to_csv(r"../output/" + filename, header = True, index = False)