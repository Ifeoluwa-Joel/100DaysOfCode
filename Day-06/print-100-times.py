import random

test_number = 0
while test_number != 9 and test_number != 5:
    test_number = random.randint(0, 1000)
    # print(test_number)


# Print all even numbers
# # upper_cap = int(input("Enter the upper cap:\n"))
# for test in range(0, upper_cap + 1):
#     if test % 2 == 0:
# #       print(test)




books_in_shelf = ["Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart", "Things Fall Apart"]
# books_in_shelf = []

# print(len(books_in_shelf))

books_in_shelf.append("No Longer At Ease")
books_in_shelf.append("Things Fall Apart")
books_in_shelf.append("Elfland")
books_in_shelf.append("Kiss Quotient")
books_in_shelf.append("Love Me Sweet")
books_in_shelf.append("Magnus Chase")
books_in_shelf.append("Harry Potter")
books_in_shelf.append("A Concise Introduction to Pure Mathematics")
books_in_shelf.append("The gods are to blame")
books_in_shelf.append("Efunsetan Aniwura")


count = 0
for book in books_in_shelf:
    count += 1


# Python Dictionaries
chelsea = {'Color': 'Blue', 'Home': 'Stamford Bridge', 'Gaffer': 'Graham Potter', 'Owner': 'Todd Boehly & Co.', 'Trophy': 'UEFA Champions League'}

chelsea['Color'] = 'Blue and White'
