from tkinter import *
from datetime import datetime, timedelta
import tkinter.messagebox
import random

list_of_words = ['absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon',
                 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful',
                 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness',
                 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex',
                 'dwarves', 'embezzle', 'equip', 'espionage',
                 ]
TITLE_FONT = "Arial"
TITLE = "#00ADB5"
WORD_FONT = "Times New Roman"
WORD = "#F94A29"
APP_BACKGROUND = "#ECF9FF"
RANDOM_WORD = random.choice(list_of_words)
WORDS_TYPED = 0
TIME_TEST = datetime.today() + timedelta(seconds=60)


# Def that change the word
def change_word():
    global RANDOM_WORD
    RANDOM_WORD = random.choice(list_of_words)
    text_entry.delete(0, END)
    word_label.config(text=f"{RANDOM_WORD}")


# Def that verify if you writhe te word correctly
def callback(string_variable):
    global RANDOM_WORD, WORDS_TYPED
    current_letter = (len(string_variable.get()) - 1)
    datetime_now = datetime.today()
    if datetime_now >= TIME_TEST:
        tkinter.messagebox.showinfo("Results", f"Your speed is: {WORDS_TYPED} words per minute.")
    if string_variable.get() == RANDOM_WORD:
        WORDS_TYPED += 1
        change_word()
    elif string_variable.get():
        try:
            if string_variable.get()[current_letter] != RANDOM_WORD[current_letter]:
                word_label.config(text=f"{RANDOM_WORD}", bg="Red")
            else:
                word_label.config(text=f"{RANDOM_WORD}", bg=APP_BACKGROUND)
        except IndexError:
            word_label.config(text=f"{RANDOM_WORD}", bg="Red")


# Creating Windows and Labels with Tkinter

windows = Tk()
windows.title('Typing Speed Test')
windows.config(padx=25, pady=25, bg=APP_BACKGROUND)
windows.geometry("750x500")

# Use place() to complete the User Interface

title_label = Label(text="Typing Speed Test", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=APP_BACKGROUND)
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

word_label = Label(text=f"{RANDOM_WORD}", font=(WORD_FONT, 44), fg=WORD, bg=APP_BACKGROUND)
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Callback to check if you're typing in the right characters
string_variable = StringVar()
string_variable.trace("w", lambda name, index, mode, sv=string_variable: callback(string_variable))

# Dialog Boxes and Pop-Ups in Tkinter
text_entry = Entry(windows, width=25, font=(f"{WORD_FONT}", 24), textvariable=string_variable)
text_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
text_entry.focus()

windows.mainloop()
