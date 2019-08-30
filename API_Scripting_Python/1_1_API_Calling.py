# 1 GET
#  Get information about an object

import requests
url = "http://jsonplaceholder.typicode.com/photos"
response = requests.get(url)
print(response.json())

# 2 POST
# Object does not exist yet

import requests
url = "http://jsonplaceholder.typicode.com/photos"
jsonPayload = { 'album': '1','title': 'TestTest', 'url': 'http://nothing.com','thumbnailUrl' : 'http://nothing.com'}
response = requests.post(url, json=jsonPayload)
print(response.json())

# 3 PUT
# Modify an existing object

import requests
url = "http://jsonplaceholder.typicode.com/photos/100"
jsonPayload = { 'album': '1','title': 'TestTest', 'url': 'http://nothing.com','thumbnailUrl' : 'http://nothing.com'}
response = requests.put(url, json=jsonPayload)
print(response.json())

# 4 DELETE
# Delete and existing object

import requests
url = "http://jsonplaceholder.typicode.com/photos/100"
response = requests.delete(url)
print(response.json())

