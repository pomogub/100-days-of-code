from tkinter import *
from pandas import DataFrame, read_csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    wordbank_csv = read_csv('data/words_to_learn.csv')  # noqa
except FileNotFoundError:
    wordbank_csv = read_csv('data/french_words.csv')  # noqa

wordbank = wordbank_csv.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(wordbank)
    canvas.itemconfigure(language_text, text="French", fill='black')
    canvas.itemconfigure(word_text, text=current_card['French'], fill='black')
    canvas.itemconfigure(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card) # noqa


def flip_card():
    canvas.itemconfigure(language_text, text="English", fill='white')
    canvas.itemconfigure(word_text, text=current_card['English'], fill='white')
    canvas.itemconfigure(card_background, image=card_back)


def word_learned():
    wordbank.remove(current_card)
    update_words = DataFrame(wordbank)
    update_words.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) # noqa

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0, bd=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, command=word_learned, highlightthickness=0, bd=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
