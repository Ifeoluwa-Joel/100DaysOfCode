import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
com_cards = []


def deal_card():
    return random.choice(cards)


def calculate_score(list_parameter):
    score = sum(list_parameter)
    # Check for Blackjack
    if score == 21:
        if 11 in list_parameter:
            return 0
    # Check if Ace is in score over 21 and turn it to 1
    if score > 21 and 11 in list_parameter:
        list_parameter.remove(11)
        list_parameter.append(1)
        score = sum(list_parameter)
        return score
    return score


def compare(user_score, com_score):
    if com_score == user_score:
        return f"It is a Push!\nUser scored: {user_score} & Computer scored: {com_score}"
    elif com_score == 0:
        return f"COM BLACKJACK! Computer wins"
    elif user_score == 0:
        return f"BLACKJACK! You WIN!!"
    elif user_score > 21:
        return f"BUST! You went over 21\nGame Over!\nFinal Score: {user_score}"
    elif com_score > 21:
        return f"COM_BUST! Computer went over 21\nYou Win!\nScore:{com_score}"
    elif com_score > user_score:
        return f"COM WINS\nUser score: {user_score}\nComputer score: {com_score}\n.Game Over"
    elif user_score > com_score:
        return f"YOU WIN!\nUser score: {user_score}\nComputer score: {com_score}"


game_over = False
while not game_over:
    print(logo)

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    com_cards.append(deal_card())
    com_cards.append(deal_card())

    print(f'Player Cards: {user_cards}')
    print(f'Computer Cards: {com_cards[0]}, _')

    user_total = calculate_score(user_cards)

    more_cards = input("Do you want more cards? ")
    if more_cards == 'y':
        while more_cards == 'y':
            user_cards.append(deal_card())
            print(f'Player cards: {user_cards}')
            more_cards = input("Do you want more cards? ")
    user_total = calculate_score(user_cards)
    # Check user score for blackjack or bust after more cards
    if calculate_score(user_cards) == 0:
        game_decision = "BLACKJACK! User wins"
    elif calculate_score(user_cards) > 21:
        game_decision = f"BUST! You went over 21. Final score: {user_total}"

    com_total = calculate_score(com_cards)
    while com_total < 17:
        com_cards.append(deal_card())
        com_total = calculate_score(com_cards)

    print(f'Computer cards: {com_cards}')
    print(compare(user_score=user_total, com_score=com_total))

    play_again = input("Do you want to enjoy Blackjack again? (y/n)")
    if play_again == 'y':
        continue
    else:
        game_over = True
