from art import *
from game_data import data
import random


# Format the account data into printable format
def format_data(account):
    """Takes the account data and returns a printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_descr}, from {account_country}.")


def check_answer(guess, a_followers, b_followers):
    """Takes user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Display art
# print(logo)
score = 0

account_b = random.choice(data)
"""
This was created here because we need to shift B to A and generate another value for B.
I will need to understand the flow of logic from top to bottom to understand this corner.
Check lines 38 to 42; for the continuation of this logic.

Note. It works for the first iteration where we don't need to worry about the shifting and subsequent iterations
when we do need to worry about it.
Bravo Angela. I did well in my approach too.
 """


# Make the game repeatable
game_should_continue = True
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f" Compare A: {format_data(account_a)}")
    # print(vs)
    print(f" Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get the follower count of each account
    a_follower_count = (account_a["follower_count"])
    b_follower_count = (account_b["follower_count"])

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry. That is wrong. Your final score is {score}.")
