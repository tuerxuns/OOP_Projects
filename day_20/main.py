import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Ssssnake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # fmt: off
    if (
            (snake.head.xcor() > 280)
            or (snake.head.xcor() < -290)
            or (snake.head.ycor() > 290)
            or (snake.head.ycor() < -280)
    ):
        # fmt: on
        scoreboard.new_highscore()
        snake.snake_reset()

    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.new_highscore()
            snake.snake_reset()

screen.exitonclick()
