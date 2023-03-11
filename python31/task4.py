import requests
import json

my_req = requests.get('https://swapi.dev/api/people/3/')

data = json.loads(my_req.text)
data['name'] = 'Ivan'

with open('my_new_json', 'w') as file:
    json.dump(data, file, indent=4)

my_req2 = requests.get('https://swapi.dev/api/planets/8/')

data2 = json.loads(my_req2.text)

with open('my_new_json2', 'w') as file2:
    json.dump(data, file2, indent=4)