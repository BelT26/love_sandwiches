import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE) 
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 
SHEET = GSPREAD_CLIENT.open('love_sandwiches') 

def get_sales_data():
    """
    get sales figures from user
    """
    print('Please enter sales data from the last market day')
    print('Data should be six numbers separated by commas')
    print('For example: 1,3,6,4,12,5\n')

    data_str = input('Enter your data here:')
    print(f'The data provided is {data_str}')

get_sales_data()    