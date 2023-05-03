from art import logo

'''
Mostly using Angela's logic at this point.
But I have made sure I understood how they work vividly well.

Let's perfect this thing.💪💪💪

'''

def add(n1, n2):
    """adds two numbers and returns the sum"""
    return n1 + n2


def subtract(n1, n2):
    """subtracts two numbers and returns the difference"""
    return n1 - n2


def multiply(n1, n2):
    """multiplies two numbers and returns the product"""
    return n1 * n2


def divide(n1, n2):
    """divides two numbers and returns the quotient"""
    return n1 / n2


def exponent(n1, n2):
    """takes two number and return the exponentiation;
    using the 1st parameter as the base num and the 2nd parameter as the exponent"""
    return n1 ** n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": exponent}


def calculator():
    """Add, multiply, divide or subtract two numbers and continues doing so till user say otherwise"""
    print(logo)
    num1 = float(input("What is the first number?: "))
    should_continue = True

    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol = input('Pick an operation from the line above: ')
        num2 = float(input("What is the next number?: "))

        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"Type 'y' to continue with {answer}: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()  # Using recursion to make Calculator() call itself

calculator()