import turtle as t
from data import color_list
from random import choice

tim = t.Turtle()

num_sides = 3
while num_sides <= 10:
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
    num_sides += 1
    tim.color(choice(color_list))

screen = t.Screen()
screen.exitonclick()
