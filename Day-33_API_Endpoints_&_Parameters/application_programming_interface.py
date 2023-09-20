"""
YouTube videos I watched before starting ANGELA's Explanation
1. https://www.youtube.com/watch?v=OVvTv9Hy91Q
    WHAT APIs ARE USED FOR?
    i. Access Data
    ii. Hide Complexity
    iii. Extend Functionality
    iv. Security

https://www.youtube.com/watch?v=ByGJQzlzxQg
"""

"""
ANGELA's EXPLANATION
An Application Programming Interface (API) is a set of commands, functions, 
protocols and objects that programmers can use to create software or interact
with an external system.
"""

# API EndPoints and Making API Calls
"""
Endpoints are the locations of the api itself, where you go when you need data 
from an api. For example, if you want to get money from a bank you need to know
where the bank is. 
Endpoints are usually URLS --> e.g. api.coinbase.com
"""

# International Space Shuttle Current Location API
# Endpoint - http://api.open-notify.org/iss-now.json
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raise HTTP Status Errors/Exceptions

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)

print(data)
print(latitude)
print(longitude)
print(iss_position)
