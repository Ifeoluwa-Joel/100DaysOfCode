# SEND MOTIVATIONAL QUOTES ON MONDAY TO EMAIL

import datetime as dt
import smtplib
from random import choice
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")
PORT = int(os.getenv("PORT"))


with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()

now = dt.datetime.now()
if now.weekday() == 0:  # Mon is 0, and so on...
    with smtplib.SMTP(host=SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TARGET_EMAIL,
                            msg=f"Subject: MONDAY MOTIVATION!\n\n"
                                f"{choice(quotes_list)}")
