# METHOD 1 (Didn't work)
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()


# METHOD 2 (worked,  but too much faff according to Angie) So here comes Pandas
# import csv
# with open('weather_data.csv') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# METHOD 3 - PANDAS
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# temp_list = []
# for temp in data["temp"]:
#     temp_list.append(temp)
# print(temp_list)
#
# day_list = []
# for day in data["day"]:
#     day_list.append(day)
# print(day_list)

# LMAO, easily achieved with:
# data.day
# or
# data['day']


# MORE ON PANDAS - check the file 'intro-to-pandas.py'
