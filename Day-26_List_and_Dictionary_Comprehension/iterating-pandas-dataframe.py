import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through Dictionaries
# for (key, value) in student_dict.items():
    # print(key)
    # print(value)

"""
Looping through DataFrames is the same like looping through Python Dictionaries
"""

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a DataFrame #
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)
"""
Well this is not very useful, is it? It is looping through columns
That is why we use iterrows() from pandas
"""

# Loop through rows of a Dataframe
student_name = input("Enter Student name: ")
for (index, row) in student_data_frame.iterrows():
    if row.student == student_name:
        print(row.score)
