board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
game_on = True
winner = None


def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" +
          board[3] + " | " + board[4] + " | " + board[5] + "\n" +
          board[6] + " | " + board[7] + " | " + board[8] + "\n")


def insert_letter(letter, position):
    board[position] = letter


def empty_space(position):
    return board[position] == "-"


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
    global game_on
    if board.count("-") < 1:
        game_on = False


def check_if_win():
    global winner
    row_winner = check_rows()
    columns_winner = check_columns()
    across_winner = check_across()
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif across_winner:
        winner = across_winner


def check_rows():
    global game_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_on = False
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]


def check_columns():
    global game_on
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_on = False
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]


def check_across():
    global game_on
    across_1 = board[0] == board[4] == board[8] != "-"
    across_2 = board[2] == board[4] == board[6] != "-"
    if across_1 or across_2:
        game_on = False
        if across_1:
            return board[0]
        if across_2:
            return board[2]


def player_turn(player):
    position = input(f"Please '{player}' pick position 1-9: ")
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invalid input, pick position 1-9: ")
        position = int(position) - 1
        if empty_space(position):
            valid = True
        else:
            position = input("Space already taken, pick position 1-9: ")
    insert_letter(player, position)
    show_board()


def game():
    show_board()
    print("Welcome to Tic Tac Toe. X starts")
    while game_on:
        player_turn(current_player)
        check_if_win_or_tie()
        switch_players()
    if winner is None:
        print("It's a tie")
    else:
        print(f"Congratulations {winner}, you won")


game()
