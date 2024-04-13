from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from data import spreadsheet

def update_values(spreadsheet_id, range_name, value_input_option, _values):
    """
    Updates the value of a cell in a Google Sheet.
    """
    try:
        credentials_file = 'credentials.json'  # Specify the path to your service account key file
        creds = Credentials.from_service_account_file(
            credentials_file,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        service = build("sheets", "v4", credentials=creds)
        body = {"values": _values}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def update_google_sheet(value_to_update, cell: str):
    # Specify the spreadsheet ID and range
    spreadsheet_id = spreadsheet
    range_name = f"Accounts!{cell}"

    # Update the value in the spreadsheet
    update_values(
        spreadsheet_id,
        range_name,
        "USER_ENTERED",
        [[value_to_update]],
    )

if __name__ == "__main__":
    # Specify the spreadsheet ID and range
    spreadsheet_id = spreadsheet
    range_name = "Accounts!A2"

    # Specify the value to be updated
    value_to_update = [['a']]

    # Update the value in the spreadsheet
    update_values(
        spreadsheet_id,
        range_name,
        "USER_ENTERED",
        value_to_update,
    )
