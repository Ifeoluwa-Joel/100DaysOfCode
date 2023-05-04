import random
# from art import logo


level = {"easy": 10, "hard": 5}


def guess_high_or_low(secret_num, user_guess):
    if secret_num > user_guess:
        return "Too low"
    elif user_guess > secret_num:
        return "Too high"


secret_number = random.randint(1, 100)
# print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
# print(f"Cheat: The number is {secret_number}")
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts_remaining = level[difficulty_choice]
print(f"You have {attempts_remaining} attempts remaining to guess the number.")

game_over = False
while not game_over:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
        game_over = True

    else:
        attempts_remaining -= 1
        print(guess_high_or_low(secret_number, guess))
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")

    if attempts_remaining == 0:
        print("You've run out of guesses, you lose.")
        print(f"The answer was: {secret_number}")
        game_over = True
        break
