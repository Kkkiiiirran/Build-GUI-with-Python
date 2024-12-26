from tkinter import *
from tkinter.filedialog import *

def openFile():
    file = askopenfile(title="Open File")
    if file is not None:
        contents = file.readlines()
        listbox.delete(0,END)
        for content in contents:
            listbox.insert(END, content)

def saveFile():
    file = asksaveasfile(defaultextension='.txt')
    if file is not None:
        for item in listbox.get(0,END):
            print(item,file=file)
        listbox.delete(0,END)

def addItem():
    item = item_entry.get()
    listbox.insert(END,item)

def deleteItem():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

def clearAll():
    listbox.delete(0,END)

def editItem():
    
    index = listbox.curselection()

    if index: 
        item = listbox.get(index)
        item_entry.delete(0,END)
        item_entry.insert(0,item)
        listbox.delete(index) 


root = Tk()

enter_item_label = Label(root, text="Enter Item:")
item_entry = Entry(root,width=30)
enter_item_label.pack(anchor=CENTER)
item_entry.pack(anchor=CENTER)

# command buttons

button_frame = Frame(root)
button_frame.pack(pady=20)

add_button = Button(button_frame, text="ADD", bg="Green", fg="White", width=15, command=addItem)
edit_button = Button(button_frame, text="EDIT", bg="Orange", fg="White", width=15, command=editItem)
delete_button = Button(button_frame, text="DELETE", bg="red", fg="white", width=15, command=deleteItem)
clear_all_button = Button(button_frame, text="CLEAR ALL", bg="Purple", fg="White", width=15, command=clearAll)

add_button.grid(row=0,column=0, pady=10, padx=10)
edit_button.grid(row=0,column=1, pady=10, padx=10)
delete_button.grid(row=1,column=0,padx=10)
clear_all_button.grid(row=1,column=1, padx=10)

# listbox and scrollbar

listbox_frame = Frame(root)
listbox_frame.pack(pady=10)

scrollbar = Scrollbar(listbox_frame, orient="vertical")
listbox = Listbox(listbox_frame, width=90, height=10, yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, padx=5)


# file manipulation buttons

file_buttons = Frame(root)
file_buttons.pack(pady=20)

open_file_button = Button(file_buttons, text="OPEN FILE", bg="#2196F3", fg="WHite", width=15, command=openFile)
save_file_button = Button(file_buttons, text="SAVE FILE", bg="#607D8B", fg="white", width=15, command=saveFile)

open_file_button.grid(row=0,column=0, padx=10)
save_file_button.grid(row=0,column=1, padx=10)

root.mainloop()