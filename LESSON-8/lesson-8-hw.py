from tkinter import *

# Function to change the background color
def change_bg(event):
    selected = listbox.curselection()
    if selected:  # Check if something is selected
        idx = selected[0]
        root.config(bg=listbox.get(idx))

# Function to add a new color
def add_color():
    new_color = color_entry.get()
    if new_color:
        listbox.insert(END, new_color)
        color_entry.delete(0, END)

# Function to remove a selected color
def remove_color():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

# Main window
root = Tk()
root.title("Color Selector App")
root.geometry("400x400")

# Frame for Listbox and Scrollbar
color_frame = Frame(root)
color_frame.pack(pady=20)

select_color = Label(color_frame)
scrollbar = Scrollbar(color_frame, orient='vertical')
listbox = Listbox(color_frame, width=30, height=10, yscrollcommand=scrollbar.set)

# Populate Listbox with colors
colors = [
    "red", "green", "blue", "yellow", "cyan",
    "magenta", "orange", "purple", "pink", "brown"
]
for color in colors:
    listbox.insert(END, color)

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT)

# Event binding for selection
listbox.bind('<<ListboxSelect>>', change_bg)

# Entry and Buttons for adding/removing colors
control_frame = Frame(root)
control_frame.pack(pady=10)

color_entry = Entry(control_frame, width=20)
color_entry.grid(row=0, column=0, padx=5)

add_button = Button(control_frame, text="Add Color", command=add_color)
add_button.grid(row=0, column=1, padx=5)

remove_button = Button(control_frame, text="Remove Color", command=remove_color)
remove_button.grid(row=0, column=2, padx=5)

root.mainloop()
