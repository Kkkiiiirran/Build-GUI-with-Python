from tkinter import *
import tkinter.messagebox

def setTimer():
    in_hours = int(hours.get())
    in_minutes = int(minutes.get())
    in_seconds = int(seconds.get())

    time = (in_hours*3600) + (in_minutes*60) + in_seconds
    
    Countdown(time)

def Countdown(time):
    if time >= 0:
        hrs = time // 3600
        mins = (time % 3600) // 60
        secs = (time % 3600) % 60
        
        # Update the display with two-digit formatting
        hours.set(f"{hrs:02}")
        minutes.set(f"{mins:02}")
        seconds.set(f"{secs:02}")
        
        root.after(1000, Countdown, time - 1)
    else:
        tkinter.messagebox.showinfo("Time Countdown", "Time's up")


root = Tk()

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set("00")
minutes.set("00")
seconds.set("00")

hoursEntry = Entry(root, textvariable=hours,width=3, font=("Arial", 18, ""), bg="orange", fg="white")
minutesEntry = Entry(root, textvariable=minutes, width=3, font=("Arial", 18, ""), bg="orange", fg = "white")
secondsEntry = Entry(root, textvariable=seconds, width=3, font=("Arial", 18, ""), bg="orange", fg="white")

hoursEntry.grid(row=0,column=0)
minutesEntry.grid(row=0,column=1)
secondsEntry.grid(row=0,column=2)

setTimer_bttn = Button(root, text="Set Timer", command=setTimer)
setTimer_bttn.grid(row=1,column=1)
root.mainloop()