"""FROM YOUTUBE --> https://www.youtube.com/watch?v=JeznW_7DlB0"""


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def bark(self):
        print("bark")


# bingo = Dog('Bingo', 10)
# print(bingo.get_name())
# print(bingo.get_age())

# STUDENTS EXAMPLE


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)




s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course('Calculus', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[1].name)
print(course.add_student(s3))
print(course.get_average_grade())
