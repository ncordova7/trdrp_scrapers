import sys
sys.path.append('../')
from source import scraper
import datetime
import yaml

with open(r'../keys.yaml') as file:
	keys = yaml.load(file, Loader=yaml.FullLoader)

weedmaps_json_site = keys['weedmaps']
source = "WEEDMAPS"
current = datetime.datetime.now()
date = current.strftime("%m-%d-%Y")

weedmap = scraper.scraper(weedmaps_json_site, source)
weedmap.connect()
weedmap.parse()
weedmap.output("weedmaps-" + date + ".csv")

print("All Done")
