from turtle import Turtle

# Write the Ball Class and Make the Ball Move

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#20262E")
        self.penup()
        self.goto(x=0, y=-280)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Changing the Ball Speed
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -280)
        self.move_speed = 0.1
        self.bounce_y()
