import requests
import json
from main import model_response_final
from search_volume import company_score
# from get_artists import get_artists

API_KEY=#

def query_data():
	prediction = model_response_final(record=True)
	print(f"{prediction[0]}")
	print(f"{prediction[1][0]}")

	url = "https://data.veridion.com/search/v1/companies"
	api_key = API_KEY

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
		formatted_json = json.dumps(response_data, indent=2)
		companies = response_data["result"]
		arr = []

		# Formatting the array
		formatted_data = [{"Company Name": f"{company['company_name']}"} for company in companies]


		f = open("jsonCompanies.json", "w")
		# Saving the formatted data to a JSON file
		try:
			ord_data = sorted(formatted_data, key=lambda x: company_score(x["Company Name"].split("Record LABEL ")[-1]), reverse=True)
			print("ord: ", ord_data[0], ord_data[1], ord_data[2])
			f.write(str(json.dumps(ord_data[:3], indent=2)))
		except:
			plc_data = formatted_data["Company Name"].split("Record LABEL ")[-1]
			print("plc:", plc_data[0], plc_data[1], plc_data[2])
			f.write(str(json.dumps(plc_data[:3], indent=2)))	

		f = open("jsonCompaniesExtended.json", "w")
		f.write(str(json.dumps(response_data, indent=2)))

		# get_artists(prediction[1][0], ord_data[:3]) # Replace with new get_artists function @Tudor
	else:
		pass
		# print("Error:", response.status_code)
		# print(response.text)

if __name__ == '__main__':
	query_data()
