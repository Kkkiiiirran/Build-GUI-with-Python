from tkinter import *

root = Tk()

root.geometry('500x500')

button_top = Button(root, text="tOp",background="pink")
button_top.pack(side="top")

button_bottom = Button(root, text="bOtToM", background="red")
button_bottom.pack(side="bottom")

button_left = Button(root, text='lEfT',background="yellow")
button_left.pack(side="left")

button_right = Button(root, text="right",background="blue")
button_right.pack(side = "right")

root.mainloop()