from turtle import Turtle, Screen


# Draw a dashed line
tim = Turtle()
tim.shape("classic")
tim.color("coral")
for _ in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.title("Turtle Challenge 2")
screen.exitonclick()
