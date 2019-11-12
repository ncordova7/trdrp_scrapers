import yaml

with open(r'source/keys.yaml') as file:
	keys = yaml.load(file, Loader=yaml.FullLoader)

print(keys)

google = keys['google'] 

print(google)