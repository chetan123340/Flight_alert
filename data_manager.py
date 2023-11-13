import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    def __init__(self):
        self.sheet_data = []

    def get_sheet_data(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.response.raise_for_status()
        self.sheet_data = self.response.json()["prices"]
        return self.sheet_data

    def update_iata(self, row_id, iata_code):
        parameters = {
            "price": {
                "iataCode": iata_code
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=parameters, headers=headers)
