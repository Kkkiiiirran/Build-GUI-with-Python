from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import tkinter.filedialog

address_book = {}

def save():
    file = tkinter.filedialog.asksaveasfile(defaultextension='.txt')
    if file:
        print(address_book,file=file)

def open():
    global address_book
    file = tkinter.filedialog.askopenfile(title="Open File")
    if file:
        listbox.delete(0,END)
        address_book.clear()
        address_book = eval(file.read())
        for item in address_book:
            listbox.insert(END,item)

def add():
    item_name = name_entry.get()
    item_address = address.get()
    item_email = email.get()
    item_mobile = mobile.get()
    item_birthday=birthday.get()
    details = {"address": item_address,
               "email": item_email,
               "mobile": item_mobile,
               "birthday": item_birthday

               }
    address_book[item_name] = details

    listbox.insert(END,item_name)
    print(address_book)

    clear_all()

def display_details(event):
    idx = listbox.curselection()
    if idx:
        name= listbox.get(idx[0])
        item = address_book[name]
        message = f"Name: {name}\n Address: {item['address']}\n Mobile: {item['mobile']}\n Email: {item['email']}\n Birthday:{item['birthday']}"
        tkinter.messagebox.showinfo("Details",message)
   

def clear_all():
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    email_entry.delete(0,END)
    mobile_entry.delete(0,END)
    birthday_entry.delete(0,END)

def delete():
    idx = listbox.curselection()
    name = listbox.get(idx[0])
    listbox.delete(idx)
    del address_book[name]

def edit():
    
    idx = listbox.curselection()
    if idx:
        clear_all()
        name = listbox.get(idx[0])

        details = address_book[name]

        item_address = details['address']
        item_mobile = details['mobile']
        item_email = details['email']
        item_birthday = details['birthday']

        name_entry.insert(END, name)
        address_entry.insert(END, item_address)
        mobile_entry.insert(END, item_mobile)
        email_entry.insert(END, item_email)
        birthday_entry.insert(END, item_birthday)

        listbox.delete(idx)
        del address_book[name]

root = Tk()

heading = Label(root, text="My Address Book")
heading.grid(row=0, columnspan=3)

# Name
name_label = Label(root, text="Name")
name = StringVar()
name_entry = Entry(root, textvariable=name)

name_label.grid(row=1,column=3,padx=30,pady=10)
name_entry.grid(row=1,column=4,padx=30,pady=10)

# Address
address_label = Label(root, text="Address")
address= StringVar()
address_entry = Entry(root, textvariable=address)

address_label.grid(row=2,column=3,padx=30,pady=10)
address_entry.grid(row=2,column=4,padx=30,pady=10)

# Mobile
mobile_label = Label(root, text="Mobile")
mobile = StringVar()
mobile_entry = Entry(root, textvariable=mobile)

mobile_label.grid(row=3,column=3,padx=30,pady=10)
mobile_entry.grid(row=3,column=4,padx=30,pady=10)

# Email
email_label = Label(root, text="Email:")
email = StringVar()
email_entry = Entry(root, textvariable=email)

email_label.grid(row=4,column=3,padx=30,pady=10)
email_entry.grid(row=4,column=4,padx=30,pady=10)

# Birthday
birthday_label = Label(root, text="Birthday:")
birthday = StringVar()
birthday_entry = Entry(root, textvariable=birthday)

birthday_label.grid(row=5,column=3,padx=30,pady=10)
birthday_entry.grid(row=5,column=4,padx=30,pady=10)


# listbox
listbox = Listbox(root, width=40, height=10)
listbox.grid(row=1,column=0, columnspan=3, rowspan=5,padx=5,pady=10)

listbox.bind('<<ListboxSelect>>', display_details)

# buttons

edit_bttn = Button(root, text="Edit",width=10, command=edit)
delete_bttn = Button(root, text="Delete",width=10, command=delete)
open_bttn = Button(root, text="Open",width=10, command=open)
update_add_bttn = Button(root, text="Update/Add",width=20, command=add)
save_bttn = Button(root, text="Save", width=40, command=save)

edit_bttn.grid(row=6,column=0,pady=10,padx=10)
delete_bttn.grid(row=6,column=1,pady=10,padx=10)
open_bttn.grid(row=0,column=3,pady=10,padx=10)
update_add_bttn.grid(row=6,column=4,pady=10,padx=10)
save_bttn.grid(row=7,column=1, columnspan=3,padx=12)


root.mainloop()