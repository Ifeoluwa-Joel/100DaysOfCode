from turtle import Turtle, Screen
from random import randint

is_race_on = False
window = Screen()
window.title("The Turtle Race!")
window.setup(width=500, height=400)
window.bgpic(picname='racetrack.gif')
user_bet = window.textinput(title="Choose player", prompt="Which turtle will win the race? ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

color_index = 0
y_position = 125
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[color_index])
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)
    color_index += 1
    y_position -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on =  False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle wins!")
            else:
                print(f" You lost. The {winning_color} turtle won.")

        turtle_pace = randint(0, 10)
        turtle.forward(turtle_pace)


window.exitonclick()
