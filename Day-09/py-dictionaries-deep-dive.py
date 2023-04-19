past_job_titles = {'Africa': 'West African Regional Manager', 'Nigeria': 'Senior Software Engineer'}


print(past_job_titles)

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
    "Nigeria": 1
}


# Retrieving items from a dictionary
'''
Items are retrieved from a data type using the key to it's value.
'''
print(programming_dictionary['Loop']) # Remember that the key must be called in the exact same datatype it was instantiated

# Adding new items to dictionary
programming_dictionary['Recursion'] = 'Having a function call itself over and over again until a condition is met'


# Creating an empty dictionary
empty_dictionary = {}

# Wiping an existing dictionary
# programming_dictionary = {}
print(programming_dictionary)
'''
This is useful for clearing out a user's progress
Wipe scores empty after games restart
etc.
'''

# Edit an item in a dictionary
programming_dictionary['Bug'] = 'A moth in your computer'
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # print(f'{key}:')
    print(key)
    print(programming_dictionary[key])