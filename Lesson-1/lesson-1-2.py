from tkinter import *

root = Tk()

root.geometry('500x500')

user_name = Label(root, text="Username").place(x=40,y=60)

password = Label(root, text="Password").place(x=40,y=100)

user_entry = Entry(root, width=60).place(x=120, y=60)

password_entry = Entry(root, show='*',width=60).place(x=120, y=100)

button = Button(root, text = "Submit").place(x=40,y=140)

root.mainloop()