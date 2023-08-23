# To make an argument optional in a function/method.
# We need to set a default value such that the code will
# not break when we call it without passing  anything to that function
# upon call.


def foo(a=1, b=2, c=3):
    print(a, b, c)


foo()


def foo_(a, b=4, c=6):
    print(a, b, c)


foo_(1)  # foo_() needs at least 1 positional argument because param a has no default value


# In cases where you want to make an argument optional but you don't have any value to assign to it
# function definition. Just assign None to it.


def foo__(a=1, b=None, c=3):
    print(a, b, c)


foo__(1, 8)
