def foo(**kwargs):
    print(kwargs)
    ans = 1
    for (key, value) in kwargs.items():
        ans *= value
    # print(ans)

foo(num1=3, num2=5)

# ###############################


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

# ########################
class Car:
    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw['model']
        """
        But in case if we will not supply all the attributes in the kw,
        this code will break. So we should use the get Method which would
        just return none
        """

        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(model='F150 RaptorR')

print(my_car.make)
print(my_car.model)


# Just trying to remember. Didn't code for two weeks
def calc(num, **kwargs):
    num += kwargs.get('add')
    num /= kwargs.get('divide')
    return num

print(calc(20, add=10, divide=2))