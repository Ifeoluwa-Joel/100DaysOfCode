##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
import pandas
import random
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")
PORT = int(os.getenv("PORT"))
PLACEHOLDER = "[NAME]"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month

data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
# print(birthday_data)

for person in birthday_data:
    if person["day"] == current_day and person["month"] == current_month:
        template_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{template_number}.txt") as letter:
            letter_contents = letter.read()
            new_letter = letter_contents.replace(PLACEHOLDER, person["name"])

        with smtplib.SMTP(host=SMTP, port=PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday {person['name']}!\n\n"
                                    f"{new_letter}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.