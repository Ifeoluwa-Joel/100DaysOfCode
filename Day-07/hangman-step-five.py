#Step 5

import random
from hangman_words import *
from hangman_art import *

# Create a function to split strings into character. This is because of hint
def split_word(word):
    char_list = []
    for char in word:
        char_list.append(char)
    return char_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
hint_used = 0

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
print('\nWelcome to Hangman Game. Guess correctly and save your little man!')
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    # Do you want hint?
    if hint_used < 2:
        random_letter_in_chosen_word = random.choice(split_word(chosen_word))
        player_want_hint = input('Do you want hint? (Y/N) ').lower()
        if player_want_hint == 'y':
            print(random_letter_in_chosen_word)
            hint_used += 1

    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You have entered {guess} already! Try again!!')

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'{guess} is not in word. You have lost a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    elif guess not in alphabets:
        print('You wasted a guess. You have lost a life')
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f'Lives remaining: {lives}')

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print('''CONGRATULATIONS!. YOU WIN!!\n
                   88   
                   ""    
                                    
8b      db      d8 88 8b,dPPYba,     
`8b    d88b    d8' 88 88P'   `"8a    
 `8b  d8'`8b  d8'  88 88       88    
  `8bd8'  `8bd8'   88 88       88    
    YP      YP     88 88       88 ''')

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])

print(f'The word is: {chosen_word}')
