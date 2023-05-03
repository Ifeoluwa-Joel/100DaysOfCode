def factorial(num):
    prod = 1
    for digit in range(1, num + 1):
        prod *= digit
    return prod


print(factorial(3))
#  I have achieved this without recursion. I want to use Recursion to solve it. I will do that tomorrow

total = 0
for number in range(10001):
    total += number
print(total)
