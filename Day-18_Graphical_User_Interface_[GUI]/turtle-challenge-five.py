import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')


def random_color():
    """returns a tuple containing 3 integers between 0.0 to 255.0
    meant to be R G and B respectfully"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

window = t.Screen()
window.exitonclick()
