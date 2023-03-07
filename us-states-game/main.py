import turtle
import pandas
from state_write import StateWrite


data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_write = StateWrite()
states = data.state.to_list()


score = 0
correct_states = []



while score < 50:

    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's the name of another State?").title()
    if answer == "Exit":
        missed_states = [state for state in states if state not in correct_states]
        pandas.DataFrame(missed_states).to_csv("states_to_learn.csv")
        break

    if answer in states:
        score += 1
        correct_states.append(answer)
        x = data[data.state == answer].x
        y = data[data.state == answer].y
        state_write.fill_state(answer, int(x), int(y))




