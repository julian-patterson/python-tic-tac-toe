from email import message
from termios import B921600
from tkinter import *
from tkinter import messagebox
from tkinter import font
from click import command

count = 0
board = [['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','','']]


def Quit():
    global tk
    tk.destroy()


def destruct():
    global tk, winnerWindow
    tk.destroy()
    winnerWindow.destroy()


def displayWinner(winner):
    global tk, winnerWindow, ID
    winnerWindow=Tk()
    winnerWindow.title('Winner Window')
    winnerWindow.configure(bg='black')
    l1=Label(winnerWindow, text='The winner is: ', bg='black', fg='white')
    l1.pack()
    l2=Label(winnerWindow, text=winner, bg='black', fg='white')
    l2.pack()
    bproceed=Button(winnerWindow, text='proceed', command=destruct)
    bproceed.pack()


def checkWinner():
    global count, board
    if (board[0][0]==board[0][1]==board[0][2]==board[0][3]==board[0][4]==board[0][5]==board[0][6]==board[0][7]==board[0][8]=="X" or 
        board[1][0]==board[1][1]==board[1][2]==board[1][3]==board[1][4]==board[1][5]==board[1][6]==board[1][7]==board[1][8]=="X" or 
        board[2][0]==board[2][1]==board[2][2]==board[2][3]==board[2][4]==board[2][5]==board[2][6]==board[2][7]==board[2][8]=="X" or
        board[3][0]==board[3][1]==board[3][2]==board[3][3]==board[3][4]==board[3][5]==board[3][6]==board[3][7]==board[3][8]=="X" or
        board[4][0]==board[4][1]==board[4][2]==board[4][3]==board[4][4]==board[4][5]==board[4][6]==board[4][7]==board[4][8]=="X" or
        board[5][0]==board[5][1]==board[5][2]==board[5][3]==board[5][4]==board[5][5]==board[5][6]==board[5][7]==board[5][8]=="X" or
        board[6][0]==board[6][1]==board[6][2]==board[6][3]==board[6][4]==board[6][5]==board[6][6]==board[6][7]==board[6][8]=="X" or
        board[7][0]==board[7][1]==board[7][2]==board[7][3]==board[7][4]==board[7][5]==board[7][6]==board[7][7]==board[7][8]=="X" or
        board[8][0]==board[8][1]==board[8][2]==board[8][3]==board[8][4]==board[8][5]==board[8][6]==board[8][7]==board[8][8]=="X" or
        board[0][0]==board[1][0]==board[2][0]==board[3][0]==board[4][0]==board[5][0]==board[6][0]==board[7][0]==board[8][0]=="X" or 
        board[0][1]==board[1][1]==board[2][1]==board[3][1]==board[4][1]==board[5][1]==board[6][1]==board[7][1]==board[8][1]=="X" or 
        board[0][2]==board[1][2]==board[2][2]==board[3][2]==board[4][2]==board[5][2]==board[6][2]==board[7][2]==board[8][2]=="X" or
        board[0][3]==board[1][3]==board[2][3]==board[3][3]==board[4][3]==board[5][3]==board[6][3]==board[7][3]==board[8][3]=="X" or
        board[0][4]==board[1][4]==board[2][4]==board[3][4]==board[4][4]==board[5][4]==board[6][4]==board[7][4]==board[8][4]=="X" or
        board[0][5]==board[1][5]==board[2][5]==board[3][5]==board[4][5]==board[5][5]==board[6][5]==board[7][5]==board[8][5]=="X" or
        board[0][6]==board[1][6]==board[2][6]==board[3][6]==board[4][6]==board[5][6]==board[6][6]==board[7][6]==board[8][6]=="X" or
        board[0][7]==board[1][7]==board[2][7]==board[3][7]==board[4][7]==board[5][7]==board[6][7]==board[7][7]==board[8][7]=="X" or
        board[0][8]==board[1][8]==board[2][8]==board[3][8]==board[4][8]==board[5][8]==board[6][8]==board[7][8]==board[8][8]=="X" or
        board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]==board[5][5]==board[6][6]==board[7][7]==board[8][0]=="X"):
        displayWinner('Player X')
    if (board[0][0]==board[0][1]==board[0][2]==board[0][3]==board[0][4]==board[0][5]==board[0][6]==board[0][7]==board[0][8]=="O" or 
        board[1][0]==board[1][1]==board[1][2]==board[1][3]==board[1][4]==board[1][5]==board[1][6]==board[1][7]==board[1][8]=="O" or 
        board[2][0]==board[2][1]==board[2][2]==board[2][3]==board[2][4]==board[2][5]==board[2][6]==board[2][7]==board[2][8]=="O" or
        board[3][0]==board[3][1]==board[3][2]==board[3][3]==board[3][4]==board[3][5]==board[3][6]==board[3][7]==board[3][8]=="O" or
        board[4][0]==board[4][1]==board[4][2]==board[4][3]==board[4][4]==board[4][5]==board[4][6]==board[4][7]==board[4][8]=="O" or
        board[5][0]==board[5][1]==board[5][2]==board[5][3]==board[5][4]==board[5][5]==board[5][6]==board[5][7]==board[5][8]=="O" or
        board[6][0]==board[6][1]==board[6][2]==board[6][3]==board[6][4]==board[6][5]==board[6][6]==board[6][7]==board[6][8]=="O" or
        board[7][0]==board[7][1]==board[7][2]==board[7][3]==board[7][4]==board[7][5]==board[7][6]==board[7][7]==board[7][8]=="O" or
        board[8][0]==board[8][1]==board[8][2]==board[8][3]==board[8][4]==board[8][5]==board[8][6]==board[8][7]==board[8][8]=="O" or
        board[0][0]==board[1][0]==board[2][0]==board[3][0]==board[4][0]==board[5][0]==board[6][0]==board[7][0]==board[8][0]=="O" or 
        board[0][1]==board[1][1]==board[2][1]==board[3][1]==board[4][1]==board[5][1]==board[6][1]==board[7][1]==board[8][1]=="O" or 
        board[0][2]==board[1][2]==board[2][2]==board[3][2]==board[4][2]==board[5][2]==board[6][2]==board[7][2]==board[8][2]=="O" or
        board[0][3]==board[1][3]==board[2][3]==board[3][3]==board[4][3]==board[5][3]==board[6][3]==board[7][3]==board[8][3]=="O" or
        board[0][4]==board[1][4]==board[2][4]==board[3][4]==board[4][4]==board[5][4]==board[6][4]==board[7][4]==board[8][4]=="O" or
        board[0][5]==board[1][5]==board[2][5]==board[3][5]==board[4][5]==board[5][5]==board[6][5]==board[7][5]==board[8][5]=="O" or
        board[0][6]==board[1][6]==board[2][6]==board[3][6]==board[4][6]==board[5][6]==board[6][6]==board[7][6]==board[8][6]=="O" or
        board[0][7]==board[1][7]==board[2][7]==board[3][7]==board[4][7]==board[5][7]==board[6][7]==board[7][7]==board[8][7]=="O" or
        board[0][8]==board[1][8]==board[2][8]==board[3][8]==board[4][8]==board[5][8]==board[6][8]==board[7][8]==board[8][8]=="O" or
        board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]==board[5][5]==board[6][6]==board[7][7]==board[8][0]=="O"):
        displayWinner('Player O')
    else:
        displayWinner('It is a tie')


def changeVal(button, row, column):
    global count
    if button['text'] == '':
        if count%2==0:
            button['text'] = 'X'
            l1=Label(tk, text='Player: 2(0)', height=3, bg='white').grid(row=0, column=0)
            board[row][column]= 'X'
        else:
            button['text'] = 'O'
            l1=Label(tk, text='Player: 1(X)', height=3, bg='white').grid(row=0, column=0)
            board[row][column] = 'O'
        count = count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror('Unable to place value')
        


def boardgui():
    global tk
    tk=Tk()
    tk.title('Tic Tac Toe Game')
    tk.configure(bg="white")
    l1=Label(tk, text= "Player: 1 (X)", height=3, bg='white')
    l1.grid(row=0, column=0)
    quitbutton = Button(tk, text='Exit', command= quit)
    quitbutton.grid(row=0,column=2)

    #first row
    b1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1, 0,0))
    b2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2, 0,1))
    b3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3, 0,2))
    b4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4, 0,3))
    b5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5, 0,4))
    b6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6, 0,5))
    b7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7, 0,6))
    b8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8, 0,7))
    b9 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9, 0,8))
    #grid
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)
    b4.grid(row=2, column=3)
    b5.grid(row=2, column=4)
    b6.grid(row=2, column=5)
    b7.grid(row=2, column=6)
    b8.grid(row=2, column=7)
    b9.grid(row=2, column=8)


    #second row
    b1_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_1, 1,0))
    b2_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_1, 1,1))
    b3_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_1, 1,2))
    b4_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_1, 1,3))
    b5_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_1, 1,4))
    b6_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_1, 1,5))
    b7_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_1, 1,6))
    b8_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_1, 1,7))
    b9_1 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_1, 1,8))
    #grid
    b1_1.grid(row=3, column=0)
    b2_1.grid(row=3, column=1)
    b3_1.grid(row=3, column=2)
    b4_1.grid(row=3, column=3)
    b5_1.grid(row=3, column=4)
    b6_1.grid(row=3, column=5)
    b7_1.grid(row=3, column=6)
    b8_1.grid(row=3, column=7)
    b9_1.grid(row=3, column=8)


    #third row
    b1_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_2, 2,0))
    b2_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_2, 2,1))
    b3_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_2, 2,2))
    b4_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_2, 2,3))
    b5_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_2, 2,4))
    b6_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_2, 2,5))
    b7_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_2, 2,6))
    b8_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_2, 2,7))
    b9_2 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_2, 2,8))
    #grid
    b1_2.grid(row=4, column=0)
    b2_2.grid(row=4, column=1)
    b3_2.grid(row=4, column=2)
    b4_2.grid(row=4, column=3)
    b5_2.grid(row=4, column=4)
    b6_2.grid(row=4, column=5)
    b7_2.grid(row=4, column=6)
    b8_2.grid(row=4, column=7)
    b9_2.grid(row=4, column=8)


    #four row
    b1_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_3, 3,0))
    b2_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_3, 3,1))
    b3_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_3, 3,2))
    b4_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_3, 3,3))
    b5_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_3, 3,4))
    b6_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_3, 3,5))
    b7_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_3, 3,6))
    b8_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_3, 3,7))
    b9_3 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_3, 3,8))
    #grid
    b1_3.grid(row=5, column=0)
    b2_3.grid(row=5, column=1)
    b3_3.grid(row=5, column=2)
    b4_3.grid(row=5, column=3)
    b5_3.grid(row=5, column=4)
    b6_3.grid(row=5, column=5)
    b7_3.grid(row=5, column=6)
    b8_3.grid(row=5, column=7)
    b9_3.grid(row=5, column=8)


    #fifth row
    b1_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_4, 4,0))
    b2_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_4, 4,1))
    b3_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_4, 4,2))
    b4_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_4, 4,3))
    b5_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_4, 4,4))
    b6_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_4, 4,5))
    b7_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_4, 4,6))
    b8_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_4, 4,7))
    b9_4 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_4, 4,8))
    #grid
    b1_4.grid(row=6, column=0)
    b2_4.grid(row=6, column=1)
    b3_4.grid(row=6, column=2)
    b4_4.grid(row=6, column=3)
    b5_4.grid(row=6, column=4)
    b6_4.grid(row=6, column=5)
    b7_4.grid(row=6, column=6)
    b8_4.grid(row=6, column=7)
    b9_4.grid(row=6, column=8)


    #sixth row
    b1_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_5, 5,0))
    b2_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_5, 5,1))
    b3_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_5, 5,2))
    b4_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_5, 5,3))
    b5_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_5, 5,4))
    b6_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_5, 5,5))
    b7_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_5, 5,6))
    b8_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_5, 5,7))
    b9_5 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_5, 5,8))
    #grid
    b1_5.grid(row=7, column=0)
    b2_5.grid(row=7, column=1)
    b3_5.grid(row=7, column=2)
    b4_5.grid(row=7, column=3)
    b5_5.grid(row=7, column=4)
    b6_5.grid(row=7, column=5)
    b7_5.grid(row=7, column=6)
    b8_5.grid(row=7, column=7)
    b9_5.grid(row=7, column=8)


    #seventh row
    b1_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_6, 6,0))
    b2_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_6, 6,1))
    b3_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_6, 6,2))
    b4_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_6, 6,3))
    b5_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_6, 6,4))
    b6_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_6, 6,5))
    b7_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_6, 6,6))
    b8_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_6, 6,7))
    b9_6 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_6, 6,8))
    #grid
    b1_6.grid(row=8, column=0)
    b2_6.grid(row=8, column=1)
    b3_6.grid(row=8, column=2)
    b4_6.grid(row=8, column=3)
    b5_6.grid(row=8, column=4)
    b6_6.grid(row=8, column=5)
    b7_6.grid(row=8, column=6)
    b8_6.grid(row=8, column=7)
    b9_6.grid(row=8, column=8)


    #eighth row
    b1_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_7, 7,0))
    b2_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_7, 7,1))
    b3_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_7, 7,2))
    b4_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_7, 7,3))
    b5_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_7, 7,4))
    b6_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_7, 7,5))
    b7_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_7, 7,6))
    b8_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_7, 7,7))
    b9_7 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_7, 7,8))
    #grid
    b1_7.grid(row=9, column=0)
    b2_7.grid(row=9, column=1)
    b3_7.grid(row=9, column=2)
    b4_7.grid(row=9, column=3)
    b5_7.grid(row=9, column=4)
    b6_7.grid(row=9, column=5)
    b7_7.grid(row=9, column=6)
    b8_7.grid(row=9, column=7)
    b9_7.grid(row=9, column=8)


    #ninth row
    b1_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b1_8, 8,0))
    b2_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b2_8, 8,1))
    b3_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b3_8, 8,2))
    b4_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b4_8, 8,3))
    b5_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b5_8, 8,4))
    b6_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b6_8, 8,5))
    b7_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b7_8, 8,6))
    b8_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b8_8, 8,7))
    b9_8 = Button(tk, text='',height=4, width=8, bg='black', activebackground= 'white', fg='white', command=lambda: changeVal(b9_8, 8,8))
    #grid
    b1_8.grid(row= 10, column=0)
    b2_8.grid(row=10, column=1)
    b3_8.grid(row=10, column=2)
    b4_8.grid(row=10, column=3)
    b5_8.grid(row=10, column=4)
    b6_8.grid(row=10, column=5)
    b7_8.grid(row=10, column=6)
    b8_8.grid(row=10, column=7)
    b9_8.grid(row=10, column=8)

boardgui()