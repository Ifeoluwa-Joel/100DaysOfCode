'''
She did exactly what I did, so I will not retype her solution.
I will just have a play around with my own code below here
'''

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_dict = {}
    new_dict['country'] = country_visited
    new_dict['visits'] = times_visited
    new_dict['cities'] = cities_visited
    travel_log.append(new_dict)

user_done = False
while not user_done:
    country = input('Enter the name of the country you wanna add:\n')
    times = input('How many times have you been there?:\n')
    cities = input('Enter the cities you visited there (Separate cities '
                   'with commas followed by a space)\n').split(" ")

    add_new_country(country_visited=country, times_visited=times, cities_visited=cities)

    more_countries = input("Do you want to enter more countries?\n")

    if more_countries == 'no':
        user_done = True

print(travel_log)
