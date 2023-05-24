# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)

from turtle import Turtle, Screen

timmy = Turtle()  # Creating an object from a blueprint
print(timmy)
timmy.shape('turtle')  # Calling methods of the object
timmy.color('coral')  # Calling methods of the object
timmy.forward(100)  # Calling methods of the object

# What can we do with this object?
# Object attributes
my_screen = Screen()
print(my_screen.canvheight)  # Tapping into the object attributes
print(my_screen.canvwidth)  # Tapping into the object attributes
my_screen.exitonclick()
