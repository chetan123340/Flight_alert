from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

sheet_data = data_manager.get_sheet_data()

for row in sheet_data:
    if row["iataCode"] == "":
        data_manager.update_iata(row["id"], flight_search.get_iata_code(row["city"]))
    curr_flight_data = FlightData(row["iataCode"])
    if curr_flight_data.price < row["lowestPrice"]:
        notification.send_message(curr_flight_data)
    print(f"{curr_flight_data.arrival_city} : {curr_flight_data.price}")


