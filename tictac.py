
from tkinter import *
import random

root = Tk()

def onClick(i,j):
    button = board[i][j]
    if button['text']!="":
        return
    button['text'] = "X"

    if checkWin(): return

    if Tie(): return
    unchecked=[]

    for i in range(3):
        for j in range(3):
            if board[i][j]['text']=="":
                unchecked.append((i,j))

    r,c = random.choice(unchecked)
    board[r][c]['text'] = "O"

    if checkWin(): return 

def Tie():
    for i in range(3):
        for j in range(3):
            if board[i][j]['text']=="":
                return False
    message="tie"
    display_message(message)
    disable_board()
    return True

def checkWin():
    result = None
    for row in range(3):
        if board[row][0]['text']==board[row][1]['text']==board[row][2]['text']!="":
            result = board[row][0]['text']
    
    for col in range(3):
        if board[0][col]['text']==board[1][col]['text']==board[2][col]['text']!="":
            result = board[0][col]['text']
          
    if board[0][0]['text']==board[1][1]['text']==board[2][2]['text']!="":
        result = board[0][0]['text']
        

    if board[0][2]['text']==board[1][1]['text']==board[2][0]['text']!="":
        result = board[0][2]['text']
     
    
    if result:
        if result=="X":
            message="You Won"
            display_message(message)
        else:
            message="Computer Won"
            display_message(message)
        disable_board()
        return True
    else:
        return False
    
    
def disable_board():
    for i in range(3):
        for j in range(3):
            board[i][j]['state'] = 'disabled' 

def display_message(message):
    new_win = Toplevel(root)
    new_win.geometry("200x150")
    display_label = Label(new_win, text=message, fg="red", font=("Helvetica", 15, "bold"))
    display_label.pack(expand=True)

board = []

for i in range(3):
    row = []
    for j in range(3):
        new_button = Button(root, text="", width=10, height=5, font=("Helvetica", 15, "bold"), bg="pink", command=lambda row=i, column = j: onClick(row,column))
        new_button.grid(row=i,column=j)
        row.append(new_button)
    board.append(row)

root.mainloop()