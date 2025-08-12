from tkinter import *
import random

turn = "X"
computer_turn = "O"


def onClick(i,j):
    button = board[i][j]
    if button['text']!="":
        return
    button['text'] = turn

    if checkWin():
        return
    
    if Tie(): return

    choices = []
    for i in range(3):
            for j in range(3):
                if board[i][j]['text']=="": choices.append((i,j))

    row, col = random.choice(choices)

    board[row][col]["text"] = computer_turn

    if checkWin():
        return
    


def Tie():
    for i in range(3):
        for j in range(3):
            if board[i][j]['text']=="":
                return False
    print("Tie") 
    disable_board()
    return True

    

def checkWin():

    result = None
    for j in range(3):
        if board[0][j]['text']== board[1][j]['text']==board[2][j]['text']!="":
            result = board[0][j]['text']
    for i in range(3):
        if board[i][0]['text']==board[i][1]['text']==board[i][2]['text']!="":
            result= board[i][0]['text']
    if board[0][0]['text']==board[1][1]['text']==board[2][2]['text']!="":
        result = board[0][0]['text']
    if board[0][2]['text']==board[1][1]['text']==board[2][0]['text']!="":
        result= board[0][2]['text']

    if result=="X":
        message = "You won"
        print(message)
        DisplayWinMessage(message)
        disable_board()
        return True
    elif result=="O":
        message = "Computer Won"
        print(message)
        DisplayWinMessage(message)
        disable_board()
        return True
    else:
        return False
    
def disable_board():
    for i in range(3):
        for j in range(3):
            board[i][j]['state'] = "disabled"


def DisplayWinMessage(message):
    # Create a Toplevel window
    win_window = Toplevel(root)
    win_window.title("Game Over")
    
    # Configure the window size (optional)
    win_window.geometry("300x150")
    
    # Create a Label to display the win message
    win_label = Label(win_window, text=message, font=("Helvetica", 20, "bold"), fg="red", bg="white")
    win_label.pack(expand=True)  # Center the label in the window
    
    # Add a button to close the Toplevel window
    close_button = Button(win_window, text="Close", command=win_window.destroy)
    close_button.pack()

    
root = Tk()
root.config(bg="pink")

board = []

for i in range(3):
    row = []
    for j in range(3):
        new_button = Button(root, text="",width=10, height=5, bg="pink", command= lambda row=i, column=j: onClick(row,column), font=("helvetica", 15, "bold"))
        new_button.grid(row=i,column=j)
        row.append(new_button)
    board.append(row)

root.mainloop()