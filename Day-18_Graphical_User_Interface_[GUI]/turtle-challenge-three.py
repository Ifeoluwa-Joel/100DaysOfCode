from turtle import Turtle, Screen


# Draw various shapes
# triangle, square, pentagon, hexagon, heptagon
# octagon, nonagon and decagon
tim = Turtle()
screen = Screen()


def draw_triangle():
    for _ in range(3):
        tim.color("red")
        tim.forward(100)
        tim.right(120)


def draw_square():
    for _ in range(4):
        tim.color("DarkSlateGray4")
        tim.forward(100)
        tim.right(90)


def draw_pentagon():
    for _ in range(5):
        tim.color("LimeGreen")
        tim.forward(100)
        tim.right(72)


def draw_hexagon():
    for _ in range(6):
        tim.color("MistyRose4")
        tim.forward(100)
        tim.right(60)


def draw_heptagon():
    for _ in range(7):
        tim.color('sienna')
        tim.forward(100)
        tim.right(51.4385)


def draw_octagon():
    for _ in range(8):
        tim.color('Red')
        tim.forward(100)
        tim.right(45)


def draw_nonagon():
    for _ in range(9):
        tim.color('RoyalBlue4')
        tim.forward(100)
        tim.right(40)


def draw_decagon():
    for _ in range(10):
        tim.color('SeaGreen4')
        tim.forward(100)
        tim.right(36)


draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()
draw_heptagon()
draw_octagon()
draw_nonagon()
draw_decagon()

screen.title("Turtle Challenge 3")
screen.exitonclick()
