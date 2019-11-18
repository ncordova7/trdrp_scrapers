import pandas as pd
import requests
import json
import datetime
from pandas.io.json import json_normalize
import copy

#yelp_key
api_key= 'Hc_nfoPO2q93Qgi1DWsT7c9wSEyX18ePHX77m_QKRuP83K81Nf4yTnPmtCwYl-e6kAzKcz6324jZEvn2Db9QLHnt3C05FXY4CqxzEZSxbTgORr5dUhOoU_Yb4sa7XXYx'
url='https://api.yelp.com/v3/businesses/search'
search = 'dispensaries'
params={'term':search, 'location':'South Los Angeles'}
headers = {'Authorization': 'Bearer %s' % api_key}


def createRequest(headers, api_key, url, params):
    yelp_search = requests.get(url, params = params, headers= headers)
    search_results = yelp_search.json()
    search_results= copy.deepcopy(search_results['businesses'])
    df = pd.DataFrame.from_dict(json_normalize(search_results), orient = 'columns')
    return df


def editYelpData(df, desired_features):

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
    df = copy.deepcopy(df.rename(columns={'coordinates.longitude': 'longitude', 'coordinates.latitude': 'latitude',
                                         'location.address1': 'address', 'location.city': 'city',
                                          'location.country': 'country',
                                          'location.state': 'state', 'location.zip_code': 'zip_code'


                                         }))

    #add date and source columns
    df['SOURCE'] = source
    df['DATE_SCRAPED'] = d.strftime("%m-%d-%Y")
    #date scraped

    return df


desired_features = {"alias" :1, "url": 2, "coordinates.longitude": 3, "coordinates.latitude" : 4,
        "display_phone": 5, "id": 6, "location.address1": 7, "location.city" : 8, "location.country": 9,
         "location.state": 10, "location.zip_code" : 11, "name": 12,
        "phone": 13, "price": 14, "rating":15, "review_count" : 17,
        }
#----Get Reviews for dispensaires
desired_features_reviews = {"id" :1, "url": 2, "rating": 3, "text" : 4,
        "url": 5, "id": 6, "user.id": 7
        }

def editReviews(df, desired_features, store_name):

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

    return df

def getReviews(id, desired_features, store_name):
    url = "https://api.yelp.com/v3/businesses/" + id +"/reviews"
    req = requests.get(url, headers=headers)
    reviews = req.json()
    df1 = pd.DataFrame.from_dict(json_normalize(reviews['reviews']), orient = 'columns')
    df = editReviews(df1, desired_features, store_name)

    return df

#-----Main Code -----

testDF = createRequest(headers, api_key, url, params)
test1 = editYelpData(testDF, desired_features)
d = datetime.datetime.today()

test1Names = copy.deepcopy(test1)
reviews = pd.DataFrame([])
for index, row in test1Names.iterrows():
    id = row['id']
    store_name = row['name']

    df2 = getReviews(id, desired_features_reviews, store_name)
    reviews = copy.deepcopy(reviews.append(df2))
    print(id, store_name)


#write csv file
filename = "yelp_" + d.strftime("%m-%d-%Y") + ".csv"
test1.to_csv(r"output/" + filename, header = True, index = False)

filename1 = "yelp_reviews_" + d.strftime("%m-%d-%Y") + ".csv"
reviews.to_csv(r"output/" + filename1, header = True, index = False)

#connect to database
#database connection isnt working currently
