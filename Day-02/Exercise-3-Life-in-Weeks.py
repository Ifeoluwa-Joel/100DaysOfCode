# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days_spent = int(age) * 365
days_left = (90 * 365) - days_spent

weeks_spent = int(age) * 52
weeks_left = (90 * 52) - weeks_spent

months_spent = int(age) * 12
months_left = (90 * 12) - months_spent

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')