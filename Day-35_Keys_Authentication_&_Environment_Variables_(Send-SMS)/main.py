import requests
import os
from dotenv import load_dotenv

load_dotenv()


def alert_on_telegram(msg: str):
    response_ = requests.get(
        f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={msg}")
    response_.raise_for_status()

    return response_.json()


app_id = os.getenv("OPEN_WEATHER_APPLICATION_ID")
bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
bot_chat_id = os.environ["TELEGRAM_BOT_CHAT_ID"]

parameters = {
    "lat": 6.621030,
    "lon": 3.374690,
    "exclude": "current,minutely,daily,alerts",
    "appid": app_id,
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

next_12_hour_data = weather_data["hourly"][0:12]  # Dict slicing to get the 0th to 11th (key:value) pairs

will_rain = False
for hour in next_12_hour_data:
    weather_id = hour["weather"][0]["id"]  # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    if weather_id < 700:
        will_rain = True
if will_rain:  # If at least one of the next 12 hours' ID is more than 700. It would have triggered preceeding line
    alert_on_telegram(msg=f"It will rain today 🌧️🌧️.\nBring an umbrella ☂️☂️")
else:
    alert_on_telegram(msg=f"Clear skies today! 🌞🌞.\nEnjoy⛱️🍹\nGod bless you! ️")
