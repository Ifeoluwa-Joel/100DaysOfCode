from turtle import Turtle, Screen
from random import choice

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 'yellow',
           "SeaGreen", "red", "DarkSlateGray4", "LimeGreen", "MistyRose4", 'sienna', 'Red', 'RoyalBlue4', 'SeaGreen4',
           'orange red', 'dark red']
direction = [0, 90, 180, 270]

tim = Turtle(visible=False)
tim.pensize(5)
tim.speed(0)


def random_walk():
    tim.color(choice(colours))
    tim.forward(30)
    tim.setheading(choice(direction))


moves = 0
while moves < 10000:
    random_walk()
    moves += 1

window = Screen()
window.exitonclick()
