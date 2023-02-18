import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detecting de colision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # Detect de syccessful crossing
    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.t_poit()

screen.exitonclick()
