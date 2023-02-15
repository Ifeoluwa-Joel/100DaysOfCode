print("Welcome to the Love Calculator!")

# Input Operation
your_name = input("What is your name?\n ")
their_name = input("What is their name?\n ")

# Logic
concatenated_names = your_name + their_name
lower_names = concatenated_names.lower()

# Count letters
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

# Find number of 't-r-u-e' occurences
true = t + r + u + e

# Find number of 'l-o-v-e' occurences
love = l + o + v + e

truelove = int(str(true) + str(love))

# Decide output
if truelove < 10 or truelove > 90:
    print(f"Your score is {truelove}, you go together like coke and mentos")

elif 40 < truelove < 50:
    print(f'Your score is {truelove}, you are alright together.')

else:
    print(f'Your score is {truelove}')
