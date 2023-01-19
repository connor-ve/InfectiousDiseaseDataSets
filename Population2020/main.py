import requests
import json

response = requests.get("https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest")
data = response.json()
data = data["data"]

States2020 = []
# Print the data
for _ in range(len(data)):
  States2020.append([data[_]['State'], data[_]['Population']])

headers = ['State', 'Population']

# make a csv file using headers and States2020
with open('States2020.csv', 'w') as f:
  f.write(f"{headers[0]}, {headers[1]},\n")
  for _ in range(len(States2020)):
    f.write(f'{States2020[_][0]}, {States2020[_][1]},\n')