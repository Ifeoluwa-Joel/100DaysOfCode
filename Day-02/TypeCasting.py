# Receive name from user
num_char = len(input("What is your name?\n"))

# Typecast it from integer so that we can be able to concatenate it
new_num_char = str(num_char)

# Print
print("Your name has " + new_num_char + " characters")


# Check types of both integers
print(type(num_char))
print(type(new_num_char))

