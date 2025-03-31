import turtle
import pandas
from writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = StateWriter()
score = 0

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
state_coords = {}

for state in states:
    state_data = data[data.state == state]
    x = int(state_data.x.iloc[0])
    y = int(state_data.y.iloc[0])
    state_coords[state] = (x, y)

while len(states) > 0:
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct", prompt="What's a state's name?"
    ).title()

    if answer_state == "Exit":
        states_to_learn = pandas.DataFrame(states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        score += 1
        states.remove(answer_state)
        writer.goto(state_coords[answer_state])
        writer.write(answer_state)
