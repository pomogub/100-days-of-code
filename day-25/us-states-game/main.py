import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')
cartographer = turtle.Turtle()
cartographer.penup()
cartographer.hideturtle()
states = pandas.read_csv('50_states.csv')
correct_guesses = []
missed_states = states.state.tolist()

while len(correct_guesses) < 50:
    if len(correct_guesses) == 0:
        answer = screen.textinput("Guess the State", "What's a state's name?").title()
    else:
        answer = screen.textinput(f"{len(correct_guesses)}/50 States Correct",
                                  "What's another state's name?").title()
    if answer == 'Exit':
        if len(correct_guesses) == 50:
            messagebox.showinfo(title="Congratulations!", message="You got all 50!")
        else:
            for guess in correct_guesses:
                missed_states.remove(guess)
            states_to_study = pandas.DataFrame(missed_states)
            states_to_study.to_csv('states_to_learn.csv')
        break
    if answer in correct_guesses:
        messagebox.showinfo(title="Try again", message="You said that already. Are you ok?")
    elif answer in states['state'].values:
        current_guess = states[states['state'] == answer]
        correct_guesses.append(current_guess.state.item())
        cartographer.goto(current_guess.x.item(), current_guess.y.item())
        cartographer.write(arg=current_guess.state.item(), align='left')
    else:
        if answer == 'Dakota' or answer == 'Carolina':
            messagebox.showinfo(title="Try again", message="Uhh which one? You know there's two right?")
        else:
            messagebox.showinfo(title="Try again", message="That's not a state, idiot")

turtle.mainloop()
