import requests
from datetime import datetime

USERNAME = 'pomogub'
TOKEN = 'dfuh389er239rjg3nrg93jnfg'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Reading Graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'momiji',
}

headers = {'X-USER-TOKEN': TOKEN}
today = datetime.now()
pixel_create_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input("How many pages did you read today? "),
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# response = requests.post(url=pixel_create_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_date = '20260902'
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date}'
update_data = {
    'quantity': '6',
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
