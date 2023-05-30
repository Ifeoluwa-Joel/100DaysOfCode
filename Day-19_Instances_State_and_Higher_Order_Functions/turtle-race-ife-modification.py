from turtle import Turtle, Screen
from random import randint

race_on = False
window = Screen()
window.title("The Turtle Race!")
window.setup(width=1410, height=735, starty=0, startx=0)
window.bgpic(picname='racetrack.gif')
user_bet = window.textinput(title="Choose player", prompt="Which turtle will win the race? ")
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
all_turtles = []

color_index = 0
y_position = 150
for _ in range(7):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(color_list[color_index])
    tim.penup()
    tim.goto(x=-670, y=y_position)
    all_turtles.append(tim)
    color_index += 1
    y_position -= 50

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        turtle_pace = randint(0, 10)
        turtle.forward(turtle_pace)
        if turtle.xcor() > 650:
            race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won!")
            else:
                print(f"You lost. The {winning_color} turtle won.")


window.exitonclick()
