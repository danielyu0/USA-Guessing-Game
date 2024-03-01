from turtle import Turtle,Screen
import pandas
import turtle


screen = Screen()
states_image = "empty_states_img.gif" # UI of the USA map
screen.addshape(states_image)
screen.title("USA States Game")
screen.setup(height=491,width=725)
turtle.shape(states_image)

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.color("black")

states_remaining = True
data = pandas.read_csv("50_states.csv") # 50 states list
all_states = data.state.to_list()
answered_list = []


while len(answered_list) < 50:
    answer_state = screen.textinput(title=f"{len(answered_list)}/50 States Correct", prompt="Name another State").title()

    if answer_state == "Exit": # Exits the loop when you cannot guess anymore and want to see what you could not guess
        missing_states = [states for states in all_states if states not in answered_list] 
        missing_state_data = pandas.DataFrame(missing_states)  
        missing_state_data.to_csv("States_to_learn.csv") # file with the missing states you could not guess
        break
    if answer_state in all_states:
        answer_row = data[data.state == answer_state]
        x_cords = float(answer_row.x.to_string(index=False))
        y_cords = float(answer_row.y.to_string(index=False))
        turtle.setposition(x_cords,y_cords)
        turtle.write(answer_state, align='center', font=('Arial', 8, 'normal'))
        answered_list.append(answer_state) 
