print('''
  ________________ _     _____      ____________
  ,' ________   ___// \    \  __`-.  /___   ___/
 |  `-.__    | |   / . \   | |,',-'      | | 
  `-.___ `,  | |  / /_\ \  |  _ `-,      | | 
  ______\  \ | | / _____ \ | | `-. \_    | | 
 /_________| /_|/_/     \_\|_\   /__/    /_\ 
''')


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")


score = 0
start_game = input("Start Game? Y/N\n")

if (start_game == 'Y'):
    crossroad_choice = input("You are at a crossroad. Do you want to go right or left?\n")
    first_choice = crossroad_choice.lower()

    if (first_choice == 'left'):
        print("You successfully got to the lake.")
        score += 1

        lake_choice = input("Do you want to swim or wait for boat")
        second_choice = lake_choice.lower()
        if (second_choice == 'boat'):
            print("You have successfully arrived at the Island")
            score += 1

            island_choice = input("You have three doors in front of you. Red, Yellow and Blue. Pick one")
            third_choice = island_choice.lower()
            if (third_choice == 'red'):
                print("You fell into Mount Doom. You are toast.\nGAME OVER!")
                score += 0

            elif (third_choice == 'blue'):
                print("You were trapped in ice.\nGAME OVER")
                score += 0

            else:
                print("YOU_WIN!\nYou got the treasure!\nGAME WON!")
                score += 1


        else:
            print("You drowned. Mermaids ate you.\nGAME OVER!")
            score += 0

    else:
        print("You stepped on a landline.\nGAME OVER!")
        score += 0

else:
    print("Okay. Come back later.")


print(f'Your score is {score}.')
