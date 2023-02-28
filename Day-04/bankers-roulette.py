import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_persons = len(names)
random_person = random.randint(0, number_of_persons)
payer = names[random_person]

# You can also use the 'choice' method under random module;
# but it is not required for this lesson, for future reference however;
# the next line demonstrates how to use it (It will also be commented so as not to interfere with the Intepreter)
# payer = random.choice(names)

# Output Operation
print(f'{payer} is going to buy the meal today!')




