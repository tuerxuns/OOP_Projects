from turtle import Turtle

SPEED = 0.03


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.diff = 0.03
        self.x_move = self.diff
        self.y_move = self.diff

    def ball_move(self):
        x_move = self.xcor() + self.x_move
        y_move = self.ycor() + self.y_move
        self.goto(x_move, y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move = -self.x_move
        self.diff += 0.01
        self.x_move = self.diff if self.x_move > 0 else -self.diff
        self.y_move = self.diff if self.y_move > 0 else -self.diff

    def bounce_x(self):
        self.x_move = -self.x_move

    def reset_position(self):
        self.goto(0, 0)
        self.diff = 0.03
