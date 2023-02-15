print("PYTHON PIZZA")
size = input("What size of pizza do you want?\nSmall[S]; Medium[M]; Large[L]\n")
bill = 0

if size == 'S':
    bill += 15
    pepperoni = input("Do you want a pepperoni? Y/N ")
    if pepperoni == 'Y':
        bill += 2


elif size == "M":
    bill += 20
    pepperoni = input("Do you want a pepperoni? Y/N ")
    if pepperoni == 'Y':
        bill += 3

else:
    bill += 25
    pepperoni = input("Do you want a pepperoni? Y/N ")
    if pepperoni == 'Y':
        bill += 3

xtra_cheese = input("Do you want extra cheese? Y/N ")
if xtra_cheese == 'Y':
    bill += 1

# Output Operation
if pepperoni == 'N' and xtra_cheese == 'N':
    print(f'You selected a {size} pizza\nYour bill is ${bill}')

elif pepperoni == 'Y' and xtra_cheese == 'N':
    print(f'You selected a {size} pizza and added pepperoni\nYour bill is ${bill}')

elif pepperoni == 'N' and xtra_cheese == 'Y':
    print(f'You selected a {size} pizza with extra cheese\nYour bill is ${bill}')

else:
    print(f'You selected a {size} pizza with extra cheese and pepperoni toppings\nYour bill is ${bill}')
