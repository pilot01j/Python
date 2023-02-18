import time
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from score import Score

screen = Screen()
screen.setup(width=610, height=630)
screen.bgcolor("black")
screen.title('My Snake Game')

game_square = Turtle()
game_square.pensize(2)
game_square.color("white")
game_square.penup()
game_square.hideturtle()
game_square.goto(-280, -280)
game_square.pendown()
for _ in range (4):
    game_square.forward(560)
    game_square.left(90)

screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    point = 0
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detection collision with food.
    if snake.head.distance(food) < 20:
        print("Collision")
        food.refresh()
        snake.extend()
        score.increase_score()


    #Detection collision with wall.
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()

    #Detection collision with tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()