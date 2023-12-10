import requests
import json

url = 'https://data.veridion.com/match/v4/companies'
headers = {
    'x-api-key': 'Lk34BnMBMFDj07xGbkQ_aNikeD4_NSKq643WxEEuQUAcjtbrVJStX9FpASw7',
    'Content-type': 'application/json',
}

data = {
    "legal_names": ["Aftermath Entertainment"],
    "commercial_names": [],
    "address_txt": "2220 Colorado Ave, Santa Monica, California, United States"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    # Load the response data into a Python object
    response_data = response.json()
    # Dump the Python object as a formatted string
    formatted_json = json.dumps(response_data, indent=4)
    print(formatted_json)
else:
    print("Error:", response.status_code)
    print(response.text)