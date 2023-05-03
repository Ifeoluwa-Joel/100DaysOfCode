def format_name(f_name, l_name):
    """Takes a first and last name,
    and formats it to return the Title case of the names"""
    if f_name == '' or l_name == '':
        return "You didn't enter valid inputs!"
    f_name_title_case = f_name.title()
    l_name_title_case = l_name.title()
    formatted_name = f_name_title_case + ' ' + l_name_title_case
    return formatted_name


first_name = input('Enter your funky first name: ')
last_name = input('Enter your funky last name: ')
full_name = format_name(first_name, last_name)
length = len(full_name)
print(length)
print(full_name)
