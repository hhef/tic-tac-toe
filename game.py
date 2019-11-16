board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"


def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" +
          board[3] + " | " + board[4] + " | " + board[5] + "\n" +
          board[6] + " | " + board[7] + " | " + board[8] + "\n")


show_board()


def switch_players():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# game
# players turns
# check winner
# check board
# check if tie
