#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import requests
import json
import datetime
from pandas.io.json import json_normalize


# In[54]:


weedmaps_json_site = "https://api-g.weedmaps.com/discovery/v1/listings?sort_by=position&filter%5Blocation%5D=any&latlng=33.96210098266602%2C-118.2745513916016&page_size=100&page=1"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


# In[55]:


r = requests.get(weedmaps_json_site, headers = headers)


# In[64]:


r


# In[65]:


data = r.json()


# In[66]:


data


# In[67]:


stores = data['data']['listings']


# In[68]:


count = 0
for i in stores:
    count += 1
    print('----------')
    print(count)
    print(i)


# In[69]:


df = pd.DataFrame.from_dict(json_normalize(stores), orient = "columns")


# In[70]:


df['name']


# In[71]:


df.info()


# In[83]:


api_cid = 'oAYGHKSZvK_Az-ZQ4UyTGQ'
api_key= 'Hc_nfoPO2q93Qgi1DWsT7c9wSEyX18ePHX77m_QKRuP83K81Nf4yTnPmtCwYl-e6kAzKcz6324jZEvn2Db9QLHnt3C05FXY4CqxzEZSxbTgORr5dUhOoU_Yb4sa7XXYx'


# In[84]:


headers = {'Authorization': 'Bearer %s' % api_key}


# In[117]:


#search = 'dispensaries'
#location = 'South LA'
search = 'LA Cannabis Co - Inglewood'


# In[118]:


url='https://api.yelp.com/v3/businesses/search'
params={'term':search, 'location':'South Los Angeles'}


# In[119]:




yelp_search = requests.get(url, params = params, headers= headers)


# In[120]:


yelp_search


# In[121]:


search_results = yelp_search.json()


# In[122]:


search_results


# In[109]:


for i in search_results:
    print(i)


# In[123]:


count = 0

for i in search_results['businesses']:
    count += 1
    print('--------')
    print(count)
    if(i['name'] == 'LA Cannabis Co - Inglewood'):
        print(i)
    #print(i)


# In[124]:


url = "https://api.yelp.com/v3/businesses/0zyJAQK15vOidZlc8ObknA/reviews"
req = requests.get(url, headers=headers)


# In[125]:


reviews = req.json()


# In[126]:


for i in reviews['reviews']:
    print(i)


# In[128]:


#count = df['names'].count()


# In[ ]:





# In[ ]:




