import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print('''
         88 88                        
         88 ""                        
         88                           
 ,adPPYb,88 88  ,adPPYba,  ,adPPYba,  
a8"    `Y88 88 a8"     "" a8P_____88  
8b       88 88 8b         8PP"""""""  
"8a,   ,d88 88 "8a,   ,aa "8b,   ,aa  
 `"8bbdP"Y8 88  `"Ybbd8"'  `"Ybbd8"'  
''')

print("START GAME")

roll = input("Roll Dice? ")
if (roll == 'y'):
    print(f'{dice1}-{dice2}')
    # Concatenate dice scores and convert back to integer
    dice1_str = str(dice1)
    dice2_str = str(dice2)
    two_dice = dice1_str + dice2_str
    two_dice_int = int(two_dice)

    # Decide Winner
    if (two_dice_int == 66):
        print("DEUCE! You win!!")
        print('''
                           88                                          
                           ""                                       
                                                                     
        8b      db      d8 88 8b,dPPYba,  8b,dPPYba,  ,adPPYba, 8b,dPPYba,  
        `8b    d88b    d8' 88 88P'   `"8a 88P'   `"8a a8P_____88 88P'   "Y8  
         `8b  d8'`8b  d8'  88 88       88 88       88 8PP""""""" 88          
          `8bd8'  `8bd8'   88 88       88 88       88 "8b,   ,aa 88          
            YP      YP     88 88       88 88       88  `"Ybbd8"' 88                  
        ''')

    elif (two_dice_int == 61 or two_dice_int == 62 or two_dice_int == 63 or two_dice_int == 64 or two_dice_int == 65):
        print("Sooo close!\nYou only need one more 6!")

    elif (two_dice_int == 16 or two_dice_int == 26 or two_dice_int == 36 or two_dice_int == 46 or two_dice_int == 56):
        print("Sooo close!\nYou only need one more 6!")

    else:
        print("Hard Luck! You couldn't get a deuce.\nRoll again.")
