import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 'yellow',
           "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')


for _ in range(300):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
