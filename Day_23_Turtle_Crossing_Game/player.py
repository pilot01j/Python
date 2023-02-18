from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.lt(90)
        self.shape("turtle")
        self.shapesize(stretch_wid=1.4, stretch_len=1.4)
        self.color("red")
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
