import requests
import datetime as dt

"""
The same way that we can pass in different args/params to the same function to get different results,
we can pass in different params to an api to get different results.
"""

# Sunrise and Sunset Times API
# Endpoint --> https://api.sunrise-sunset.org/json.
MY_LAT = 6.621030
MY_LONG = 3.374690

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,  # this line formatted the data returned into 24-hour format, which we will need to be able to
                     # compare with the current time we will get from the datetime module
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]
"""
To future self: the complicated line above is easy enough if you calm down.
Read line from left to right, thinking like the interpreter as you go.
Tip, run print(sunrise) to see why these splits and indexing were necessary

Oh, you can simply check notes on Udemy:
Note 33 - "Neat way to extract the time from complicated string returned by the API." at 12:18 Minute of Lesson 300
"""

print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)

