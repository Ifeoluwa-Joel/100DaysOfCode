import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

app_id = os.getenv("OPEN_WEATHER_APPLICATION_ID")
SENDER = os.getenv("MY_EMAIL")
RECEIVER = os.getenv("TARGET_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.environ["SMTP"]
PORT = int(os.environ["PORT"])


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
    with smtplib.SMTP(host=SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(user="trainingemail494@gmail.com", password=PASSWORD)
        connection.sendmail(from_addr="trainingemail494@gmail.com",
                            to_addrs="trainingemail494@gmail.com",
                            msg=f"Subject:Rain Alert!\n\n"
                                f"It will rain today 🌧️🌧️ .\nBring an umbrella ☂️☂️".encode("utf8")
                            )
        """ msg.encode("utf8") is necessary because of the emojis. The default ASCII can't handle them """
