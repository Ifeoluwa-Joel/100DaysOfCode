# FUNCTIONS WITH MULTIPLE PARAMETERS

def greet_with(name, location):
    print(f'Hi there {name}')
    print(f'What is it like in {location}?')

name = input('What is your name? ')
location = input("Location: ")

greet_with(name, location)

# Keep in mind, positional argument in Python makes the Interpreter reads and assign function
# variables according to their position in function definition and function calling

# KEYWORD ARGUMENT
# Keyword_argument on the other hand does not care, because data is explicitly assigned to specific
# parameers during function calls
greet_with(location='Abule Oja', name='Dr. Adigun')
