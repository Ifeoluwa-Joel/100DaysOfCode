import pandas
nasa_csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nasa_phonetic_dictionary = {
    row.letter: row.code
    for (index, row) in nasa_csv_data.iterrows()
}
# print(nasa_phonetic_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word_input = input("Enter the word: ")
phonetic_list = [nasa_phonetic_dictionary[char.title()] for char in user_word_input]
print(phonetic_list)
