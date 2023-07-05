import pandas

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
