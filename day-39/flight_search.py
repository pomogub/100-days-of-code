from os import environ
import requests
import requests_cache
from dotenv import load_dotenv

load_dotenv()
requests_cache.install_cache('flight_cache')


class FlightSearch:

    def __init__(self):
        self.api_key = environ['SERP_API']
        self.endpoint = 'https://serpapi.com/search'

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
          'engine': 'google_flights',
          'departure_id': origin_city_code,
          'arrival_id': destination_city_code,
          'outbound_date': from_time,
          'return_date': to_time,
          'type': '1',
          'adults': '1',
          'currency': 'USD',
          'api_key': self.api_key,
         }
        flight_response = requests.get(url=self.endpoint, params=params)
        data = flight_response.json()
        return data
