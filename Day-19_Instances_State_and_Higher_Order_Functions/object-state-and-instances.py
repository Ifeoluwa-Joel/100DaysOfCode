from turtle import Turtle, Screen
from random import randint

timmy = Turtle(shape='turtle')
tommy = Turtle(shape='turtle')
timmy.color('blue')
tommy.color('red')

for _ in range(10):
    timmy.setheading(0)
    timmy.forward(randint(20,80))
    tommy.setheading(180)
    tommy.forward(randint(20, 80))
timmy.write("I am Timmy")
tommy.write("I am Tommy")


window = Screen()
window.exitonclick()
