import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
data = states_data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess State Name", prompt="What's another state?").title()
    if answer_state == "Exit":
        break
    if answer_state in data:
        guessed_states.append(answer_state)
        result = states_data[states_data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(result.x), int(result.y))
        t.write(answer_state, move=True, align="center")

states = {
    "states": guessed_states
}
data_from_csv = pandas.DataFrame(states)
data_from_csv.to_csv("guessed_states.csv")


