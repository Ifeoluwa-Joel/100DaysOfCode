import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
sender_num = os.getenv("MY_TWILIO_PHONE_NO")
recipient_num = os.environ["MY_LOCAL_NO"]
app_id = os.getenv("OPEN_WEATHER_APPLICATION_ID")


parameters = {
    "lat": 6.621030,
    "lon": 3.374690,
    "exclude": "current,minutely,daily,alerts",
    "appid": app_id,
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today 🌧️🌧️.\nBring an umbrella ☂️☂️",
        from_=sender_num,
        to=recipient_num
    )

    print(message.status)  # to ensure that it was sent successfully
