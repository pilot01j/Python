from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from tika import parser
import os

TITLE_FONT = "Arial"
TITLE_COLOR = "#362FD9"
WORD_FONT = "Times New Roman"
WORD_COLOR = "#181823"
BACKGROUND_COLOR = "#FCFFE7"
BTN_BACKGROUND_COLOR = "#579BB1"
LANGUAGE = "ro"


def open_pdf():
    # Use tkinter filedialog to select a PDF file
    pdf_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select PDF",
        filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
    )
    raw = parser.from_file(pdf_file)
    raw_content = raw['content']
    print(raw_content)
    # Use gTTS to convert text to speech
    tts = gTTS(text=raw_content, lang=LANGUAGE)
    tts.save('pdf-audio.mp3')
    play_btn.config(fg=TITLE_COLOR)


def play_audio():
    os.startfile('pdf-audio.mp3')

# Creating Windows and Labels with Tkinter
root = Tk()
root.title('Text to Speech')
root.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
title_label = Label(text="Text to Speech", font=(TITLE_FONT, 54, "bold"), fg=TITLE_COLOR, bg=BACKGROUND_COLOR)

# Use grid() to complete the User Interface
title_label.grid(column=0, row=0, pady=40)
open_btn = Button(text="Select PDF", font=(WORD_FONT, 35), width=15, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=open_pdf)
play_btn = Button(text="Play Audio", font=(WORD_FONT, 35), width=15, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=play_audio)
open_btn.grid(column=0, row=1, pady=5)
play_btn.grid(column=0, row=2, pady=5)
root.mainloop()
