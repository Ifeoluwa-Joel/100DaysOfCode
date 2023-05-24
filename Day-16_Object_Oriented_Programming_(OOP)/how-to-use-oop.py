class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def say_hi(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old!')
        # print('Hello, my name is ' + self.name + ' and I am ' + self.age + ' years old!')


p1 = Person('Bob', 25)
p1.say_hi()
