# import colorgram
# extracted_colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in extracted_colors:
#     rgb = color.rgb
#     color_tuple = (rgb.r, rgb.g, rgb.b)
#     color_list.append(color_tuple)
# print(color_list)

import turtle as t
import random
tim = t.Turtle(visible=False)
t.colormode(255)

tim.pencolor("white")
tim.speed("fastest")
color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205),
              (223, 178, 169)]


def draw_hirst_row(x_cor, y_cor):
    tim.setposition(x_cor, y_cor)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


horizontal_cor = -250
vertical_cor = 250
for _ in range(10):
    draw_hirst_row(horizontal_cor, vertical_cor)
    vertical_cor -= 50

window = t.Screen()
window.exitonclick()
