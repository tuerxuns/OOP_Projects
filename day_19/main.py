from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def move_forwards():
    bob.forward(10)


screen.listen()

screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
