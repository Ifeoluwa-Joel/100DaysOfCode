"""FROM YOUTUBE --> https://www.youtube.com/watch?v=JeznW_7DlB0"""


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old ")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am a cat. My name is {self.name} and I am {self.age} years old. I am {self.color} in complexion")


class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Bark')

    def show(self):
        print(f"I am a dog. My name is {self.name} and I am {self.age} years old. I am a {self.color} dog.")

#
# c = Cat("Keanu", 45, "brown")
# c.show()
# c.speak()
#
# d = Dog("Bingo", 13, 'black')
# d.show()
# d.speak()


class Staff:
    def __init__(self, name, staff_id, auth_level, wage, department):
        self.name = name
        self.staff_id = staff_id
        self.auth_level = auth_level
        self.wage = wage
        self.department = department


class Manager(Staff):
    def __init__(self, name, staff_id, auth_level, wage, department, subordinates, package):
        super().__init__(name, staff_id, auth_level, wage, department)
        self.subordinates = subordinates
        self.package = package


class Worker(Staff):
    def __init__(self, name, staff_id, auth_level, wage, department, reputation):
        super().__init__(name, staff_id, auth_level, wage, department)
        self.reputation = reputation


m = Manager("Ifeoluwa Joel", '001', '10', 120000, 'Artificial Intelligence', 700, 'Overseer Benefit')
print(m.name)