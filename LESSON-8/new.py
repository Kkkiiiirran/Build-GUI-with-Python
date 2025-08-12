from tkinter import *
from tkinter.filedialog import *

# from address_book import delete


# def addItem():
#     item = item_entry.get()
#     listbox.insert(END,item)

# def deleteItem():
#     index = listbox.curselection()
#     if index:
#         listbox.delete(index)

# def clearAll():
#     listbox.delete(0,END)

# def editItem():
    
#     index = listbox.curselection()

#     if index: 
#         item = listbox.get(index)
#         item_entry.delete(0,END)
#         item_entry.insert(0,item)
#         listbox.delete(index) 

def delete_text():
    index = listbox.curselection()
    listbox.delete(index)


window = Tk()
listbox_frame = Frame(window, bg='#f0f0f0')
listbox_frame.pack(pady=10)
scrollbar = Scrollbar(listbox_frame, orient="vertical")
listbox = Listbox(listbox_frame, width = 70, height = 5, yscrollcommand =scrollbar.set )


scrollbar.config(command = listbox.yview) 

scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, padx=5)

delete = Button(window, text="delete", command=delete_text)
delete.pack(pady = 10)
listbox.insert(END, "Oo")
listbox.insert(END, "hello")

# listbox.delete(END)
# scrollbar = Scrollbar(listbox_frame, orient="vertical")


# listbox = Listbox(listbox_frame, width=70, height=5, yscrollcommand=scrollbar.set, font=('Arial', 11), bg='#fff')
# scrollbar.config(command=listbox.yview)

# scrollbar.pack(side=RIGHT, fill=Y)
# listbox.pack(side=LEFT, padx=5)

window.mainloop()