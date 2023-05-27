import turtle as t
from random import choice

tim = t.Turtle(visible=False)

colors = ['medium aquamarine', 'lawn green', 'pale violet red', 'orange', 'dark goldenrod', 'honeydew', 'medium purple',
          'tan', 'yellow', 'gold', 'green', 'dark green', 'peach puff', 'orange red', 'dark cyan', 'dark red', 'maroon',
          'dark olive green', 'purple', 'red', 'blue', 'black', 'teal']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides_n in range(3, 11):
    tim.color(choice(colors))
    draw_shape(shape_sides_n)

screen = t.Screen()
screen.exitonclick()
