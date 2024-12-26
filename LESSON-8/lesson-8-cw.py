from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

# Create the window
master = Tk()
master.title("Memorizer")
master.geometry("600x500")
master.config(bg='#f0f0f0')

# ----------------- CALLBACK FUNCTIONS -----------------

# Open file and populate the listbox
def openFile():
    fin = askopenfile(title='Open File')
    if fin is not None:
        listbox.delete(0, END)
        items = fin.readlines()
        for item in items:
            listbox.insert(END, item.strip())
        status_label.config(text="File opened successfully", fg="green")

# Save listbox content to a file
def saveFile():
    fout = asksaveasfile(defaultextension=".txt")
    if fout is not None:
        for item in listbox.get(0, END):
            print(item.strip(), file=fout)
        listbox.delete(0, END)
        status_label.config(text="File saved successfully", fg="green")

# Add item to the listbox
def addItem():
    new_item = item_entry.get()
    if new_item.strip():
        listbox.insert(END, new_item)
        item_entry.delete(0, END)
        status_label.config(text="Item added", fg="blue")
    else:
        status_label.config(text="Cannot add empty item", fg="red")

# Delete selected item
def deleteItem():
    index = listbox.curselection()
    if index:
        listbox.delete(index)
        status_label.config(text="Item deleted", fg="orange")
    else:
        status_label.config(text="No item selected to delete", fg="red")

# Clear all items from the listbox
def clearAll():
    listbox.delete(0, END)
    status_label.config(text="All items cleared", fg="orange")

# Edit selected item
def editItem():
    index = listbox.curselection()
    if index:
        current_text = listbox.get(index)
        item_entry.delete(0, END)
        item_entry.insert(0, current_text)
        listbox.delete(index)
        status_label.config(text="Edit the item and press ADD", fg="blue")
    else:
        status_label.config(text="No item selected to edit", fg="red")


# ----------------- WIDGETS -----------------

# Entry for adding/editing items
item_label = Label(master, text="Enter Item:", bg='#f0f0f0', font=('Arial', 12))
item_label.pack(pady=5)
item_entry = Entry(master, width=50, font=('Arial', 12))
item_entry.pack(pady=5)

# Buttons for operations
button_frame = Frame(master, bg='#f0f0f0')
button_frame.pack(pady=10)

add_button = Button(button_frame, text="ADD", command=addItem, width=15, bg='#4CAF50', fg='white')
edit_button = Button(button_frame, text="EDIT", command=editItem, width=15, bg='#FF9800', fg='white')
delete_button = Button(button_frame, text="DELETE", command=deleteItem, width=15, bg='#F44336', fg='white')
clear_button = Button(button_frame, text="CLEAR ALL", command=clearAll, width=15, bg='#9C27B0', fg='white')

add_button.grid(row=0, column=0, padx=5, pady=5)
edit_button.grid(row=0, column=1, padx=5, pady=5)
delete_button.grid(row=1, column=0, padx=5, pady=5)
clear_button.grid(row=1, column=1, padx=5, pady=5)

# Listbox with Scrollbar
listbox_frame = Frame(master, bg='#f0f0f0')
listbox_frame.pack(pady=10)

scrollbar = Scrollbar(listbox_frame, orient="vertical")
listbox = Listbox(listbox_frame, width=70, height=15, yscrollcommand=scrollbar.set, font=('Arial', 11), bg='#fff')

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, padx=5)

# File Operation Buttons
file_button_frame = Frame(master, bg='#f0f0f0')
file_button_frame.pack(pady=10)

open_button = Button(file_button_frame, text="OPEN FILE", command=openFile, width=15, bg='#2196F3', fg='white')
save_button = Button(file_button_frame, text="SAVE FILE", command=saveFile, width=15, bg='#607D8B', fg='white')

open_button.grid(row=0, column=0, padx=5)
save_button.grid(row=0, column=1, padx=5)

# Status Label
status_label = Label(master, text="Welcome to Memorizer!", bg='#f0f0f0', font=('Arial', 10, 'italic'), fg='gray')
status_label.pack(pady=5)

# ----------------- MAINLOOP -----------------
master.mainloop()
