import random

# Syntax for random integer
random_integer = random.randint(10, 100)
print(random_integer)

# Syntax for random float
random_float = random.random()
print(random_float)

# Generate random float between 0 to 5
print(round(random_float * 5, 4))

# Revisiting Love Calculator
love_score = random.randint(1, 100)

if (love_score < 20):
    print(f'Your love score is {love_score}.\nYou won\'t last a fortnight.')

elif (love_score < 61):
    print(f'Your love score is {love_score}.\nYou could make it work, but boy, do you have work to do?')

elif (love_score <90):
    print(f'Your love score is {love_score}.\nYour ship will sail. Enjoy your love!')
else:
    print(f'Your love score is {love_score}!.\nThis is the bone of your bones. You have hit a JACKPOT!!!')
