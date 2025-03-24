import random
import turtle
from turtle import Turtle, Screen
from hirst_colors import colors_list

DOT_SIZE = 40
DOT_SPACING = DOT_SIZE * 2.5
GRID_SIZE = 10

screen = Screen()
screen.setup(width=0.50, height=1.0)
screen.title("Hirst Dot Painting")
turtle.colormode(255)

brush = Turtle()
brush.speed(0)
brush.up()


def random_color():
    color = random.choice(colors_list)
    return color


def spot_painter():
    brush.dot(DOT_SIZE, random_color())


def painter(grid_size, dot_spacing):
    size = grid_size * dot_spacing
    start_x = -size / 2
    start_y = -size / 2
    brush.teleport(start_x, start_y)

    for row in range(grid_size):

        for col in range(grid_size):
            spot_painter()

            if col < grid_size - 1:
                brush.forward(dot_spacing)

        next_y = start_y + (row + 1) * dot_spacing
        brush.teleport(start_x, next_y)


def main():
    painter(grid_size=GRID_SIZE, dot_spacing=DOT_SPACING)
    screen.exitonclick()


main()
