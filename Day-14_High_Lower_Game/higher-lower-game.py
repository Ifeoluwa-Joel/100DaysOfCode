# Import necessary modules and files
import random
from game_data import data
from art import *

# Get Contestant 1 info
contestant1_index = random.randint(0, 49)
contestant1_name = data[contestant1_index]['name']
contestant1_followers = data[contestant1_index]['follower_count']
contestant1_bio = data[contestant1_index]['description']
contestant1_country = data[contestant1_index]['country']

# Get Contestant 2 info
contestant2_index = random.randint(0, 49)
if contestant2_index == contestant1_index:
    contestant2_index = random.randint(0,49)
contestant2_name = data[contestant2_index]['name']
contestant2_followers = data[contestant2_index]['follower_count']
contestant2_bio = data[contestant2_index]['description']
contestant2_country = data[contestant2_index]['country']

score = 0


# Compare function that can compare and return if a guess is right or wrong plus add 1 to score
def compare(contestant_a_followers, contestant_b_followers, score):
    """decides if the user is correct, and prints message.
        Increments score if user is correct."""
    if data_from_console == 'a':
        if contestant_a_followers > contestant_b_followers:
            score += 1
            print(f"\nYou are right! Current score: {score}.")
            return
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
    else:
        if contestant_b_followers > contestant_a_followers:
            score += 1
            print(f"\nYou are right! Current score: {score}.")
            return
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            return


# Game
print(logo)
game_over = False
while not game_over:
    print(f"Compare A: {contestant1_name}, a {contestant1_bio}, from {contestant1_country}")
    print(vs)
    print(f"Against B: {contestant2_name}, a {contestant2_bio}, from {contestant2_country}")
    data_from_console = input("Who has more followers? Type 'A' or 'B': ").lower()
    compare(contestant1_followers, contestant2_followers, score)
    print(f"{contestant1_name}'s followers: {contestant1_followers}")  # Debug line. Remove
    print(f"{contestant2_name}'s followers: {contestant2_followers}")  # Debug line. Remove

    # Stop loop in case user is wrong
    if data_from_console == 'a':
        user_choice = contestant1_followers
    else:
        user_choice = contestant2_followers

    if user_choice < contestant1_followers or user_choice < contestant2_followers:
        game_over = True
        break

    # Find a way to shift contestant 2 to 1.
    contestant1_index = contestant2_index
    contestant1_name = data[contestant1_index]['name']
    contestant1_followers = data[contestant1_index]['follower_count']
    contestant1_bio = data[contestant1_index]['description']
    contestant1_country = data[contestant1_index]['country']

    # Find a way to read in another random contestant into slot 2
    contestant2_index = random.randint(0, 49)
    contestant2_name = data[contestant2_index]['name']
    contestant2_followers = data[contestant2_index]['follower_count']
    contestant2_bio = data[contestant2_index]['description']
    contestant2_country = data[contestant2_index]['country']

    # Increase score by 1
    score += 1
