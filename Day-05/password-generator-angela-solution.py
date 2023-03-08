#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

# Eazy Level
# password = ""
# # nr_letters = 4
#
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters) # I used random.choices but Angela is using random.choice
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)


# Hard Level
# ... in easy level above, we were saving the components of the password into a sting called 'password'
# but in this one, we will be saving them into a list where we can easily randomize them...

password_list = [] # Empty List
# nr_letters = 4

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters) # I used random.choices but Angela is using random.choice
#   password_list.append(random.choice(letters)) This line does the same thing as the line above

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)

# Try shuffling list
random.shuffle(password_list)
print(password_list)

random_password = ""
for random in password_list:
    random_password += random
print(random_password)