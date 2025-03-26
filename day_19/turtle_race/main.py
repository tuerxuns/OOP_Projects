from turtle import Turtle, Screen
from random import randrange

start_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Place your bets!",
    prompt="Which turtle do you think will win? Enter a colour: ",
)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtle_racers = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle_racers.append(new_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in turtle_racers:
        if turtle.xcor() > 230:
            start_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        random_distance = randrange(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
