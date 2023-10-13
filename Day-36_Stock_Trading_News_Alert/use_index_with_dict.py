from datetime import datetime

params = {
    "function": "TIME_SERIES_DAILY",
    "outputsize": "compact",
    "symbol": "GOGL",
    "apikey": 2020202020
}


key_at_index = list(params.keys())[3]
value_at_index = list(params.values())[2]
print(key_at_index)
print(value_at_index)


print(datetime.today())