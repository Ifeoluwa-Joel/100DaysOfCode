from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # self.shape('circle')
        # self.shapesize(0.5)
        self.penup()
        self.color('gold')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = (randint(-275, 275))
        random_y = (randint(-275, 275))
        self.goto(random_x, random_y)
