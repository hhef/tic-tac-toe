board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
win_combination = [(board[0] == board[1] == board[2]),  # first row
                   (board[3] == board[4] == board[5]),  # second row
                   (board[6] == board[7] == board[8]),  # third row
                   (board[0] == board[3] == board[6]),  # first column
                   (board[1] == board[4] == board[7]),  # second column
                   (board[2] == board[5] == board[8]),  # third column
                   (board[0] == board[4] == board[8]),  # first across
                   (board[2] == board[4] == board[6])]  # second across


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
    check_if_tie()
    check_if_win()


def check_if_tie():
    if board.count("-") < 1:
        return True


def check_if_win():
    check_rows()
    check_columns()
    check_across()


def check_rows():
    if win_combination[0] or win_combination[1] or win_combination[2]:
        if win_combination[0]:
            return board[0]
        elif win_combination[1]:
            return board[3]
        elif win_combination[2]:
            return board[6]


def check_columns():
    if win_combination[3] or win_combination[4] or win_combination[5]:
        if win_combination[3]:
            return board[0]
        elif win_combination[4]:
            return board[1]
        elif win_combination[5]:
            return board[2]


def check_across():
    if win_combination[6] or win_combination[7]:
        if win_combination[6]:
            return board[0]
        if win_combination[7]:
            return board[2]


def game():
    while True:
        show_board()
        print("Welcome to Tic Tac Toe. X starts")
        position = input(f"Please {current_player} pick position 1-9: ")
        insert_letter(current_player, int(position))

        # check if win or tie
        switch_players()


game()