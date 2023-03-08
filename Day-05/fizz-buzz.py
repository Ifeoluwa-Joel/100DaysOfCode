for number in range(1, 1001):
    if (number % 3 == 0 and number % 5 != 0):
        print("Fizz")
    elif (number % 5 == 0 and number % 3 != 0):
        print("Buzz")
    elif(number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    else:
        print(number)
