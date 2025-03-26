from turtle import Turtle

STARTING_LENGTH = [(0, 0), (-20, 0), (-40, 0)]
MOVE_LENGTH = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]
        self.last_direction = RIGHT

    def create_snake(self):
        for s_body in STARTING_LENGTH:
            self.add_segment(s_body)

    def move(self):

        for seg in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg - 1].xcor()
            new_y = self.snake_segment[seg - 1].ycor()
            self.snake_segment[seg].goto(new_x, new_y)

        self.head.forward(MOVE_LENGTH)

        self.last_direction = self.head.heading()

    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_segment.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_segment[-1].position())

    def up(self):
        if self.last_direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.last_direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_direction != LEFT:
            self.head.setheading(RIGHT)
