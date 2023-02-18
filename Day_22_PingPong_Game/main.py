from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game.")
screen.tracer(0) #automation turn off

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #Detect de colision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    #Colision with r_padlle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        print("Colision")
        ball.bounce_x()

    #Detect de R paddle missing
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score()
    #Detect de L paddle missing
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
