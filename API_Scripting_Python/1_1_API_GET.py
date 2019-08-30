# 1 GET
#  Get information about an object

import requests
url = "http://jsonplaceholder.typicode.com/photos"
response = requests.get(url)
print(response.json())