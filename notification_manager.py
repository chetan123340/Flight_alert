from twilio.rest import Client
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUM = os.getenv("TWILIO_NUM")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, curr_fight_data: FlightData):
        self.client.messages.create(
            body=f"Low Price ALERT !! Only £{curr_fight_data.price} to fly from {curr_fight_data.departure_city}-{curr_fight_data.departure_airport_code} to {curr_fight_data.arrival_city}-{curr_fight_data.arrival_airport_code}, from {curr_fight_data.departure_date} to {curr_fight_data.arrival_date}",
            from_=TWILIO_NUM,
            to='+919902554506'
        )
