# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
import random

name_list = ['Ifeoluwa', 'Angela', 'Jason', 'Edmund', 'Caspian', 'Erie', 'Marjorie']
name = random.choice(name_list)

def greet(name): #greet is a function with  input
    print(f'Hi there, {name}')
    print('Chelsea beats Real Madrid today, yeah?')
    print('If so, I will be one happy man')

# name = input("What is your name? ")
greet(name)
