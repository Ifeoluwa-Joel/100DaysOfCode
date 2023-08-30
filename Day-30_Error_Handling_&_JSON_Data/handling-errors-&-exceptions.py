# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"] This can be solved by the get() method which returns None instead of KeyError

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# Morphy's Law'
'''
Anything that can go wrong will go wrong.
--> So, we need to catch these exceptions
'''

# try... except syntax:
'''
try:
    block of code
except <Error>:
    do something in case block of code above raised <Error>
else: 
    if no error is raised. Run this code.
finally:
    run this code irrespective of what happens above.
'''

try:
    file = open("a_file.txt")
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
