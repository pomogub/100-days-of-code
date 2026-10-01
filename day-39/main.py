#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime, timedelta

tomorrow = datetime.today() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(weeks=26)

# data_manager = DataManager()
# sheet_data = data_manager.get_destinations()

flight = FlightSearch()
pprint(flight.check_flights(
    origin_city_code='LHR',
    destination_city_code='CDG',
    from_time='2026-10-10',
    to_time='2026-10-11'
)
)
