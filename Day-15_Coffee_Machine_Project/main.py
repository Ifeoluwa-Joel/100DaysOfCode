MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Define Constants
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25
ESPRESSO_COST = MENU['espresso']['cost']
LATTE_COST = MENU['latte']['cost']
CAPPUCCINO_COST = MENU['cappuccino']['cost']
ESPRESSO_WATER = MENU['espresso']['ingredients']['water']
ESPRESSO_COFFEE = MENU['espresso']['ingredients']['coffee']
LATTE_WATER = MENU['latte']['ingredients']['water']
LATTE_COFFEE = MENU['latte']['ingredients']['coffee']
LATTE_MILK = MENU['latte']['ingredients']['milk']
CAPPUCCINO_WATER = MENU['cappuccino']['ingredients']['water']
CAPPUCCINO_COFFEE = MENU['cappuccino']['ingredients']['coffee']
CAPPUCCINO_MILK = MENU['cappuccino']['ingredients']['milk']

water_left = resources['water']
milk_left = resources['milk']
coffee_left = resources['coffee']
money = 0


def report():
    """prints a report of the amount of resources and  money
            in the machine at the moment it is called"""
    print(f"Water: {water_left}ml")
    print(f"Milk: {milk_left}ml")
    print(f"Coffee: {coffee_left}g")
    # print(f"Money: ${money}")


def make_espresso():
    """takes the recipe for an espresso and makes an espresso.
            depletes the storage of water and coffee everytime it is called"""
    global water_left, coffee_left
    espresso_drink = ESPRESSO_COFFEE + ESPRESSO_WATER
    water_left -= ESPRESSO_WATER
    coffee_left -= ESPRESSO_COFFEE
    print(f"Here is your nice cup of espresso ☕. {espresso_drink}ml. Enjoy.")


def make_latte():
    """takes the recipe for a latte and makes a latte.
            depletes the storage of water and coffee everytime it is called"""
    global water_left, coffee_left, milk_left
    latte_drink = LATTE_COFFEE + LATTE_WATER + LATTE_MILK
    water_left -= LATTE_WATER
    coffee_left -= LATTE_COFFEE
    milk_left -= LATTE_MILK
    print(f"Here is your nice cup of latte ☕. {latte_drink}ml. Enjoy.")


def make_cappuccino():
    """takes the recipe for a cappuccino and makes a cappuccino.
            depletes the storage of water and coffee everytime it is called"""
    global water_left, coffee_left, milk_left
    cappuccino_drink = CAPPUCCINO_COFFEE + CAPPUCCINO_WATER + CAPPUCCINO_MILK
    water_left -= CAPPUCCINO_WATER
    coffee_left -= CAPPUCCINO_COFFEE
    milk_left -= CAPPUCCINO_MILK
    print(f"Here is your nice cup of cappuccino ☕. {cappuccino_drink}ml. Enjoy.")


def check_resource(drink):
    global water_left, milk_left, coffee_left
    if drink == 'espresso':
        if water_left < ESPRESSO_WATER:
            print("Sorry there is not enough water.")
        if coffee_left < ESPRESSO_COFFEE:
            print("Sorry there is not enough coffee.")
        if water_left >= ESPRESSO_WATER and coffee_left >= ESPRESSO_COFFEE:
            make_espresso()
    elif drink == 'latte':
        if water_left < LATTE_WATER:
            print("Sorry there is not enough water.")
        if coffee_left < LATTE_COFFEE:
            print("Sorry there is not enough coffee.")
        if milk_left < LATTE_MILK:
            print("Sorry there is not enough milk.")
        if water_left >= LATTE_WATER and milk_left >= LATTE_MILK and coffee_left >= LATTE_COFFEE:
            make_latte()
    elif drink == 'cappuccino':
        if water_left < CAPPUCCINO_WATER:
            print("Sorry there is not enough water.")
        if coffee_left < CAPPUCCINO_COFFEE:
            print("Sorry there is not enough coffee.")
        if milk_left < CAPPUCCINO_MILK:
            print("Sorry there is not enough milk.")
        if water_left >= CAPPUCCINO_WATER and coffee_left >= CAPPUCCINO_COFFEE and milk_left >= CAPPUCCINO_MILK:
            make_cappuccino()
    else:
        print("Sorry. I do not recognise that drink. Wanna try again?")


def process_coins(drink):
    global money
    input("Please insert coins.")
    quarters = int(input("How many quarters? ")) * QUARTER
    dimes = int(input("How many dimes? ")) * DIME
    nickels = int(input("How many nickels? ")) * NICKEL
    pennies = int(input("How many pennies? ")) * PENNY
    money = quarters + dimes + nickels + pennies
    # calculate_balance
    if drink == 'espresso':
        if money >= ESPRESSO_COST:
            balance = money - ESPRESSO_COST
            print(f"Here is ${balance} dollars in change.")
            return 1
        else:
            print(f"Sorry that's not enough money. Money refunded. ${money}")
            return 0
    elif drink == 'latte':
        if money >= LATTE_COST:
            balance = money - LATTE_COST
            print(f"Here is ${balance} dollars in change.")
            return 1
        else:
            print(f"Sorry that's not enough money. Money refunded. ${money}")
            return 0
    elif drink == 'cappuccino':
        if money >= CAPPUCCINO_COST:
            balance = money - CAPPUCCINO_COST
            print(f"Here is ${balance} dollars in change.")
            return 1
        else:
            print(f"Sorry that's not enough money. Money refunded. ${money}")
            return 0


machine_on = True
while machine_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink_choice == 'report':
        report()
    elif process_coins(drink_choice) == 1:
        check_resource(drink_choice)
    elif drink_choice == "off":
        print("Switching off...")
        machine_on = False
        break
