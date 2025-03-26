from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Ssssnake")
screen.tracer(0)

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
