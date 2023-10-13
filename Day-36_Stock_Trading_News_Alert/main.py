import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from twilio.rest import Client
from random import choice

load_dotenv()


def perc_change(num_1, num_2) -> float:
    """
    :param num_1: yesterday's closing stock price
    :param num_2: day before yesterday's closing stock price
    :return: the percentage change between the stock prices
    """
    result = abs(((num_2 - num_1) / num_2) * 100)
    return round(result, 2)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
SENDER_NUM = os.getenv("MY_TWILIO_PHONE_NO")
RECIPIENT_NUM = os.environ["MY_LOCAL_NO"]
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "outputsize": "compact",
    "symbol": STOCK,
    "apikey": api_key
}

news_api_key = os.getenv("NEWS_API_KEY")
yesterday = datetime.strftime(datetime.today() - timedelta(days=1), "%Y-%m-%d")
news_parameters = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
    "from": yesterday,
    "language": "en"
}

response = requests.get("https://www.alphavantage.co/query", params=alphavantage_parameters)
response.raise_for_status()
tesla_stock_data = response.json()

# To understand this section, view the contents of <tesla_stock_data> in a json viewer. It's an elaborate tree
yesterday_key = list(tesla_stock_data["Time Series (Daily)"].keys())[0]
yesterday_stock_price = float(tesla_stock_data["Time Series (Daily)"][yesterday_key]["4. close"])
day_before_yesterday_key = list(tesla_stock_data["Time Series (Daily)"].keys())[1]
day_before_yesterday_stock_price = float(tesla_stock_data["Time Series (Daily)"][day_before_yesterday_key]["4. close"])

# Choose icon to show in message
if yesterday_stock_price > day_before_yesterday_stock_price:
    icon = "🔺"
    direction = "rises"
else:
    icon = "🔻"
    direction = "falls"

percentage_change = perc_change(yesterday_stock_price, day_before_yesterday_stock_price)
if percentage_change >= 5:
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    first_10_news = news_data["articles"][:9]
    current_news = choice(first_10_news)  # Choose one news to send to subscriber

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=f"{STOCK}:{icon} {percentage_change}%\n"
             f"Headline: {current_news['title']}\n"
             f"{current_news['description']}\n"
             f"Read more...{current_news['url']}",
        from_=SENDER_NUM,
        to=RECIPIENT_NUM
    )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=f"{STOCK} {icon} {percentage_change}%\n"
             f"{COMPANY_NAME}'s stock {direction} by {percentage_change}%",
        from_=SENDER_NUM,
        to=RECIPIENT_NUM
    )
