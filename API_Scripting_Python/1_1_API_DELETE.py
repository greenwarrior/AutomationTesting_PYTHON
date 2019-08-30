# 4 DELETE
# Delete and existing object

import requests
url = "http://jsonplaceholder.typicode.com/photos/100"
response = requests.delete(url)
#print(response.json())
response.json()
