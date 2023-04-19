capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

# Nesting a List in a Dictionary
'''
Suppose instead of just the capitals we want to have a list of
all the cities I've traveled to in one country.
'''
travel_log_simple = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Munich', 'Meissen'],
}


# Nesting a Dictionary in a Dictionary
'''
Suppose instead of just keeping track of how many places I have visited  in a country;
What if  I want to keep track of how many times I have visited that country
'''
travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin', 'Munich', 'Meissen'], 'local_foods_tried': 7},
}

# Dictionaries nested in Lists

travel_log_europe = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Munich', 'Meissen'],
        'local_foods_tried': 7
     },
]

travel_log_north_america = [
    {
        'country': 'United_States',
        'cities_visited': ['South Carolina', 'Texas', 'Los Angeles', 'California', 'Chicago', 'Florida'],
        'total_visits': 107
    },
    {
        'country': 'Canada',
        'cities_visited': ['Ottawa', 'Saskatoon', 'Toronto', 'Vancouver'],
        'local_foods_tried': 13
    },
]

for journey in travel_log_europe:
    print(journey)

for journey in travel_log_north_america:
    print(journey)

print(travel_log_europe[0]['cities_visited'])
