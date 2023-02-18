import random
from tkinter import *
from random import randint, choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---------------------------- Read CSV file ------------------------------- #
try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/romanian_words_file.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # transform csv in dictionary


# ---------------------------- DEF ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Romanian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Romanian"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

# Flash Cards

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(highlightthickness=0, image=wrong_image, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
