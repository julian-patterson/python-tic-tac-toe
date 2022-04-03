
#DO NOT DELETE THESE
x = "x"

o = "o"

e = "e"


    
def Start():
    #printing the board
    def boardprinter_l(l_board):
        for n in range(len(l_board)):
            boardprinter(l_board[n], n)

    def boardprinter(board, n):
        print("b{} ".format(n+1), end = "")
        for n in range(1, len(board[0]) + 1):
            print(n, end = " ")
        print()
        count = 0
        for row in board:
            print(['a', 'b', 'c'][count], end= '  ')
            for cell in row:
                print(cell, end=" ")
            count += 1
            print()
    

    def winfinder_l(board_l):
        """returns 'x' if x wins, 'o' if o wins, 'tie' if it's a tie and None if nobody has won yet or it's a tie"""
        def winfinder(board):
            #horizontal win finder
            for row in board:
                if (row[0] == row[1] == row[2]) and row[0]!=e:
                    if row[0] == x:
                        return 'X'
                    else:
                        return 'O'
            #vertical win finder
            for n in range(len(board)):
                if (board[0][n] == board[1][n] == board[2][n]) and board[0][n]!=e:
                    if board[0][n] == x:
                        return 'X'
                    else:
                        return 'O'
            
            #diagonal win finder
            if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and board[1][1]!=e:
                if board[1][1] == x:
                    return 'X'
                else:
                    return 'O' 
            return None
        #horizontal
        n = 0
        for _ in range(3):
            row = board_l[n:n+3]
            if (winfinder(row[0]) == winfinder(row[1]) == winfinder(row[2])) and winfinder(row[0]):
                if winfinder(row[0]) == 'X':
                    return x
                else:
                    return o
            n+=3
        #vertical
        columns = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
        for i in range(3):
            board_column = []
            for j in range(3):
                board_column += [board_l[columns[i][j]]]
            if (winfinder(board_column[0]) == winfinder(board_column[1]) == winfinder(board_column[2])) and winfinder(board_column[0]):
                    if winfinder(board_column[0]) == 'X':
                        return x
                    else:
                        return o
        #diagonal
        diagonals = ((0,4,8), (2, 4, 6))
        for i in range(2): #for diagonals index
            board_diagonal = []
            for j in range(3): #for diagonals deep index
                board_diagonal += [board_l[diagonals[i][j]]]
            if (winfinder(board_diagonal[0]) == winfinder(board_diagonal[1]) == winfinder(board_diagonal[2])) and winfinder(board_diagonal[0]):
                    if winfinder(board_diagonal[0]) == 'X':
                        return x
                    else:
                        return o
        #tiechecker
        e_counter = 0
        for board in board_l:
            for row in board:
                for cell in row:
                    if cell==e:
                        e_counter += 1
        if e_counter == 0:
            return 'tie'

        #if all else fails....
        return None

    #variables
    board = [
        [e, e, e], 
        [e, e, e], 
        [e, e, e],
        ]
    board_l = []
    for _ in range(9): #idk how else to do this
        board_l += [board.copy()]
    player1 = input("Player 1 name (goes first): ")
    player2 = input("Player 2 name: ")
    player_d = {x:player1, o:player2}
    d_abc = {'a':0, 'b':1, 'c':2}
    d_123 = {'1':0, '2':1, '3':2}
    current_board = None
    current_board_index = {
                        (0,0):0, (0,1):1, (0,2):2,
                        (1,0):3, (1,1):4, (1,2):5,
                        (2,0):6, (2,1):7, (2,2):8
                        }
    active = o
    nonactive = x
    retry = False
    firsttime = True

    #game start
    boardprinter_l(board_l)
    if input('Tutorial? y/n ').lower() in ('y', 'yes'):
        print("tutorial example: 'a 2' ")
        print("first move (by X) must include a board number. Example below:\nb1 a 2 ")

    while True:
        if retry == False:
            active, nonactive = nonactive, active
        else:
            retry = False
        if firsttime == True: #i hate myself
            location_initial = input(player1 + ", please enter the location of X: ").split()
            current_board = int(location_initial[0][1:])-1
            location = location_initial[1:]
            location[0], location[1] = d_abc[location[0]], d_123[location[1]]
            print(location)
            board_l[current_board][location[0]][location[1]] = active
            current_board = current_board_index[tuple(location)]
            firsttime = False
        else:
            location = input(player_d[active] + ", please enter the location of {}: ".format(active)).split()
            location[0], location[1] = d_abc[location[0]], d_123[location[1]]
            if board_l[current_board][location[0]][location[1]]!=e:
                print('someone has already gone there!')
                retry = True
                continue
            else:
                board_l[current_board][location[0]][location[1]] = active
                current_board = current_board_index[tuple(location)]


        boardprinter_l(board_l)

        if winfinder_l(board_l):
            if winfinder_l(board_l) == 'tie':
                print('tie between {} and {}'.format(player1, player2))
            print(player_d[winfinder_l(board_l)], 'won!')
            break

Start()

