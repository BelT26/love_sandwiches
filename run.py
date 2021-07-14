import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

newline = '\n'

def get_sales_data():
    """
    get sales figures from user
    """
    while True:
        print('Please enter sales data from the last market day')
        print('Data should be six numbers separated by commas')
        print('For example: 1,3,6,4,12,5\n')
        data_str = input('Enter your data here:')
        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print('Thank you for your valid data!')
            break
    return sales_data

def validate_data(values):
    """
    inside the try check that all inputs can be converted to integers
    raise a ValueError if value cannot be parsed or
    if there are not exactly 6 numbers
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f'6 values expected. You provided {len(values)}')
    except ValueError as e:
        print(f"Invalid data {e}. Please try again{newline}")
        return False
    return True


def update_sales_worksheet(data):
    """Update sales worksheet. Add new row with data provided
    """
    print('Updating sales worksheet...\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet updated successfully! \n')


def calculate_surplus(sales_row):
    """compares sales with stock and calculates surplus"""
    print('Calculating surplus data...\n')
    stock = SHEET.worksheet('stock').get_all_values()
    pprint(stock)
    stock_row = stock[-1]
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data


def main():
    """ run main program functions"""
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    print(sales_data)
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus(sales_data)
    print(new_surplus_data)


print('Welcome to Love Sandwiches data automation')
main()
