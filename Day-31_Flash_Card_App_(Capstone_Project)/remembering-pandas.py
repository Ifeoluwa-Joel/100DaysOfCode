import pandas

csv_data = pandas.read_csv("french_words.csv")
words_dataframe = pandas.DataFrame(csv_data)

print(words_dataframe)
print(words_dataframe.at[100, "English"])


