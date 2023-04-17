# ANGELA'S LOGIC
'''
We are going to loop through all the digits between 1 and the test number (excluding 1 and the test number)
Since all prime numbers are only divisible by 1 and themselves; if any digit between the test number and 1
returns 0 upon modulo operation (number % digit) that  means there's another number beside 1 and the test
 number itself that can divide the test number, hence it cannot be prime.
'''

def prime_checker(number):
    is_prime = True
    for digit in range(2, number):
        if number % digit == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
