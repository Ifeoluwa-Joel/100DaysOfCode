import pandas
"""
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

squirrel_count_dict = {
    "Fur Color": ['grey', 'red', 'black'],
    "Count": [grey["Primary Fur Color"].count(), cinnamon["Primary Fur Color"].count(),
              black["Primary Fur Color"].count()]
}

squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count.csv")
"""

# Angela's logic for the same task above.

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("C:/Users/Ifeoluwa Joel/Desktop/squirrel_count.csv")

