import requests
from datetime import datetime
from smtplib import SMTP
from time import sleep

MY_LAT = 37.84605 # Your latitude
MY_LONG = -85.951133 # Your longitude
MY_EMAIL = 'alda.fay@ethereal.email'
PASSWORD = 'f1dJ5TPZdrtb3ZcWhD' # noqa


def overhead():

    # Your position is within +5 or -5 degrees of the ISS position.
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def nighttime():

    # Is currently dark
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True

while True:
    sleep(60)
    if nighttime() and overhead():
        with SMTP('smtp.ethereal.email', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='loscakes@gmail.com',
                                msg="Subject:ISS\n\nLook up, the ISS is above!"
                                )

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
