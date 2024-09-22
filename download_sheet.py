from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Google Sheet ID
SHEET_ID = "11OcQz1Vk3ofny3Ql7wN-XlHkZwub-hojt-fO094SxiI"

# Authenticate and create the service
creds = Credentials.from_authorized_user_file('token.json')
service = build('sheets', 'v4', credentials=creds)

# Get all sheet metadata
sheet_metadata = service.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
sheets = sheet_metadata.get('sheets', [])

# Loop through each sheet and download the data
for sheet in sheets:
    sheet_name = sheet['properties']['title']
    print(f"Downloading data from sheet: {sheet_name}")
    
    # Define the range as the entire sheet
    range_name = f'{sheet_name}'
    
    # Fetch the data from the sheet
    result = service.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=range_name).execute()
    values = result.get('values', [])

    # Print the values (or handle the data as needed)
    if not values:
        print(f'No data found in sheet: {sheet_name}')
    else:
        for row in values:
            print(row)
