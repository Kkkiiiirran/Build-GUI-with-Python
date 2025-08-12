# layout methods
import random
from tkinter import *

from time import strftime
bg = "black"
fg = "white"

def Time():
    global bg,fg
    
    curr_time = strftime("%H : %M : %S %p")
    time_label.config(text=curr_time, bg = bg, fg=fg)
    time_label.after(1000,  Time)

    bg,fg = fg,bg


window = Tk()

time_label = Label(window, font = ("Calibri", 40, "bold"))
time_label.pack(side=TOP)

Time()

window.mainloop()