import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# load_dotenv()


NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_API_ID = os.getenv("NUTRITIONIX_API_ID")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
today = datetime.now()
today_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")
sheety_header = {
        "Authorization": SHEETY_TOKEN
    }


nutritionix_header = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
nutritionix_request_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 71,
    "height_cm": 176.1,
    "age": 25,
}
nat_lang_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_response = requests.post(url=nat_lang_exercise_endpoint, headers=nutritionix_header,
                                     json=nutritionix_request_body)
print(nutritionix_response.raise_for_status())
nutritionix_data = nutritionix_response.json()


def new_entry():
    sheety_post_endpoint = "https://api.sheety.co/9b57982e1060f76bf25f96121e73d043/myWorkouts/workouts"
    for exercise in nutritionix_data["exercises"]:
        sheety_post_body = {
            "workout": {
                "date": today_string,
                "time": time_string,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        sheety_response = requests.post(url=sheety_post_endpoint, headers=sheety_header, json=sheety_post_body)
        print(sheety_response.text)


def edit_row(**kwargs):
    sheety_edit_endpoint = "https://api.sheety.co/9b57982e1060f76bf25f96121e73d043/myWorkouts/workouts/3"
    sheety_edit_config = {
        "workout": {
            "date": today_string,
            "time": time_string,
            "exercise": kwargs.get("exercise"),
            "duration": kwargs.get("duration"),
            "calories": kwargs.get("calories"),
            }
        }

    edit_response = requests.post(url=sheety_edit_endpoint, headers=sheety_header, json=sheety_edit_config)
    print(edit_response.text)


# edit_row(exercise=)
print(nutritionix_data)