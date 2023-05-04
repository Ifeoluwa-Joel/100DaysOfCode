import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("WELCOME TO ROCK-PAPER-SCISSORS GAME!")
print("Play against the Computer in this fast-paced rock-paper-scissors game.")
print("RULES: Use 'R' to denote rock, 'P' to denote paper and 'S' to denote scissors.\nEnjoy your game.")
print("")

score = 0
# User Gameplay
user_input = input("Show gesture ")
user_gesture = user_input.lower()

# Computer Gameplay
com_input = random.randint(0,2)
if (com_input == 0):
    com_gesture = 'r'
elif (com_input == 1):
    com_gesture = 'p'
else:
    com_gesture = 's'


if (user_gesture == 'r' and com_gesture == 's'):
    print(f'You chose: ROCK\nCOM chose: Scissors')
    print(f'{rock}\nYOU WIN!')
elif (user_gesture == 's' and com_gesture == 'p'):
    print(f'You chose: Scissors\nCOM chose: Paper')
    print(f'{scissors}\nYOU WIN!')
elif (user_gesture == 'p' and com_gesture == 'r'):
    print(f'You chose: Paper\nCOM chose: Rock')
    print(f'{paper}\nYOU WIN!')
elif (com_gesture == 'r' and user_gesture == 's'):
    print(f'You chose: Scissors\nCOM chose: Rock')
    print("COM WINS\nGame Over")
elif (com_gesture == 's' and user_gesture == 'p'):
    print(f'You chose: Paper\nCOM chose: Scissors')
    print("COM WINS\nGame Over")
elif (com_gesture == 'p' and user_gesture == 'r'):
    print(f'You chose: Rock\nCOM chose: Paper')
    print("COM WINS\nGame Over")
elif (com_gesture == 'p' and user_gesture == 'p'):
    print(f' You chose: {user_gesture}\n COM chose:{com_gesture}')
    print("It's a draw.\nTry again!")

elif (com_gesture == 'r' and user_gesture == 'r'):
    print(f' You chose: {user_gesture}\n COM chose:{com_gesture}')
    print("It's a draw.\nTry again!")

elif (com_gesture == 's' and user_gesture == 's'):
    print(f' You chose: {user_gesture}\n COM chose:{com_gesture}')
    print("It's a draw.\nTry again!")

else:
    print("You doofus! You have entered an invalid input")
    print("Game Over!")
