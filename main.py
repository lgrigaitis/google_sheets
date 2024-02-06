import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1lhOiuoxjapZ5-if6ltRx2oZLzKSSQ4LO-g-t8KSZXP8"

workbook = client.open_by_key(sheet_id)
values_list = workbook.sheet1.row_values(1)


