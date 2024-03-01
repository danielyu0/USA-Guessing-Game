from turtle import Turtle,Screen
import pandas
import turtle


screen = Screen()
states_image = "empty_states_img.gif"
screen.addshape(states_image)
screen.title("USA States Game")
screen.setup(height=491,width=725)
turtle.shape(states_image)

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.color("black")

states_remaining = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answered_list = []


while len(answered_list) < 50:
    answer_state = screen.textinput(title=f"{len(answered_list)}/50 States Correct", prompt="Name another State").title()

    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in answered_list] # list comprehension replacement for 4 lines below
        missing_state_data = pandas.DataFrame(missing_states)  # 1 column data frame
        missing_state_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        answer_row = data[data.state == answer_state]
        x_cords = float(answer_row.x.to_string(index=False))
        y_cords = float(answer_row.y.to_string(index=False))
        turtle.setposition(x_cords,y_cords)
        # turtle.goto(int(answer_row.x), int(answer_row.y))     # can be used this 1 line instead of above 3 lines
        turtle.write(answer_state, align='center', font=('Arial', 8, 'normal'))
        answered_list.append(answer_state) # can use answer_row.state.item(), item returns first element





















# Adds the states cords to state
# states_dict = {
#     "states": ["Alabama", "Alaska",	"Arizona",	"Arkansas",	"California",	"Colorado",	"Connecticut",	"Delaware",	"Florida",	"Georgia",	"Hawaii",	"Idaho",	"Illinois",	"Indiana",	"Iowa",	"Kansas",	"Kentucky",	"Louisiana",	"Maine",	"Maryland",	"Massachusetts",	"Michigan",	"Minnesota",	"Mississippi",	"Missouri",	"Montana",	"Nebraska",	"Nevada",	"New Hampshire",	"New Jersey",	"New Mexico",	"New York",	"North Carolina",	"North Dakota",	"Ohio",	"Oklahoma",	"Oregon",	"Pennsylvania",	"Rhode Island",	"South Carolina",	"South Dakota",	"Tennessee",	"Texas",	"Utah",	"Vermont",	"Virginia",	"Washington",	"West Virginia",	"Wisconsin",	"Wyoming"],
#     "cords": []
# }
#
#
# # get x,y coordinates and add to list of states.
# def get_mouse_click_coor(x, y):
#     coords = (x, y)
#     states_dict["cords"] += coords
#     print(states_dict["cords"])
#     print(states_dict)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

