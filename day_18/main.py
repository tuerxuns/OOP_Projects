import random
from turtle import Turtle, Screen

timmy = Turtle()


def random_color():
    color = tuple(random.randint(0, 255) for _ in range(3))
    return color


def shape_drawer(sides):
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)
    # noinspection PyTypeChecker
    timmy.color(random_color())


def main():
    timmy.shape("turtle")
    screen = Screen()
    screen.colormode(255)

    requested_sides = int(input("How many sides would you like to go up to? "))
    for shape_sides in range(3, requested_sides + 1):
        shape_drawer(shape_sides)

    screen.exitonclick()


if __name__ == "__main__":
    main()
