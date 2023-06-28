import requests
import json

r = requests.get(
    'https://api.cricapi.com/v1/series_info?apikey=78823c6f-7468-4118-ab87-8864c7dfdd03&id=c75f8952-74d4-416f-b7b4-7da4b4e3ae6e')
r = r.json()

json_object = json.dumps(r, indent=4)

with open("db.json", "w") as outfile:
    outfile.write(json_object)

# with open('db.json') as infile:
#     matches = json.load(infile)
#     matches = matches['data']['matchList']
#     print(type(matches))
#     matches.sort(key=lambda x: x['dateTimeGMT'])
#     for k, v in matches[1].items():
#         print(k, v)
