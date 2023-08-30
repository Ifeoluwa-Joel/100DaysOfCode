sample_json_format = {
    "Amazon": {
        "email": "angela@email.com",
        "password": "5fBraA$uSA5"
    },
    "Twitter": {
        "email": "angela@email.com",
        "password": "!gVfPVihW&4pM"
    },
    "eBay": {
        "email": "angela@email.com",
        "password": "JjV+bylY6m04"
    }
}

"""
WRITE           READ             UPDATE
json.dump()     json.load()     json.update()
"""

"""
json.dump() serializes to json
json.load() deserializes to Python dict
"""


json.dump(new_data, data_file, indent=4)  # DUMP DATA in json
json_loaded_data = json.load(data_file)  # LOAD DATA in json
print(json_loaded_data)

# HOW TO UPDATE - 3 steps
data = json.load(data_file)  # read old data
data.update(new_data)  # update with new data
with open("data.json", "w") as data_file:
    json.dump(data, data_file, indent=4)  # saving updated data
