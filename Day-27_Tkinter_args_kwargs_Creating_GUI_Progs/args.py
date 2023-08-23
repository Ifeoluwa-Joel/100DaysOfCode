def add(*args):
    total = 0
    for number in args:
        total += number
    print(f"The sum is {total}")


add(10, 4, 5, 1, 3, 7)


# We can also refer to each of this arbitrary args by index.


def foo(*args):
    print(args[2])


foo(9, 4, 4, 5, 2, 5, 6, 7, 8, 9, 10)



"""
What if we want to refer to each of the arguments by name instead of index in the args tuple? 
Well, that's where **kwargs come in.

Check out that file.
"""