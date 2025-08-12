# pack
# place
# grid

# pack
# side = TOP
# side = LEFT
# side = RIGHT
# side = BOTTOM

from tkinter import *

window = Tk()

window.geometry("500x500")

# start = Button(window, text="click me", bg = "red", fg="white")
# start.pack(side=TOP, ipadx=20)
# start2 = Button(window, text="click me", bg = "red", fg="white")
# start2.pack(side=TOP, ipadx=20, pady = 20)
start = Button(window, text="click me", bg = "red", fg="white")
start.place(x = 20, y=20)
start2 = Button(window, text="click me", bg = "red", fg="white")
start2.place(x=20, y = 60)
start3 = Button(window, text="click me", bg = "red", fg="white")
start3.place(x=100, y = 20)



window.mainloop()

