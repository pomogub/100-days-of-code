from os import environ
import requests
import requests_cache
from dotenv import load_dotenv

load_dotenv()
requests_cache.install_cache('sheet_cache')


class DataManager:

    def __init__(self):
        self.token = environ['TOKEN']
        self.header = {'Authorization': f'Bearer {self.token}'}
        self.destinations = {}

    def get_destinations(self):
        sheet_response = requests.get(url=environ['FLIGHTS_ENDPOINT'], headers=self.header)
        data = sheet_response.json()
        self.destinations = data['prices']
        return self.destinations
