# 2 POST
# Object does not exist yet

import requests
url = "http://jsonplaceholder.typicode.com/photos"
jsonPayload = { 'album': '1','title': 'TestTest', 'url': 'http://nothing.com','thumbnailUrl' : 'http://nothing.com'}
response = requests.post(url, json=jsonPayload)
print(response.json())