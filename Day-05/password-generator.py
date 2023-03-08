#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

#Eazy Level - Order not randomised:
print("EASY LEVEL")
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Randomly select the characters
alphabets = random.choices(letters, k = nr_letters)
signs = random.choices(symbols, k = nr_symbols)
digits = random.choices(numbers, k = nr_numbers)


# Convert selected characters to strings
password_alphabets = ""
for alphabet in alphabets:
    password_alphabets = password_alphabets + alphabet

password_signs = ""
for sign in signs:
    password_signs = password_signs + sign

password_digits = ""
for digit in digits:
    password_digits = password_digits + digit


# CREATE PASSWORD
# Concatenate the alphabet, sign and digit strings together
generated_password = password_alphabets + password_signs + password_digits
print(generated_password + "\n")


# ###################################################
# Hard Level - Order of characters randomised:
print("HARD LEVEL!")
# Convert generated password to list and save into variable break_generated_password
break_generated_password = list(generated_password)

# Shuffle broken password
random.shuffle(break_generated_password)

# Convert randomized password which is currently a list back to string
randomized_password =""
for random in break_generated_password:
    randomized_password = randomized_password + random
print(f'Your generated password is:\n{randomized_password}')

#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P