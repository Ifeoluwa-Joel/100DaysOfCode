"""
Tried to write this without looking at any material other than documentation. This is a tacky but fun one.
Note to future self: You were once the worst coder on Planet Earth - Jeez!
"""

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)



window = Screen()
window.setup(width=600, height=400)
window.bgcolor('black')

dvd = Turtle(shape='circle')
dvd.penup()
dvd.color('gold')
dvd.shapesize(6, 6)
dvd.speed('fastest')


def wall_checker(turtle_object):
    """takes a turtle object and checks it x and y coordinates:
    :returns 0 if at the screen border"""
    if turtle_object.xcor() > 220 or turtle_object.xcor() < -230 or \
            turtle_object.ycor() > 140 or turtle_object.ycor() < -140:
        return 0


dvd.setheading(random.randint(0, 359))
screensaver_on = True
while screensaver_on:
    dvd.forward(10)
    if wall_checker(dvd) == 0:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        dvd.color((r, g, b))
        current_x = dvd.xcor()
        current_y = dvd.ycor()
        dvd.setheading(dvd.heading() + 150)

window.exitonclick()

