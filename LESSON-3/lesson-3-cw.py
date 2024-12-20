from tkinter import *
import random

options = ["Rock", "Paper", "Scissors"]

# detecting click
def RockClicked():
    user_selection="Rock"
    Play(user_selection)

def PaperSelecion():
    user_selection="Paper"
    Play(user_selection)

def ScissorsSelection():
    user_selection="Scissors"
    Play(user_selection)


# Displaying Win
def Tie():
    global player_score,computer_score
    game_start.config(text="Tie!!!", fg="Orange")
    
def PlayerWins():
    global player_score
    game_start.config(text="You Win!!!",fg="Green")
    player_score+=1
    
def ComputerWins():
    global computer_score
    game_start.config(text="Computer Wins, You lose.", fg="Red")
    computer_score+=1

# Displaying Score
def DisplayScore():
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Checking Win
def Play(user_selected):
    computer_choice = random.choice(options)
    you_selected_label.config(text=f"You Selected: {user_selected}")
    computer_selected_label.config(text=f"Computer Selected: {computer_choice}")
    if computer_choice==user_selected:
        Tie()
    elif (user_selected=="Rock" and computer_choice=="Scissors") or (user_selected=="Paper" and computer_choice=="Rock") or user_selected=="Scissors" and computer_choice=="Paper":
        PlayerWins()
        
    else:
        ComputerWins()

    DisplayScore()

    
root = Tk()
root.geometry("1000x300")
root.title("Rock Paper Scissors Game")

title = Label(root, text="ROCK PAPER SCISSORS", fg="Grey", font=("Heletica", 20))
title.pack(pady=10)

game_start = Label(root,text="Let's Start the Game...", font=("Helvetica", 13), fg="Green")
game_start.pack(pady=5)

frame = Frame(root)
frame.pack()

your_options = Label(frame, text="Your Options",fg = "Grey", font=("Helvetica", 15))

# Buttons
rock = Button(frame, text="Rock", bg="Pink",command=RockClicked)
paper = Button(frame, text="Paper", bg="Grey",command=PaperSelecion)
scissors = Button(frame,text="Scissors", bg="light blue",command=ScissorsSelection)

# Score Display
score = Label(frame, text="Score", font=("Helvetica", 15), fg="Grey")

user_selection = StringVar()
you_selected_label = Label(frame, text="You Selected:", font=("Helvetica", 13))
# user_entry = Entry(frame, textvariable=user_selection)

computer_selected_label = Label(frame, text="Computer Selected:",font=("Helvetica", 13))
computer_selection = StringVar()
# computer_entry = Entry(frame, textvariable=computer_selection)

player_score_label = Label(frame,text="Player Score:-",font=("Helvetica", 13))
player_score = 0
# player_score_display = Label(frame, textvariable=player_score)

computer_score_label = Label(frame, text="Computer Score:-",font=("Helvetica", 13))
computer_score = 0

# layout
your_options.grid(row=0,column=0, pady=12)

rock.grid(row=1,column=1,ipadx=30, ipady=5)
paper.grid(row=1,column=2, ipadx=30, ipady=5)
scissors.grid(row=1,column=3, ipadx=30, ipady=5, padx=20)

score.grid(row=2,column=0, pady=10)

you_selected_label.grid(row=3,column=1, padx=30)
computer_selected_label.grid(row=4,column=1)

player_score_label.grid(row=3,column=2, padx=30)
computer_score_label.grid(row=4,column=2)

root.mainloop()
