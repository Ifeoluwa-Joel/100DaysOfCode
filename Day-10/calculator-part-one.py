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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    operation_symbol = input('Pick an operation from the line above: ')
    num2 = int(input("What is the second number?: "))

    '''My own logic
    I used the calc() function I have commented out below. It worked alright.
    But I find Angela's logic below the function much more readable. 
    God! When will I start thinking like Angela? 😭😭😭😭
    '''

    # def calc(n1, n2, sign):
    #     for symbol in operations:
    #         if sign == symbol:
    #             calculated_answer = operations[symbol](n1, n2)
    #             return f"{n1} {sign} {n2} = {calculated_answer}"
    #
    # print(calc(n1=num1, n2=num2, sign=operation_symbol))

    """
    Instead of the calc() function. 
    Angela used the logic below:
    """

    calc_complete = False
    while not calc_complete: #Main calculator loop
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {first_answer}')

        main_calc_loop = input(f"Do you want to continue calculating with {first_answer}? Type 'y' or 'n': ")
        if main_calc_loop == 'n':
            calc_complete = True
            break

        no_more_numbers = False
        while not no_more_numbers: # Secondary loop
            operation_symbol = input('Pick another operation: ')
            num3 = int(input('What is the next number? '))
            calculator_function = operations[operation_symbol]

            second_answer = calculator_function(first_answer, num3)
            print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')
            first_answer = second_answer

            check_for_more_numbers = input(f"Type 'y' to continue calculating with {second_answer}?  or 'n' to restart the calculator: ")

            if check_for_more_numbers == 'n':
                no_more_numbers = True
                calc_complete = True
                calculator() # Recursion is used to recall the calculator() function back


calculator()