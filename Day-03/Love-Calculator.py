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

#OLD OUTPUT
# if truelove < 10 or truelove > 90:
#     print(f"Your score is {truelove}, you go together like coke and mentos")
#
# elif 40 < truelove < 50:
#     print(f'Your score is {truelove}, you are alright together.')
#
# else:
#     print(f'Your score is {truelove}')

# New Output
if (truelove < 11):
    print(f'Your score is {truelove}.\n Ajatuka ni t\'agbaaran')

elif (truelove < 21):
    print(f'Your score is {truelove}.\n Find your  love go front')

elif (truelove < 31):
    print(f'Your score is {truelove}.\n Una go kill each other las las')

elif (truelove < 41):
    print(f'Your score is {truelove}.\n Walahi, e le bara yin kale')

elif (truelove < 51):
    print(f'Your score is {truelove}.\n Fair. You can do better')

elif (truelove < 61):
    print(f'Your score is {truelove}.\n Average. You are alright together')

elif (truelove < 71):
    print(f'Your score is {truelove}.\n High score. You go together like groundnut and garri')

elif (truelove < 81):
    print(f'Your score is {truelove}.\n Wow! Bread and Butter Love. I want o')

elif (truelove < 91):
    print(f'Your score is {truelove}.\n Amazing! Forever is the deal!')

else:
    print(f" Your score is {truelove}. OUT OF RANGE!!. KI LO DE? ADAM AND EVE")