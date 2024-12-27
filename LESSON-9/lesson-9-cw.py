from tkinter import *
import random

turn = "X"
mode = "Computer"

def startGame(type):
    global mode
    mode = type
    mode_frame.destroy()
    board_frame.pack()


def DisplayWinMessage(message):
    win_label = Label(root, text=message, font=("Helvetica", 20, "bold"), fg="red", bg="white")
    win_label.place(relx=0.5, rely=0.5, anchor="center")

def onClick(row, column):
    global turn
    # first mark
    if board[row][column]['text'] != "": return 
    if mode=="Multi Player": turn = "O" if turn=="X" else "X"
    board[row][column]['text'] = turn
    unchecked = []

    # check if you won
    result = CheckWin()
    if result:
        if result=="X":
            DisplayWinMessage("You Won")
        else:
            if mode=="Multi Player":
                DisplayWinMessage("Player 2 Won")
        return 
    
    # if you didn't win check if its a tie
    if BoardFill():
        DisplayWinMessage("Tie")
        # print("Tie")
        return 
    
    # if not a tie we want computer to mark his turn
    if mode=="Single Player":
        for i in range(3):
            for j in range(3):
                if board[i][j]['text']=="": unchecked.append((i,j))
        
        r, c = random.choice(unchecked)
        board[r][c]['text']= "O"

        # check if computer won

        if CheckWin(): 
            DisplayWinMessage("Computer Won")
            return

        
    

def CheckWin():
    j=0
    for i in range(3):
        if board[i][j]['text']==board[i][j+1]['text']==board[i][j+2]['text']!="":
            DisableGame() 
            return board[i][j]['text']
    
    i=0
    for j in range(3):
        if board[i][j]['text']==board[i+1][j]['text']==board[i+2][j]['text'] !="":
            DisableGame()
            return board[i][j]['text']
    
    if board[0][0]['text']==board[1][1]['text']==board[2][2]['text']!="":
        DisableGame()
        return board[i][j]['text']

    if board[0][2]['text']==board[1][1]['text']==board[2][0]['text']!="":
        DisableGame()
        return board[i][j]['text']

    return False

def BoardFill():
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == "": return False
    DisableGame()
    return True

def DisableGame():
    for i in range(3):
            for j in range(3):
                board[i][j]['state'] = "disabled"
root = Tk()

mode_frame = Frame(root)
mode_frame.pack()

single_player = Button(mode_frame, text="Single Player", command=lambda: startGame("Single Player"))
multi_player = Button(mode_frame, text="Multi Player", command=lambda: startGame("Multi Player"))

single_player.pack()
multi_player.pack()

board_frame = Frame(root, bg="pink")

board = []

for i in range(3):
    row =[]
    for j in range(3):
        button = Button(board_frame, text="", width=10, height=5, font=("Helvetica", 15, "bold"), command=lambda row=i, column=j: onClick(row,column), bg="pink", fg="blue")
        button.grid(row=i,column=j)
        row.append(button)
    board.append(row)




root.mainloop()

from tkinter import *
import random

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
MODE_SINGLE = "Single Player"
MODE_MULTI = "Multi Player"

# Game State
turn = PLAYER_X
mode = MODE_SINGLE


def start_game(game_mode):
    global mode
    mode = game_mode
    mode_frame.destroy()
    board_frame.pack()


def display_win_message(message):
    win_label = Label(root, text=message, font=("Helvetica", 20, "bold"), fg="red", bg="white")
    win_label.place(relx=0.5, rely=0.5, anchor="center")


def on_click(row, column):
    global turn

    if board[row][column]['text'] != "":
        return

    board[row][column]['text'] = turn

    if mode == MODE_MULTI:
        turn_toggle()

    if check_win():
        display_win_message(f"{turn} Won")
        return

    if board_fill():
        display_win_message("Tie")
        return

    if mode == MODE_SINGLE and turn == PLAYER_X:
        computer_move()


def turn_toggle():
    global turn
    turn = PLAYER_O if turn == PLAYER_X else PLAYER_X


def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j]['text'] == ""]
    row, col = random.choice(empty_cells)
    board[row][col]['text'] = PLAYER_O

    if check_win():
        display_win_message("Computer Won")


def check_win():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text']!="":
            disable_game()
            return True
    for j in range(3):
        if board[0][j]['text']==board[1][j]['text']==board[2][j]['text']!="": 
            disable_game()
            return True

    if all(board[i][i]['text'] == turn for i in range(3)):
        disable_game()
        return True
    if board[0][2]['text']==board[1][1]['text']==board[2][0]['text']!="":
        disable_game()
        return True

    return False


def board_fill():
    if all(board[i][j]['text'] != "" for i in range(3) for j in range(3)):
        disable_game()
        return True
    return False


def disable_game():
    for row in board:
        for button in row:
            button['state'] = "disabled"


# GUI Initialization
root = Tk()
root.title("Tic Tac Toe")

mode_frame = Frame(root)
mode_frame.pack()

Button(mode_frame, text="Single Player", command=lambda: start_game(MODE_SINGLE)).pack()
Button(mode_frame, text="Multi Player", command=lambda: start_game(MODE_MULTI)).pack()

board_frame = Frame(root, bg="pink")

board = []
for i in range(3):
    row = []
    for j in range(3):
        button = Button(
            board_frame,
            text="",
            width=10,
            height=5,
            font=("Helvetica", 15, "bold"),
            command=lambda row=i, column=j: on_click(row, column),
            bg="pink",
            fg="blue"
        )
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

root.mainloop()
