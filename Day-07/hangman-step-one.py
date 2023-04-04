import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Generate an index to randomly choose from word_list
word_list_index = random.randint(0, 2)

# TODO 1
chosen_word = word_list[word_list_index]
# Angela did: chosen_word = random.choice(word_list)    Why didn't I think of that?!

# TODO 2
guess = input("Guess a letter: ").lower()

# TODO 3
for char in chosen_word:
    if guess == char:
        print('Right')
    else:
        print('Wrong')

print(chosen_word)
