# Turtle Intro #

import turtle as t

tim = t.Turtle(visible=True)
tim.shape("classic")
tim.color("coral")

# Challenge 1 - Draw a Square #
for _ in range(4):
    tim.right(90)
    tim.forward(100)

screen = t.Screen()
screen.title("Turtle Challenge 1")
screen.exitonclick()
