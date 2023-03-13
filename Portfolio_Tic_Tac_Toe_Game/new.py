board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
game = True


def print_board():
    print(f" {board[0]} |  {board[1]}  | {board[2]} ")
    print("---|-----|---")
    print(f" {board[3]} |  {board[4]}  | {board[5]} ")
    print("---|-----|---")
    print(f" {board[6]} |  {board[7]}  | {board[8]} ")


def player_input():
    input_x = int(input("Enter a number in range 1 and 9: "))
    if board[input_x - 1] == "-":
        board[input_x - 1] = current_player
    else:
        print("This section is unplaceable")


def check_horizontle():
    global winner

    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_row():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def check_diag():
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def check_if_win():
    global game
    if check_horizontle():
        print_board()
        print(f"The winner is {winner}!")
        game = False

    elif check_row():
        print_board()
        print(f"The winner is {winner}!")
        game = False

    elif check_diag():
        print_board()
        print(f"The winner is {winner}!")
        game = False


def game_tie():
    global game
    if "-" not in board:
        print_board()
        print("Tie ! ")
        game = False


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


if __name__ == '__main__':
    while game:
        print_board()
        player_input()
        check_if_win()
        game_tie()
        switch_player()