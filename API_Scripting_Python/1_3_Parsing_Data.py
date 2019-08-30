#############################################################################
# 1 Accessing the keys or values of the dictionary using the for loop
#   e.g. my_json.keys()
#   e.g. my_json.values()
# 2 To find the value of a specific key
#    dictionary_name[key]
#    e.g. my_json['id']
##############################################################################
import requests


url = 'https://api.github.com/user'
# 1 No login authentication provided
# response = requests.get(url)
# 2 Authentication is provided
#response = requests.get(url, auth=('greenwarrior', 'password1'))
# 3
response = requests.get(url, headers={'Authorization':'Bearer Token'})
# Assign the response to a dictionary called my_json
my_json = response.json()

# Print each  the key in the dictionary using the for loop
for key in my_json.keys():
    print(key)

# Print the value of the key 'id'
print(my_json['id'])




