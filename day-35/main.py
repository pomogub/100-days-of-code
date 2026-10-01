from requests import get
from twilio.rest import Client


sid = ''
auth_token = ''
client_secret = 'SwjYZVqYZHNEKjuYPAuumbjYCOQcZ9HP'

OWM_Endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
api_key = '3a31d2f114fe396b26f0d9f2bbc37fa5'

weather_params = {
    'lat': 37.8403,
    'lon': -85.9491,
    'cnt': 4,
    'appid': api_key
}

response = get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_codes = []
will_rain = False

for forecast in weather_data['list']:
    weather_codes.append(forecast['weather'][0]['id'])
for code in weather_codes:
    if code < 700:
        will_rain = True
if will_rain:
    client = Client(sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today, brin an ☂️",
    #     from_='+17372324091',
    #     to='+12709963838'
    # )
