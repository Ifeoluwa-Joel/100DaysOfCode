from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual number
def check_answer(guess, answer, turns):
    """checks guess against answer. Returns the no of turns remaining"""
    # Track the number of turns and reduce by 1 it they get it wrong
    if guess > answer:
        print("Too high")
        return turns - 1
    # Track the number of turns and reduce by 1 it they get it wrong
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it right! The answer was {answer}.")



# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random numer between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Psssst. The number is {answer}")

    turns = set_difficulty()

    # Repeat the guess functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
            # I would have used break, but since this game is in a function
            # <return> does the same thing in this circumstance








game()