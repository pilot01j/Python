from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # copy using only a clic
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_simbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_simbols + password_numbers + password_letters
    shuffle(password_list)  # mix characters in password list
    password = "".join(password_list)  # create a string using characters from password list
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="ERROR", message="You net to complete all rows.")
    else:
        try:
            with open("date.json", "r") as data_file:
                # Read old data json file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("date.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data json file
            data.update(new_data)

            with open("date.json", "w") as data_file:
                # Saving updated data json file
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)  # delete date from Entries
            password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("date.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
window_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=window_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Login:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1)
website_entry.focus()  # hire will start
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pilot01j@gmail.com")
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_new_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
