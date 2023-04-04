# Python functions can be found in this url --> https://docs.python.org/3/library/functions.html

# Examples of functions
print("Hello")
num_char = len("Hello")
print(num_char)


# Structure of a Python function
# def function_identifier():
# funtion contents comes here indented

def add(a, b):
    sum = a + b
    return sum

# num1 = int(input("Enter the first number you want to add: "))
# num2 = int(input("Enter the second number you want to add: "))
# print(add(num1, num2))

def my_funtion(a, b):
    sum = add(a, b)
    print(f'The sum of {a} and {b} is: {sum}')
    print("Thanks for using this function.")

print(my_funtion(2, 5))

