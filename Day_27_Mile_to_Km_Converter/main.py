from tkinter import *


def button_cliched():
    mile_to_km = int(input_mile.get())*1.609
    result_label.config(text=f"{round(mile_to_km, 2)}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=10)

mile_label = Label(text="Mile")
mile_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1)

input_mile = Entry(width=10)
input_mile.grid(column=1, row=0)

button = Button(text="Calculate", command=button_cliched)
button.grid(column=1, row=2)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

window.mainloop()
