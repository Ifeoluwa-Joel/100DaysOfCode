sum = 0
for number in range(0, 101, 2):
    sum += number
print(sum)

# Alternate way
total = 0
for number in range(1,101):
    if (number % 2 == 0):
        total += number
print(total)