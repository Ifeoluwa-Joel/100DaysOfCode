# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = input("Please input the sentence you want me to break and count: ")
new_dict = {word: len(word) for word in sentence.split()}
print(new_dict)
