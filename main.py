import turtle
import pandas


score = 0
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:

  screen.title("U.S. States Game")
  answer_state = screen.textinput(title=f"You have {score}/50", prompt="What's another state name?").title()
  if answer_state == "Exit":
    for answer in all_states:
      if answer not in guessed_states:
        
        missed_states.append(answer)
    new_data = pandas.DataFrame(missed_states)
    new_data.to_csv("states_to_learn.csv")
      
    break
  if answer_state in all_states:
    score += 1
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)
    
    

screen.exitonclick

