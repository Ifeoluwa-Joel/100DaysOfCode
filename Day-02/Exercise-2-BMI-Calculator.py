# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# int_weight = int(weight)
# int_height = float(height)

bmi = int(weight) / float(height) ** 2
print(int(bmi))
