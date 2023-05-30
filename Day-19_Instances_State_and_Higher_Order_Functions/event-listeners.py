from turtle import Turtle, Screen

tim = Turtle(visible=False)
window = Screen()


def move_forwards():
    tim.forward(10)


def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)


window.listen()
window.onkey(key="space", fun=move_forwards)
window.onkey(key="Left", fun=turn_left)
window.onkey(key="Right", fun=turn_right)

window.exitonclick()
