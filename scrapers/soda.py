import pandas as pd
import json
from sodapy import Socrata
import yaml


with open(r'../keys.yaml') as file:
	keys = yaml.load(file, Loader=yaml.FullLoader)

soda_key = keys['soda']

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.lacity.org", #site
				 soda_key)			#api key

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.lacity.org,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.

results = client.get("63jg-8b9z", limit = 2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

results_df.to_csv(r'../output/soda.csv', index = None, header = True)

print("Success")