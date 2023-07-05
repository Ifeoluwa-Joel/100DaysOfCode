import pandas

data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data['temp'].max())


# # Get Data in Columns
# day_list = data.day  # Treating the dataframe as an object with the column name as its attribute
# day__list = data['day']  # Treating the dataframe as a dictionary with the column name as its key
# print(day_list)
# print(day__list)


# Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.day == 'Saturday'])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == 14])  # Returns all rows when the temp is 14
# print(data[data.temp == 14].day)  # Returns all the days when the temp was 14

"""
So basically when we tap into a series, we get that column alone. 
e.g data.day. We get all the values under the 'day' column
but when we filter that expression by a condition, we get the corresponding row.
e.g data.day == 'Monday' or data.temp == data.temp.max()

Innit?

Let's continue with tutorial -->
"""

# monday = data[data.day == 'Monday']
# print(monday.condition)
tuesday = data[data.day == 'Tuesday']
print(tuesday.temp)
# print(tuesday.condition)

""" So we can now use the var monday to get hold of data under particular columns for that row alone.
Basically holding a particular 'cell'  instead of entire rows or columns. Fun! 
 """

# # CHALLENGE! Get hold of Monday's temp and convert it to Fahrenheit
# monday = data[data.day == 'Monday']
# monday_temp_celsius = int(monday.temp)
# monday_temp_fahrenheit = (monday_temp_celsius * (9 / 5)) + 32
# print(monday_temp_fahrenheit)
# # SUCCESS ✔❕

# FINAL THING!
"""
How to create a DataFrame from scratch
On line 3, we created that DataFrame by reading from a csv file.
We can also our DataFrame from scratch, from some  data we are generating in Python 
"""

data_dict = {
    "students": ['Amy', 'James', 'Angela'],
    "scores": [76, 56, 65],
    "sex": ['Female', 'Male', 'Female']
}

new_data = pandas.DataFrame(data_dict)  # Get hold of pandas, tap into pandas' Dataframe class and initialize the
                                        # class with your properly formatted python dictionary.
print(new_data)


"""
We can also save this our DataFrame into a csv.file
"""

# new_data.to_csv("C:/Users/Ifeoluwa Joel/Desktop/new_file.csv")
