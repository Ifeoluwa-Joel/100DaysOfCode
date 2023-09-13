import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP = os.getenv("SMTP")
PORT = int(os.getenv("PORT"))

with smtplib.SMTP(host=SMTP, port=PORT) as connection:
    connection.starttls()  # TLS - Transport Layer Security. For encryption in transit
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=TARGET_EMAIL,
                        msg="Subject: Hello from Python\n\nThis is the body of the email. I am using .env now")


# How to make emails not be flagged as spam. Add subject
