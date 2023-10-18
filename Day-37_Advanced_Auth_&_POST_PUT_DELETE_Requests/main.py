import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.environ["PIXELA_API_TOKEN"]
USERNAME = "wreckitralph"
GRAPH_ID = "graph1"

pixela_new_user_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "wreckitralph",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_new_user_endpoint, json=user_params)
# print(response.text)

""" Create a new graph """
pixela_graph_endpoint = "https://pixe.la/v1/users/wreckitralph/graphs"

graph_config = {
    "id": "graph1",
    "name": "Pages Read",
    "unit": "page",
    "type": "int",
    "timezone": "Africa/Lagos",
    "color": "ajisai",
}

header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=pixela_graph_endpoint, headers=header, json=graph_config)
# print(response.text)


""" ADD A PIXEL TO THE GRAPH """
post_pixel_endpoint = "https://pixe.la/v1/users/wreckitralph/graphs/graph1"
today = datetime.now()
today_date = today.strftime("%Y%m%d")


pixel_config = {
    "date": today_date,
    "quantity": "5",
}

# response = requests.post(post_pixel_endpoint, json=pixel_config, headers=header)
# print(response.text)


""" UPDATE PIXEL EXISTING IN THE GRAPH """
update_pixel_endpoint = "https://pixe.la/v1/users/wreckitralph/graphs/graph1/20231016"

update_params = {
    "quantity": "4",
}

response = requests.put(update_pixel_endpoint, headers=header, json=update_params)
print(response.text)
print(response.json())
