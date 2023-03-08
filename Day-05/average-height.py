# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

# Convert each element in the list to integer
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# My SOLUTION

# Add all items in the list
sum = 0
for i in student_heights:
  sum += i

# Count all items in the list
count = 0
for c in student_heights:
  count += 1

# Find the average and round to nearest whole number
average = sum / count
average = round(average)
print(average)


# Angela's Solution
total_height = 0
for height in student_heights:
  total_height += height

total_student = 0
for student in student_heights:
  total_student += 1

avg = round(total_height / total_student)
print(avg)

