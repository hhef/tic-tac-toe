board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"


def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" +
          board[3] + " | " + board[4] + " | " + board[5] + "\n" +
          board[6] + " | " + board[7] + " | " + board[8] + "\n")


def insert_letter(letter, position):
    board[position] = letter


def switch_players():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_if_win_or_tie():
    pass


def game():
    show_board()
    print("Welcome to Tic Tac Toe. X starts")
    position = input(f"Please {current_player} pick position 1-9: ")
    insert_letter(current_player, position)

    # check if win or tie
    switch_players()
