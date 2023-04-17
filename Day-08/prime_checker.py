# CONCEPTS USED TO SOLVE PROBLEM
'''
- Positional and Keyword Argument
- For loops
-
'''

# Using Trial Division Algorithm
def prime_checker(number):
    score = 0
    for digit in range(1, number + 1):
        if number % digit == 0:
            score += 1
    if score == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)