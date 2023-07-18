# new_dict = {new_key:new_value for item in list}   --> comprehend a new dictionary from a list
# new_dict = {new_key:new_value for (key, value) in existing_dict.items()} --> comprehend new dict from an existing dict
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in existing_dict.items() if test}


import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: score
    for (student, score) in student_grades.items() if score >= 39
}
print(passed_students)