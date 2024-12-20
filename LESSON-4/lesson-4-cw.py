from tkinter import *
from time import strftime

root = Tk()

def Get_Time():
    time = strftime("%H:%M:%S: %p")
    time_label.config(text=time)
    time_label.after(1000, Get_Time)


time_label = Label(root, bg="orange", fg="white", font=("Calibri",40,"bold"))


time_label.pack()
Get_Time()
root.mainloop()
