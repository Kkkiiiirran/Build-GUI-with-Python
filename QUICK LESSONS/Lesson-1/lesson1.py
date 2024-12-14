from tkinter import *

root = Tk()

root.geometry('500x500')

button = Button(root, bd = 5, text = "Click Me!", background="pink",command=root.destroy)

button.pack(side="top")

root.mainloop()

