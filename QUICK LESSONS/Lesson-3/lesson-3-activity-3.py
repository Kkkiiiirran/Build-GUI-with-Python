from tkinter import *

root = Tk()

root.geometry("150x200")

w = Label(root,text="HelloHello",font=50)

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,fill=Y)

myList = Listbox(root, yscrollcommand=scroll_bar.set)

for line in range(1,26):
    myList.insert(END,"Hi " + str(line))

myList.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=myList.yview)

root.mainloop()