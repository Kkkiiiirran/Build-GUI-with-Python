from tkinter import *
from time import strftime
import random

def Get_Time():
    time = strftime("%H:%M:%S %p")
    red = random.randint(0,255)
    green =random.randint(0,255)
    blue = random.randint(0,255)
    newcolor= f"#{red:02x}{green:02x}{blue:02x}"
    time_label.config(text=time, bg=newcolor)
    time_label.after(1000,Get_Time)


root = Tk()
root.title("Digital Clock")

heading = Label(root, text="Digital Clock")

time_label = Label(root, fg="White", font=("Calibri", 40, "bold"))
time_label.pack()
Get_Time()

root.mainloop()