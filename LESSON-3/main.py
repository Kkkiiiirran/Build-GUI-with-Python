from tkinter import *
import random as r, tkinter.font as tkf
win = "Lets start the game!"
pscore, cscore = 0,0

window = Tk()
window.title("Rock, Paper, Scissors!")
addfont = tkf.Font(size = 12)
window.geometry("600x600")

Label(window, text = "Lets play Rock, Paper, Scissors", font = tkf.Font(size = 12), fg = "Green").pack()

score_p = Label(window, text = "Player = " + str(pscore)).pack()
score_c = Label(window, text = "CPU = " + str(pscore)).pack()
winner = Label(window, text = win, pady = 10).pack()
rock_b = Button(window, text = "Rock", width = 5, bd = 1, bg = "Gray", pady= 5).place(x = 100, y = 200)
paper_b = Button(window, text = "Paper", width = 5, bd = 1, bg = "White", pady= 5).place(x = 200, y = 200)
sciss_b = Button(window, text = "Scissor", width = 5, bd = 1, bg = "Red", pady= 5).place(x = 300, y = 200)

window.mainloop()