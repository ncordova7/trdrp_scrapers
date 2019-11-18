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


#-----Main Code -----

testDF = createRequest(headers, api_key, url, params)
test1 = editYelpData(testDF, desired_features)
d = datetime.datetime.today()

#write csv file
filename = "yelp_" + d.strftime("%m-%d-%Y") + ".csv"
test1.to_csv(r"output/" + filename, header = True, index = False)

#connect to database
#database connection isnt working currently
