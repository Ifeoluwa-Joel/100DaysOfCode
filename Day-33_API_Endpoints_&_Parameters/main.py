import requests
from datetime import datetime, timezone
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")
PORT = int(os.getenv("PORT"))
MY_LAT = 6.621030
MY_LONG = 3.374690


def is_iss_near():
    """
    :return: True if iss is +/- 5 of my latitude or longitude
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # this line formatted the data returned into 24-hour format, which we will need to be able to
        # compare with the current time we will get from the datetime module
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)

    if time_now.hour >= sunset:
        return True


# If the ISS is close to my current position and it is currently dark, send me an email to tell me to look up.
def main():
    if is_iss_near() and is_night():
        with smtplib.SMTP(host=SMTP, port=PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TARGET_EMAIL,
                                msg=f"Subject: ISS is Overhead!\n\n"
                                    f"The International Space Station is currently overhead at your location({MY_LAT}, "
                                    f"{MY_LONG}).\nLook up!")


# BONUS CHALLENGE: run the code every 60 seconds.
start_time = time.time()  # time() func returns the time in seconds since the 'epoch' as a floating point number
print(start_time)

while True:
    main()
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))  # Remove the Time taken by code to execute
