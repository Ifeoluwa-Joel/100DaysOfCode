"""FROM YOUTUBE --> https://www.youtube.com/watch?v=JeznW_7DlB0"""

# CLASS ATTRIBUTES
"""
Class attributes are attributes that are specific to the class and not to an instance or an object of that class.
"""


class Person:
    number_of_people = 0  # Class Attribute
    GRAVITY = -9.8  # Class Attribute

    def __init__(self, name):  # Class Method
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):  # Class Method
        return cls.number_of_people

    @classmethod
    def add_person(cls):  # Class Method
        cls.number_of_people += 1


p1 = Person("Tim")
print(Person.number_of_people_())
p2 = Person("Jill")
print(Person.number_of_people_())
p3 = Person("Jack")
print(Person.number_of_people_())

# -# STATIC CLASSES ###########
"""
This is used so that methods in a class can be organized and be imported to another class
where they can be used independent of anything from the original file.
Like the Math class, we don't have to create an instance of the Maths class to be able to use the class'
functions. We just use the functions in any module where the Math class is imported.
Static means they don't change anything. Which is why we do not use 'self' or 'cls' in them.
"""


class Math:
    @staticmethod
    def add5(x):
        """
        :param x: adds 5 to x
        :return: the sum of x and 5
        """
        return x + 5


print(Math.add5(10))
