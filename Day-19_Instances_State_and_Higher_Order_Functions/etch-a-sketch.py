from turtle import Turtle, Screen

tim = Turtle()
window = Screen()
window.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


window.onkey(fun=move_forward, key='w')
window.onkey(fun=move_backward, key='s')
window.onkey(fun=turn_left, key='a')
window.onkey(fun=turn_right, key='d')
window.onkey(fun=clear_screen, key='c')

window.exitonclick()
