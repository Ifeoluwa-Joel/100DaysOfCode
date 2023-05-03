############### Blackjack Project #####################

#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.

############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
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


import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_total = 0
dealer_total = 0

def deal_card():
    """ Looks into the card deck and returns one card"""
    chosen_card = random.choice(cards)
    return chosen_card

def sum_cards(list):
    """Takes a list and return the sum of all items in the list"""
    sum_card = 0
    for item in list:
        sum_card += item
    return sum_card

def has_blackjack(player_cards):
    """decides if any player has an Ace and 10
    It returns either True or False"""
    if 11 in player_cards:
        if 10 in player_cards:
            if sum_cards(player_cards) == 21:
                return True

def BlackJackGame():
    game_over = False
    while not game_over: # Main game loop
        print(logo)
        # Give starting hands to both dealer and user
        user_cards = []
        user_cards.append(deal_card())
        user_cards.append(deal_card())

        dealer_cards = []
        dealer_cards.append(deal_card())
        dealer_cards.append(deal_card())

        # Check Blackjack☠️☠️
        user_black_jack = False
        dealer_black_jack = False
        if has_blackjack(user_cards):
            user_black_jack = True
        if has_blackjack(dealer_cards):
            dealer_black_jack = True

        # Calculate scores based on card values
        user_total = sum_cards(user_cards)
        dealer_total = sum_cards(dealer_cards)

        print(f'Player Cards: {user_cards}, current score: {user_total}')
        print(f'Dealer Cards: {dealer_cards[0]}, _')

        # Hit or Stand
        hit = input("Do you want another card? (y/n) ")
        if hit == 'y':
            while hit == 'y':
                user_cards.append(deal_card())
                user_total = sum_cards(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_total}")
                if 11 in user_cards and user_total > 21:
                    user_total -= 10
                elif user_total > 21:
                    print(f"BUST! 💥\n"
                          f"Your total is {user_total}. You lost!")
                    game_over = True
                    break # Break out of the hit or stand loop
                hit = input("Do you want another card? (y/n) ")
                # Decide if user has overhitted and BUST immediately
                if hit == 'y':
                    continue
            if user_total > 21:
                break # Break out of main game loop. This is necessary so
                    # that after bust, the game will not go on to score comparison again


        while dealer_total < 16:
            dealer_cards.append(deal_card())
            dealer_total = sum_cards(dealer_cards)


        # Calculate user total again too - in case he chose more cards after first total
        user_total = sum_cards(user_cards)

        # Ace is 11 unless when total is over 21 when it becomes 1
        if 11 in user_cards and user_total > 21:
            user_total -= 10

        if 11 in dealer_cards and dealer_total > 21:
            dealer_total -= 10



        # DECIDE GAME BY VARIOUS LOGICS. Let's Go!
        # Decider 1 - The BLACKJACK Rule☠️☠️
        # Check if there is winner based on Blackjack☠️☠️ rule (Ace + 10)
        if dealer_black_jack:
            print("Dealer has BLACKJACK!❎\nDealer wins\nYou Lost")
            print(f"Dealer Cards: {dealer_cards} = {dealer_total}")
            game_over = True
            break
        elif user_black_jack and not dealer_black_jack:
            print("BLACKJACK! YOU WIN! ✅✔️")
            print(f"Player Cards: {user_cards} = {user_total}")
            game_over = True
            break
        elif user_black_jack and dealer_black_jack:
            print("PUSH!\nDealer and Player has BLACKJACK!")
            print(f"Player Cards: {user_cards} = {user_total}")
            print(f"Dealer Cards: {dealer_cards} = {dealer_total}")
            game_over = True
            break

        # Decider 2 - The BUST rule 💥
        # Check if user has over 21
        # if user_total > 21:
        #     print(f"BUST! 💥\n"
        #           f"Your total is {user_total}. You lost!")
        #     game_over = True
        #     break

        if dealer_total > 21:
            print(f"Dealer BUST! 💥\n"
                  f"Dealer total is {dealer_total}. You WIN!")
            game_over = True
            break

        # Decider 3 - Score Comparison
        # Decide using score comparison
        if dealer_total > user_total and dealer_total <= 21:
            print(f"Player Cards: {user_cards} = {user_total}")
            print(f"Dealer Cards: {dealer_cards} = {dealer_total}")
            print("Dealer wins. YOU LOST!")
            game_over = True
            break

        elif user_total > dealer_total and user_total <= 21:
            print(f"Player Cards: {user_cards} = {user_total}")
            print(f"Dealer Cards: {dealer_cards} = {dealer_total}")
            print("YOU WIN!!! 🎇🎇")
            game_over = True
            break


        elif user_total == dealer_total:
            print(f"Player Cards: {user_cards} = {user_total}")
            print(f"Dealer Cards: {dealer_cards} = {dealer_total}")
            print("PUSH. It is a tie.")
            game_over = True
            break
        # End of Main Game Loop

    play_again = input('\nWill you like to play Blackjack again?(y/n) ')
    if play_again == 'y':
        BlackJackGame()
    # End of BlackJackGame()

BlackJackGame()