import pandas as pd
import requests
import json
import datetime
from pandas.io.json import json_normalize
import copy
import yaml
import os
import numpy as np

#yelp_key
#api_key= 'CuTMcKvzJtwEZ-8M6NjD5xMIk5DAjsyyVHOtX_J5uBrQ2U9FpLdC6JJz-aXj6fAreU_MrxWZsbrXUwlW9C_-ApCwprt6ApVkx83A7Cv_eXl1bNCrakenUhAynJLkXXYx'
#with open(r'../keys.yaml') as file:
	#keys = yaml.load(file, Loader=yaml.FullLoader)

#api_key = keys['yelp']
#url='https://api.yelp.com/v3/businesses/search'
#search = 'dispensaries'
#params={'term':search, 'location':'South Los Angeles'}
#headers = {'Authorization': 'Bearer %s' % api_key}

def createRequest(headers, api_key, url, params):
    yelp_search = requests.get(url, params = params, headers= headers)
    search_results = yelp_search.json()
    for i in search_results:
        if(i == "error"):
            print("yelp api is internally unstable, api call skipped")

            #return 0 to indicate a skip
            return 0
        else:
            search_results= copy.deepcopy(search_results['businesses'])
            df = pd.DataFrame.from_dict(json_normalize(search_results), orient = 'columns')
            return df


def editYelpData(df, desired_features, business_type):

    source = "yelp"
    d = datetime.datetime.today()
    #loop through defined deatures and if a column is not there create one and put null values
    if(type(df) is not pd.DataFrame):
        #print(business_type, " establishments skipped")
        df = 0
        return df
        # skip due to yelp api issues
    else:
        for i in desired_features:
            if(i not in df.columns):
                df[i] = None
        #drop columns not desired
        for i in df.columns:
            if(i not in desired_features):
                df = copy.deepcopy(df.drop(columns = [i]))

                #rename columns
        df = copy.deepcopy(df.rename(columns={'coordinates.longitude': 'LONGITUDE', 'coordinates.latitude': 'LATITUDE',
                                         'location.address1': 'ADDRESS', 'location.city': 'CITY',
                                          'location.country': 'COUNTRY',
                                          'location.state': 'STATE', 'location.zip_code': 'ZIPCODE',
                                          'name': "BUSINESS_NAME"



                                         }))
        #add date and source columns
        df['SOURCE'] = source
        df['DATE_SCRAPED'] = d.strftime("%m-%d-%Y")
        df['PROPERTYTYPE'] = business_type
        df = df.fillna("NA")
        return df


desired_features = {"alias" :1, "url": 2, "coordinates.longitude": 3, "coordinates.latitude" : 4,
        "display_phone": 5, "id": 6, "location.address1": 7, "location.city" : 8, "location.country": 9,
         "location.state": 10, "location.zip_code" : 11, "name": 12,
        "phone": 13, "price": 14, "rating":15, "review_count" : 17,"PROPERTYTYPE": 18
        }
#----Get Reviews for dispensaires
desired_features_reviews = {"id" :1, "url": 2, "rating": 3, "text" : 4,
        "url": 5, "id": 6, "user.id": 7,"PROPERTYTYPE": 8
        }

def editReviews(df, desired_features, store_name, business_type):

    source = "yelp"
    d = datetime.datetime.today()
    #loop through defined deatures and if a column is not there create one and put null values
    for i in desired_features:
            if(i not in df.columns):
                df[i] = None

    #drop columns not desired
    for i in df.columns:
        if(i not in desired_features):
            df = copy.deepcopy(df.drop(columns = [i]))

    #rename columns
    df = copy.deepcopy(df.rename(columns={'user.id': 'user_id', 'id': 'review_id',
                                          'location.city': 'city',
                                          'url': 'review_url',
                                         }))

    #add date and source columns
    df['Store_name'] = store_name
    df['SOURCE'] = source
    df['DATE_SCRAPED'] = d.strftime("%m-%d-%Y")
    df['PROPERTYTYPE'] = business_type
    df = df.fillna("NA")



    return df


def getReviews(id, desired_features, store_name, business_type):
    url = "https://api.yelp.com/v3/businesses/" + id +"/reviews"
    req = requests.get(url, headers=headers)
    reviews = req.json()
    #print("here is the error")
    #print(reviews)
    #yelp api is unstable at times to avoid errors check to see if json returns errors
    for i in reviews:
        if(i == "error"):
            print("yelp api unstable, store: ", store_name, " skipped")
        else:
            df1 = pd.DataFrame.from_dict(json_normalize(reviews['reviews']), orient = 'columns')
            df = editReviews(df1, desired_features, store_name, business_type)
            return df

#-----Main Code -----
with open(r'../keys.yaml') as file:
	keys = yaml.load(file, Loader=yaml.FullLoader)

api_key = keys['yelp']
#api_key= 'CuTMcKvzJtwEZ-8M6NjD5xMIk5DAjsyyVHOtX_J5uBrQ2U9FpLdC6JJz-aXj6fAreU_MrxWZsbrXUwlW9C_-ApCwprt6ApVkx83A7Cv_eXl1bNCrakenUhAynJLkXXYx'
url='https://api.yelp.com/v3/businesses/search'

keywords = {"dispensary": "dispensary"}
for key in keys['keywords']:
    print("Currently pulling all reviews for all: ", key, " establishments")
    search = str(key)
    params={'term':search, 'location':'South Los Angeles'}
    headers = {'Authorization': 'Bearer %s' % api_key}
    testDF = createRequest(headers, api_key, url, params)
    #print(testDF)
    test1 = editYelpData(testDF, desired_features, search)
    if(type(test1) is not pd.DataFrame):
        print(search, " establishments skipped")
    else:
        test1 = copy.deepcopy(test1.replace(r'^\s*$', np.nan, regex=True))
        test1 = copy.deepcopy(test1.fillna("NA"))
        d = datetime.datetime.today()
        test1Names = copy.deepcopy(test1)
        reviews = pd.DataFrame([])
        for index, row in test1Names.iterrows():
            id = row['id']
            store_name = row['BUSINESS_NAME']
            df2 = getReviews(id, desired_features_reviews, store_name, search)
            reviews = copy.deepcopy(reviews.append(df2))
            print(id, store_name)
        reviews = copy.deepcopy(reviews.replace(r'^\s*$', np.nan, regex=True))
        reviews = copy.deepcopy(reviews.fillna("NA"))
        #write csv file
        filename = "yelp_" + d.strftime("%m-%d-%Y") + ".csv"
        filename1 = "yelp_reviews_" + d.strftime("%m-%d-%Y") + ".csv"

        with open(r"../output/" + filename, 'a') as f:
            test1.to_csv(f, mode='a', header=f.tell()==0)

        with open(r"../output/"+ filename1, 'a') as k:
            reviews.to_csv(k, mode='a', header=k.tell()==0)
        #if not os.path.isfile(filename):
            #test1.to_csv(r"../output/" + filename, header = True)
        #else:
            #test1.to_csv(r"../output/" + filename, mode='a', header=False)

        #if not os.path.isfile(filename1):
        #    reviews.to_csv(r"../output/" + filename1, header = True)
        #else:
        #    reviews.to_csv(r"../output/" + filename1, mode='a', header=False)
    #filename = "yelp_" + d.strftime("%m-%d-%Y") + ".csv"
    #test1.to_csv(r"../output/" + filename, header = True, index = False)

    #filename1 = "yelp_reviews_" + d.strftime("%m-%d-%Y") + ".csv"
    #reviews.to_csv(r"../output/" + filename1, header = True, index = False)


    print("success...")
