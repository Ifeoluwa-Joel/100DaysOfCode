"""
return keyword usually signfies the end of a function.
However using more than one 'return' statements may become necessary in some use cases.
See example below.
"""

def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't enter valid inputs!"  # Here, this return statement will prevent the function from going
                                                # formatting in cases where the user has not provided meaningful input.
    f_name_title_case = f_name.title()
    l_name_title_case = l_name.title()
    formatted_name = f_name_title_case + ' ' + l_name_title_case
    return formatted_name


print(format_name("Jack", ""))