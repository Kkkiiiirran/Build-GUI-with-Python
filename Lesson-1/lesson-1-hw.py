from tkinter import *

root = Tk()

root.geometry('500x500')

heading = Label(root, text="Pick a Template").place(x=40,y=60)

template_name = Entry(root, width=40).place(x=140,y=60)

project_name = Label(root, text = "Project Name").place(x=40,y=100)

project_name_entry = Entry(root, width=40).place(x=140,y=100)

create_replt_btn = Button(root, text="Create repl",background="black",bd=5,fg="white").place(x=40,y=140)

root.mainloop()