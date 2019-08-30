# 3 PUT
# Modify an existing object

import requests
url = "http://jsonplaceholder.typicode.com/photos/100"
jsonPayload = { 'album': '1','title': 'TestTest', 'url': 'http://nothing.com','thumbnailUrl' : 'http://nothing.com'}
response = requests.put(url, json=jsonPayload)
#print(response.json())
response.json()