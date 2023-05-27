import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    """returns a tuple containing 3 integers between 0.0 to 255.0
    meant to be R G and B respectfully"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed('fastest')

for _ in range(300):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(directions))

window = t.Screen()
window.exitonclick()
