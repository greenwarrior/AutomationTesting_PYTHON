#############################################################################
# 1 No authentication provided
#     response = requests.get(url)
# 2  auth = () Authentication is provided
#     response = requests.get(url, auth=('greenwarrior', 'Green1978!'))
# 3  Using token
#    get(url, headers = {'Authorization' : 'Bearer copied token'})
#  To obtain the github token:
#   Settings -> Developer Settings -> Personal Access Tokers ->
#         Generate new token -> Enter the notes -> Check off the required access
#         e.g. users -> Generate token -> Copy the token
##############################################################################
import requests


url = 'https://api.github.com/user'
# 1 No login authentication provided
# response = requests.get(url)
# 2 Authentication is provided
#response = requests.get(url, auth=('greenwarrior', 'password1'))
# 3
response = requests.get(url, headers={'Authorization':'Bearer Token'})
print(response.json())



