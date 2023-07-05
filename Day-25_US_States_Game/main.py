import turtle
import pandas
from scoreboard import Scoreboard

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

is_game_on = True
guessed_states = []
lives = 3
while is_game_on:
    answer_state = screen.textinput(title=f"({scoreboard.score}/50) Guess the State",
                                    prompt="Enter the name of a State: ").title()

    if answer_state == 'Exit':
        break
    if answer_state in guessed_states:
        continue

    # Get Hold of the States column in the CSV and check each state against 'answer_state'.
    # If a state matches answer state go ahead and place answer_state in the coordinates of that state read
    # from the .csv file
    for state in data.state:
        if answer_state == state:
            selected_state = data[data.state == answer_state]
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            tim.goto(selected_state.x.item(), selected_state.y.item())
            tim.write(answer_state)
            scoreboard.update_score()
            guessed_states.append(answer_state)  # To ensure player don't guess states twice to statpad

    if scoreboard.score == 50:
        is_game_on = False

# turtle.mainloop()

# states to learn.csv
all_states = data.state.to_list()
missing_states = []
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)


unguessed_data = pandas.DataFrame(missing_states)
unguessed_data.to_csv("C:/Users/Ifeoluwa Joel/Desktop/states_to_learn.csv")
