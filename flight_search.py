import requests
import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    def __init__(self):
        pass

    def get_iata_code(self, place):
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "term": place,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=headers)
        return response.json()["locations"][0]["code"]
