import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("triangle")
timmy.speed("fastest")
turtle.colormode(255)
directions = [0, 90, 180, 270]
timmy.pensize(5)

def dashed_line ():
    for x in range(18):#linie intrerupta
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def geometric_figures():
    for x in range (6):
        timmy.color(random_color())
        y = 360
        z = 3 + x
        for h in range (z):
            timmy.forward(30)
            timmy.rt(y / z)
        z +=1

def random_directions():
    for x in range (100):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))

def circle_figure(nr_circle):
    for x in range (int(360/nr_circle)):
        timmy.color(random_color())
        timmy.circle(90)
        timmy.setheading(timmy.heading()+nr_circle)


#dashed_line()
#geometric_figures()
#random_directions()
circle_figure(1)

screen = Screen() #Cream ecranul
screen.exitonclick() #clic > X
