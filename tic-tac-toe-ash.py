

x = "x"

o = "o"

e = "e"


    
def Start():
    #printing the board
    def boardprinter(board):
        print("   ", end = "")
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
        
    #variables
    board = [
        [e, e, e], 
        [e, e, e], 
        [e, e, e],
        ]
    player1 = input("Player 1 name (goes first): ")
    player2 = input("Player 2 name: ")
    player_d = {'X':player1, 'O':player2}
    d_abc = {'a':0, 'b':1, 'c':2}
    d_123 = {'1':0, '2':1, '3':2}
    #game start
    boardprinter(board)
    print("tutorial example: 'a 2' ")
    while True:
        
        #player 1 turn
        location = input(player1 + ", please enter the location of X: ")
        location = location.split()
        location[0] = d_abc[location[0]]
        location[1] = d_123[location[1]]
        board[location[0]][location[1]] = x
        boardprinter(board)
        #player 2 turn
        location = input(player2 + ", please enter the location of O: ")
        location = location.split() #['a', '1']
        location[0] = d_abc[location[0]] #['0', '1']
        location[1] = d_123[location[1]] # ['0', '0']
        board[location[0]][location[1]] = o
        boardprinter(board)

        iswin = winfinder(board)
        if iswin:
            print(player_d[iswin], 'won!')
            break

            
Start()

