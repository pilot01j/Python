from tkinter import *


def button_clicked(*args):
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Fereastra
window = Tk()
window.title("My First GUI Program.")  # denumirea
window.minsize(width=500, height=300)  # marimea
window.config(padx=20, pady=20)#lasam putin loc prin parti

# Label - text in fereastra
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))  # scriim ceva in fereastra
my_label.config(text="New Text")#modificam texul
#my_label.pack(side="left")  # autorizam si setam locul in fereastra
#my_label.place(x=0, y=0)#setam locul in fereastra
my_label.grid(column=0, row=0)#Setem locul impar.fer. intr-o grila
my_label.config(padx=20, pady=20)#facem loc prin parti
# Button
button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry - o fereastra unde putem scri ceva
input = Entry(width=10)
input.grid(column=3, row=3)



window.mainloop()
