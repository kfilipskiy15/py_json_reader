import json
from pprint import pprint

with open('test1.json') as f:
    data = json.load(f)
print("chest")
pprint(data["volume_parameters"]["chest"])