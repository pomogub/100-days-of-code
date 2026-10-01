import requests
from os import environ
from datetime import datetime

# API_KEY =  'nix_live_1AAT2N9XCMtuMuq5H0UQjX3754uS8L9p'
# APP_ID = 'app_e7f7b6da47f04088993ebc3f'
# TOKEN = '389vn3byd62kdlg89u4njuie'
GENDER = 'male'
AGE = 39
WEIGHT_KG = 147
HEIGHT_CM = 165

exercise_endpoint = 'https://app.100daysofpython.dev/v1/nutrition/natural/exercise'
exercise_text = input("What exercise did you do? ")
exercise_headers = {
    'x-app-key': environ['API_KEY'],
    'x-app-id': environ['APP_ID'],
}
exercise_data = {
    'query': exercise_text,
    'gender': GENDER,
    'age': AGE,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
}

datetime_now = datetime.now()
current_date = datetime_now.strftime('%m/%d/%Y')
current_time = datetime_now.strftime('%X')
# sheety_endpoint = 'https://api.sheety.co/6c6bd9dc78cea37eecbaaba786270c21/workoutTracking/workouts'
sheety_header = {'Authorization': environ['TOKEN']}
sheet_input = ''

response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_data)
result = response.json()
# print(result)

for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            'date': current_date,
            'time': current_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

sheet_response = requests.post(url=environ['WORKOUT_ENDPOINT'], headers=sheety_header, json=sheet_input)
# print(sheet_response.text)
