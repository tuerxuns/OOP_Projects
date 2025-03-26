from turtle import Turtle

STARTING_LENGTH = 3
MOVE_LENGTH = 20


class Snake:
    def __init__(self):
        self.snake_segment = []
        self.start_position = 0
        self.create_snake()

    def create_snake(self):
        for s_body in range(STARTING_LENGTH):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=self.start_position, y=0)
            self.snake_segment.append(new_snake)
            self.start_position -= MOVE_LENGTH

    def move(self):
        for seg in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg - 1].xcor()
            new_y = self.snake_segment[seg - 1].ycor()
            self.snake_segment[seg].goto(new_x, new_y)

        self.snake_segment[0].forward(MOVE_LENGTH)
