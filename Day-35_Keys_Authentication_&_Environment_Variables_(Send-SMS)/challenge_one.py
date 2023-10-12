import requests

parameters = {
    "lat": 6.621030,
    "lon": 3.374690,
    "appid": "db39e38e31bb0d2b94dc06d25f5c12b0",
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

data = response.json()

print(data["hourly"])
print(len(data["hourly"]))
