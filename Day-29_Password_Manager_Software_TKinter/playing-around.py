git# Just playing around with nested lists
# Goal is to build a nested list like this [('John', 184, 84.5),  ('Ryan', 177, 81.8), ...]

heights = [184, 177, 190, 188, 159, 166]
weights = [84.5, 81.8, 86.1, 92.2, 69.6, 72.0]
names = ['John', 'Ryan', 'Bobby', 'Pete', 'Esther', 'Jane']

person_data = []
for item in range(len(names)):
    person = (names[item], heights[item], weights[item])
    person_data.append(person)

print(person_data)
