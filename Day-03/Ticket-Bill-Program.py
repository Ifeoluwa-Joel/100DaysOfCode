height = int(input("What is your height? (in metres) "))
age = int(input("How old are you? "))
bill = 0

wants_photo = input("Do you want photo taken? Y/N ")

# midlife_crisis = age >= 45 and age <= 55
midlife_crisis = 45 <= age <= 55

if height >= 120:
    print("You can go on the rollercoaster")

    if age < 12:
        print("Children's price is $5")
        bill += 5

    elif age < 18:
        print("Teenagers' price is $7")
        bill += 7

    elif midlife_crisis == True:
        print("Ouch! You are in midlife crisis.\nYou have a free ride.")
        bill += 0

    else:
        print("Adult price is $12")
        bill = 12

    if wants_photo == "Y":
        bill += 3

    print(f'Your ticket price is: ${bill}')

else:
    print("Sorry, you can't go on the rollercoaster.")
