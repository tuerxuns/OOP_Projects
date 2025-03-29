import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
turtle.movement("Up", "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_spawn()
    car.car_move()

    for c in car.all_cars:
        if c.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.finish_line():
        turtle.goto_start()
        car.car_level()
        scoreboard.level_up()

screen.exitonclick()
