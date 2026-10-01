from tkinter import *
import math
# ---------------------------- CONSTANTS/VARIABLES ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    title_label.config(text="Timer")
    sessions.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps in (1, 3, 5, 7):  # else
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    elif reps in (2, 4, 6):  # if count_down % 2(run before long break)
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    elif reps == 8:  # if count_down % 8
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checks += "✔"
        sessions.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# window.after(1000, say_something, 3, 5, 8)

title_label = Label(text="Timer", font=(FONT_NAME, 42, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

sessions = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
sessions.grid(column=1, row=3)


window.mainloop()
