import json
import requests


# pip install requests


api_query = "https://www.metaweather.com/api/location/44418/2013/4/27/"

response = requests.get(api_query)

print(response.status_code)
# print(response.content)

content = response.content

print(type(content))

parsed = json.loads(content)

print(type(parsed))

for index, line in enumerate(parsed):
    if index < 5:
        print(line["max_temp"])
