# Ultimate Tic-Tac-Toe game
# initial version

board = []

for i in range(9):
    mini_board = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]
    board.append(mini_board)

# Circles are denoted as 1, crosses as 2

while True:
    move_type = input("Enter 1 to play as circles, or 2 to play as crosses: ")
    try:
        int(move_type)
        if int(move_type) == 1 or int(move_type) == 2:
            move_type = int(move_type)
            break
    except ValueError:
        continue

if move_type == 1:
    opponent_move_type = 2
else:
    opponent_move_type = 1


number_of_moves = 0


def move(init_board, board_n):
    while True:
        n = int(input("Move number(0 to 8): "))
        if init_board[board_n][n] == 0:
            return n


board_num = int(input("Board number(0 to 8): ")) # first move
move_num_2 = move(board, board_num)
board[board_num][move_num_2] = move_type
number_of_moves += 1
move_num_1 = 0


# for loop used for debug only, later you can change it to a while loop until someone wins or there is a tie
for i in range(4):
    if number_of_moves % 2 == 1:  # if odd, i.e. if it's your turn
        while True:
            move_num_1 = move(board, move_num_2)
            if board[move_num_2][move_num_1] == 0:
                break
        board[move_num_2][move_num_1] = move_type
        number_of_moves += 1
    elif number_of_moves % 2 == 0:  # if even, i.e. if it's you opponent's turn
        while True:
            move_num_2 = move(board, move_num_1)
            if board[move_num_1][move_num_2] == 0:
                break
        board[move_num_1][move_num_2] = opponent_move_type
        number_of_moves += 1

for i in range(9):
    print(board[i])
