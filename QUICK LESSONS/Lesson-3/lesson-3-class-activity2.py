from tkinter import *

root = Tk()

root.title("My favourtie Dishes")
root.geometry('200x250')

listbox = Listbox(root, height=10,width=15,bg="light grey",activestyle='dotbox',font="Helvetica",fg="Purple")
label = Label(root,text="Food Items")

listbox.insert(1,"Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3,"Burger")
listbox.insert(4,"Pizza")
listbox.insert(5,"Burrito")
label.pack()
listbox.pack()
root.mainloop()