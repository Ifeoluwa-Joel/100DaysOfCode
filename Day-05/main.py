#For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

# Playing around
print("\nMULTIPLE INPUTS")
clubs = input("Enter the list of clubs - separated by commas\n").split(",")

print(clubs)
print(f'{clubs[0]} is the boss of {clubs[1]}, {clubs[2]} and {clubs[3]}')