from turtle import Screen
from paddle import Paddles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddles((350, 0))
left_paddle = Paddles((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

right_paddle.movement("Up", "Down")
left_paddle.movement("w", "s")

game_on = True
while game_on:
    screen.update()
    ball.ball_move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.wall_bounce()

    # fmt: off
    if (
            ball.distance(right_paddle) < 50
            and ball.xcor() > 330
            or ball.distance(left_paddle) < 50
            and ball.xcor() < -330
    ):
        # fmt: on
        ball.paddle_bounce()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()
        ball.x_move = -ball.diff
        ball.y_move = ball.diff

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()
        ball.x_move = ball.diff
        ball.y_move = ball.diff

screen.exitonclick()
