import argparse
import request

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--token', required=True, help='Access token for Google API')

# Parse the command-line arguments
args = parser.parse_args()

# Access the token
access_token = args.token
print(f"Access Token: {access_token}")


SPREADSHEET_ID = "1gFPuDW8U_LvKiyQ1B6LqMh0E7REEy68lxR914bkhMMg"
SHEET_NAME = "Sheet2_tmp"

# Google Sheets API URL for retrieving the sheet data
url = f'https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{SHEET_NAME}'

# Set up headers with access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Step 1: Retrieve the data from the Google Sheet
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json().get('values', [])
    
    # Step 2: Write the data to a CSV file
    with open('sheet_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
    
    print("Data exported to 'sheet_data.csv'.")
else:
    print(f"Error: {response.status_code}, {response.text}")
