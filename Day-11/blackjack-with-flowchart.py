############### Blackjack Project #####################

#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.

############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
com_cards = []
user_total = 0
com_total = 0


def deal_card():
    return random.choice(cards)

def sum_cards(list):
    total = 0
    for item in list:
        total += item
    return total

def has_blackjack(player_cards):
    """decides if any player has an Ace and 10
    It returns either True or False"""
    if 11 in player_cards:
        if 10 in player_cards:
            if sum_cards(player_cards) == 21:
                return True

game_over = False
while not game_over: #Main game loop
    print(logo)

    # Deal 2 starting cards to both players
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    com_cards.append(deal_card())
    com_cards.append(deal_card())

    user_total = sum_cards(user_cards)
    com_total = sum_cards(com_cards)
    print(f"User cards: {user_cards}, current score = {user_total}")
    print(f"COM cards: {com_cards[0]}, _")

    # Check for Blackjack before user is prompted for more cards
    user_has_blackjack = False
    com_has_blackjack = False
    if has_blackjack(user_cards):
        user_has_blackjack = True
        print("BLACKJACK! YOU WIN!!")
        print(f'Your cards: {user_cards}, current score is {user_total}')
        game_over = True
        break
    elif has_blackjack(com_cards):
        com_has_blackjack = True
        print("Computer has Blackjack! COM WINS!")
        print(f'COM cards: {com_cards}, current score is {com_total}')
        game_over = True
        break

    hit = input("Do you want another card? (y/n): ")
    if hit == 'y':
        while hit == 'y':
            user_cards.append(deal_card())
            user_total = sum_cards(user_cards)
            print(f'{user_cards}, current score: {user_total}')

            # Check for Blackjack
            user_has_blackjack = False
            com_has_blackjack = False
            if has_blackjack(user_cards):
                user_has_blackjack = True
                print("BLACKJACK! YOU WIN!!")
                print(f'Your cards: {user_cards}, current score is {user_total}')
                game_over = True
                break

            if user_total > 21:
                if 11 in user_cards:
                    user_total -= 10
                    print(f"Player Ace = 1. New score: {user_total}")
                    if user_total > 21:
                        print("BUST1! You went over 21.\nGame Over!")
                        print(f'Your cards: {user_cards}, Final score is {user_total}')
                        print('COM WINS!')
                        game_over = True
                        break
                else:
                    print("BUST2! You went over 21.\nGame Over!")
                    print(f'Your cards: {user_cards}, Final score is {user_total}')
                    print('COM WINS!')
                    game_over = True
                    break

            hit = input("Do you want another card? (y/n): ")
            if hit == 'y':
                continue
            else:
                break

    # If Bust or Blackjack has determined game;
    # Break out of main game loop also.
    if game_over:
        break

    # Computer plays now
    while com_total < 17:
        com_cards.append(deal_card())
        com_total = sum_cards(com_cards)

    if com_total > 21:
        if 11 in com_cards:
            com_total -= 10
            print(f"Computer Ace = 1. New score: {com_total}")
            if com_total > 21:
                print("COM_BUST1! COM overpicked and is over 21")
                print(f'COM cards: {com_cards}, Final score is {com_total}')
                print('YOU WIN!')
                game_over = True
                break
        else:
            print("COM_BUST2! COM overpicked and is over 21")
            print(f'COM cards: {com_cards}, Final score is {com_total}')
            print('YOU WIN!')
            game_over = True
            break

    # If Bust or Blackjack has determined game after COM play;
    # Break out of main game loop also.
    if game_over:
        break

    # As a last resort -->
    # Determine game with score comparisons
    if com_total > user_total:
        print("\nCOM WINS!")
        print(f"Your cards: {user_cards}, Final score is {user_total}")
        print(f"COM cards: {com_cards}, Final score is {com_total}")
        print("Game Over!")
        game_over = True
        break
    elif user_total > com_total:
        print("\nYOU WIN!")
        print(f"Your cards: {user_cards}, Final score is {user_total}")
        print(f"COM cards: {com_cards}, Final score is {com_total}")
        game_over = True
        break
    elif user_total > com_total:
        print("\nPUSH! It is a tie")
        print(f"Your cards: {user_cards}, Final score is {user_total}")
        print(f"COM cards: {com_cards}, Final score is {com_total}")
        game_over = True
        break
