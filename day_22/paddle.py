from turtle import Turtle, Screen

screen = Screen()


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_up(self):
        y_up = self.ycor() + 20
        self.goto(self.xcor(), y_up)

    def paddle_down(self):
        y_down = self.ycor() - 20
        self.goto(self.xcor(), y_down)

    def movement(self, up_key, down_key):
        screen.onkey(self.paddle_up, up_key)
        screen.onkey(self.paddle_down, down_key)
