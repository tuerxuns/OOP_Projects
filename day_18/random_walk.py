import random
from turtle import Turtle, Screen

timmy = Turtle()


def random_color():
    color = tuple(random.randint(0, 255) for _ in range(3))
    return color


def random_direction():
    direction = random.randrange(0, 360, 90)
    return direction


def shape_drawer(sides):
    for _ in range(sides):
        # noinspection PyTypeChecker
        timmy.color(random_color())
        timmy.setheading(random_direction())
        timmy.forward(25)


def main():
    timmy.shape("turtle")
    timmy.pensize(10)
    timmy.speed(10)
    screen = Screen()
    screen.colormode(255)
    shape_drawer(200)
    screen.exitonclick()


main()
