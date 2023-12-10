import requests
import json
from main import model_response_final

def query_data():
	prediction = model_response_final(record=False)
	print(f"{prediction[0]}")
	print(f"{prediction[1][0]}")

	url = "https://data.veridion.com/search/v1/companies"
	api_key = "API_KEY"

	headers = {
		"Content-Type": "application/json",
		"x-api-key": api_key
	}

	data = {
		"filters": [
			{
				"attribute": "company_keywords",
				"relation": "match_expression",
				"value": {
				"match": {
					"operator": "and",
					"operands": [
						"Record Labels",
						prediction[1][0],
						]
					},
				}
			}
		]
	}

	response = requests.post(url, headers=headers, json=data)

	if response.status_code == 200:
		response_data = response.json()
		formatted_json = json.dumps(response_data, indent=4)
		companies = response_data["result"]
		arr = []

		# Formatting the array
		formatted_data = [{"Company Name": f"{company['company_name']}"} for company in companies]

		# Saving the formatted data to a JSON file
		f = open("jsonCompanies.json", "w")
		f.write(str(json.dumps(formatted_data, indent=4)))
	else:
		print("Error:", response.status_code)
		print(response.text)

if __name__ == '__main__':
	query_data()