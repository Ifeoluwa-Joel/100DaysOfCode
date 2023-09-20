import requests

# Using Open Notify API - Endpoint:
response = requests.get(url="http://api.open-notify.org/astros.json")
response.raise_for_status()

data = response.json()
print(data)

iss_stat = [dic for dic in data["people"] if dic["craft"] == "ISS"]
num_aboard_iss = len(iss_stat)
astros_aboard_iss = [name["name"] for name in iss_stat]
print(num_aboard_iss)
print(astros_aboard_iss)

tiangong_stat = [dic for dic in data["people"] if dic["craft"] == 'Tiangong']
num_aboard_tiangong = len(tiangong_stat)
astros_aboard_tiangong = [name["name"] for name in tiangong_stat]
print(num_aboard_tiangong)
print(astros_aboard_tiangong)
