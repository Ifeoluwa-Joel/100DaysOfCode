from turtle import Turtle, Screen
from random import randint

race_on = False
window = Screen()
window.title("The Turtle Race!")
window.setup(width=1410, height=735, starty=0, startx=0)
window.bgpic(picname='racetrack.gif')
user1_bet = window.textinput(title="Choose Player 1:", prompt="Which turtle will win the race? ")
user2_bet = window.textinput(title="Choose Player 2:", prompt="Which turtle will win the race? ")
color_list = [user1_bet, user2_bet]
all_turtles = []

color_index = 0
y_position = 100
for _ in range(2):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(color_list[color_index])
    tim.penup()
    tim.goto(x=-670, y=y_position)
    all_turtles.append(tim)
    color_index += 1
    y_position -= 200

if user1_bet and user2_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        turtle_pace = randint(0, 10)
        turtle.forward(turtle_pace)
        if turtle.xcor() > 640:
            race_on = False
            turtle.write('WIN!')
            winning_color = turtle.fillcolor()
            if winning_color == user1_bet:
                print(f"Player 1 won! The {winning_color} turtle won!")
            else:
                print(f"Player 2 won! The {winning_color} turtle won.")


window.exitonclick()
