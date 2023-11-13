import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightData:
    def __init__(self, to_city):
        self.data = self.get_response_data(to_city)
        self.price = self.data["price"]
        self.departure_airport_code = self.data["cityCodeFrom"]
        self.departure_city = self.data["cityFrom"]
        self.arrival_airport_code = self.data["cityCodeTo"]
        self.arrival_city = self.data["cityTo"]
        self.departure_date = self.data["local_departure"].split("T")[0]
        self.arrival_date = self.data["local_arrival"].split("T")[0]

    def get_response_data(self, to_city):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        end_date = datetime.datetime.now() + datetime.timedelta(days=6 * 30)

        parameters = {
            "fly_from": "LON",
            "fly_to": to_city,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": end_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 27,
            "one_for_city": 1,
            "curr": "GBP"
        }
        data = None
        try:
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=parameters, headers=headers)
            response.raise_for_status()
            data = response.json()["data"][0]
        except:
            data = None
        finally:
            return data
