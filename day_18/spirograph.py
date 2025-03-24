import random
from turtle import Turtle, Screen

timmy = Turtle()


def random_color():
    color = tuple(random.randint(0, 255) for _ in range(3))
    return color


def circle_drawer(circles):
    for _ in range(circles):
        # noinspection PyTypeChecker
        timmy.color(random_color())
        timmy.circle(200)
        timmy.left(360 / circles)


def main():
    timmy.shape("turtle")
    timmy.pensize(1)
    timmy.speed(0)
    screen = Screen()
    screen.colormode(255)
    circle_drawer(120)
    screen.exitonclick()


main()
