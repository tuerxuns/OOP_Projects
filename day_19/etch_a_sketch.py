from turtle import Turtle, Screen

drawer = Turtle()
screen = Screen()


def m_forward():
    drawer.forward(10)


def m_backwar():
    drawer.backward(10)


def t_clockwise():
    drawer.right(10)


def t_counterclockwise():
    drawer.left(10)


def clear_screen():
    drawer.penup()
    drawer.clear()
    drawer.home()
    drawer.pendown()


def movement():
    screen.onkey(key="w", fun=m_forward)
    screen.onkey(key="s", fun=m_backwar)
    screen.onkey(key="d", fun=t_clockwise)
    screen.onkey(key="a", fun=t_counterclockwise)
    screen.onkey(key="c", fun=clear_screen)


screen.listen()
movement()

screen.exitonclick()
