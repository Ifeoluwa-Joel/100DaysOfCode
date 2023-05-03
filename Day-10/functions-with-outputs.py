# Functions with outputs

def format_name(f_name, l_name):
    f_name_title_case = f_name.title()
    l_name_title_case = l_name.title()
    formatted_name = f_name_title_case + ' ' + l_name_title_case
    return formatted_name

first_name = input('Enter your funky first name: ')
last_name = input('Enter your funky last name: ')

print(f'Your formatted name is: {format_name(l_name=last_name, f_name=first_name)}')

