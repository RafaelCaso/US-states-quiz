import turtle
import pandas
from pen import Pen

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="Name a State").title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state.title() in all_states:
        state = data[data["state"] == answer_state.title()]
        guessed_states.append(answer_state)
        pen = Pen(state=answer_state.title(), x=int(state.x), y=int(state.y))
        pen.write_answer()




