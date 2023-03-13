from tkinter import *
from tkinter import messagebox

# Creating Windows and Labels with Tkinter
root = Tk()
root.title('Tic Tac Toe')

clicked = True
count = 0


# Def that disable all buttons when the winner exist:

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Def that color in green the winner buttons and send a message about winner:

def green_winners(winner_bt_1, winner_bt_2, winner_bt_3):
    winner_bt_1.config(bg="green")
    winner_bt_2.config(bg="green")
    winner_bt_3.config(bg="green")
    if winner_bt_1['text'] == "X":
        messagebox.showinfo("Tic Tac Toe", "The winner is: X")
    elif winner_bt_1['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe", "The winner is: O")

    disable_all_buttons()


# Def that verify the if winner exist:

def if_winner():
    global winner
    winner = False
    if b1['text'] == "X" and b2['text'] == 'X' and b3['text'] == 'X' \
            or b1['text'] == "O" and b2['text'] == 'O' and b3['text'] == 'O':
        green_winners(b1, b2, b3)
        winner = True

    elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X' \
            or b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
        green_winners(b4, b5, b6)
        winner = True

    elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X' \
            or b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O':
        green_winners(b7, b8, b9)
        winner = True

    elif b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == 'X' \
            or b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == 'O':
        green_winners(b1, b4, b7)
        winner = True

    elif b2['text'] == "X" and b5['text'] == 'X' and b8['text'] == 'X' \
            or b2['text'] == "O" and b5['text'] == 'O' and b8['text'] == 'O':
        green_winners(b2, b5, b8)
        winner = True

    elif b3['text'] == "X" and b6['text'] == 'X' and b9['text'] == 'X' \
            or b3['text'] == "O" and b6['text'] == 'O' and b9['text'] == 'O':
        green_winners(b3, b6, b9)
        winner = True

    elif b1['text'] == "X" and b5['text'] == 'X' and b9['text'] == 'X' \
            or b1['text'] == "O" and b5['text'] == 'O' and b9['text'] == 'O':
        green_winners(b1, b5, b9)
        winner = True

    elif b3['text'] == "X" and b5['text'] == 'X' and b7['text'] == 'X' \
            or b3['text'] == "O" and b5['text'] == 'O' and b7['text'] == 'O':
        green_winners(b3, b5, b7)
        winner = True

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disable_all_buttons()


def b_click(b):
    global clicked, count

    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        if_winner()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        if_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "Please select a blank box")


# Use grid() and columnspan to Complete the User Interface

def play_again():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # Buttons:
    b1 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 30), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))

    # Button grid assign:

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# Game Menu:

game_menu = Menu(root)
root.config(menu=game_menu)

options_menu = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Restart Game", command=play_again)

play_again()
root.mainloop()
