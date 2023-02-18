from turtle import Turtle
import random
from typing import Tuple

colors =["red", "yellow", "blue", "green", "purple", "pink", "orange", "brown"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        self.food_color = random.choice(colors)
        self.color(self.food_color)
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)