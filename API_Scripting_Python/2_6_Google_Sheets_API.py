################################################################################
# Install gspread using pip :  python -m pip install gpread
# Add the Google API for Python :  python -m pip google-api-python-client
# Google token 'C:/Learn/API_Scripting_Python/google_api/clientsecret.json'
# Spreadsheet in Google drive  ServiceAccountTest
# Link https://gspread.readthedocs.io/en/latest/
################################################################################


# Import gspread
import gspread


# Set up the authentication import the  ServiceAccountCredentials() module
from oauth2client.service_account import  ServiceAccountCredentials

#Set up the credentials

# Scope - tells what we are interacting with
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Create credentials using the Google API token
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Learn/API_Scripting_Python/google_api/clientsecret.json',scope)


# Create client using the credentials
client = gspread.authorize(creds)

#  Create sheet
# client.open() tells the client to open the spreadsheet, sheet1
sheet = client.open('ServiceAccountTest').sheet1
# Update the spreadsheet e.g. Adds 'test' to cell 1,1
sheet.update_cell(1,1,"test")

# Read data from the sheet e.g. from ServiceAccountTest row 1
# sheet.row_values(1)
print(sheet.row_values(1))

# Read all values from the spreadsheet
# sheet.get_all_values()
print(sheet.get_all_values())

# Complex Data using enumerate() function
# Write 1,2, and 3 in cells 11, 12 and 13
#       4,5, and 6  in cells 21  22 and 23, respectively
# 1. Loops over the list
# 2.  Gives the value at each point, gives index that corresponds to the value
#  row_index 0 and 1 (two rows of the sheet)
#  row  1,2,3,4,5,6
#   c00  c11  -> 1     c10 c21 -> 4
#   c01  c12  -> 2     c11 c22 -> 5
#   c02  c13  -> 3     c12 c23 -> 5
#

my_data = [[1,2,3],[4,5,6]]
for row_index, row in enumerate(my_data):
    for col_index, value in enumerate(row):
        sheet.update_cell(row_index+1, col_index+1, value)
    


