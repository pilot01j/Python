from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def turn_left():
    new_heding = timmy.heading() + 10
    timmy.setheading(new_heding)


def turn_right():
    timmy.right(10)


def turn_back():
    timmy.backward(10)

def clear():
    timmy.home()
    timmy.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_back, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")

screen.exitonclick()
