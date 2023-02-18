import random
import turtle
import colorgram
from turtle import Turtle, Screen


def extract_color(nr_colors):
    """Extract colors from an image.jpg."""
    rgb_colors = []
    colors = colorgram.extract('image.jpg', nr_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)


timmy = Turtle()
turtle.colormode(255)
color_list = [(243, 234, 76), (211, 158, 93), (188, 12, 69),
              (111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166), (160, 78, 35), (128, 186, 146),
              (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95), (234, 165, 194), (79, 13, 63),
              (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132), (58, 165, 95), (135, 213, 228), (9, 102, 63),
              (134, 36, 21), (93, 29, 12), (156, 211, 190)]


def dot_colors():
    timmy.penup()
    timmy.hideturtle()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    nr_dots = 100
    for z in range(1, nr_dots+1):
        timmy.dot(15, random.choice(color_list))
        timmy.forward(30)
        if z % 10 == 0:
            timmy.setheading(90)
            timmy.forward(30)
            timmy.setheading(180)
            timmy.forward(30*10)
            timmy.setheading(0)


dot_colors()

screen = Screen()
screen.exitonclick()
