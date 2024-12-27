from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
my_address_book = {}

def add():
    name2 = name.get()
    if not name2:
        messagebox.showerror(title="No Name", message="Name field cannot be emtpy")
        return
    address2 = address.get()
    email2 = email.get()
    mobile2 = mobile.get()
    birthday2=birthday.get()
    details = {"address": address2,
               "email": email2,
               "mobile": mobile2,
               "birthday": birthday2

               }
    my_address_book[name2] = details
    print(my_address_book)
    address_book.insert(END,name2)
    clearall()

def delete():
    idx = address_book.curselection()
    if idx:
        item_name = address_book.get(idx)
        address_book.delete(idx)
        del my_address_book[item_name]
        print(my_address_book)
    else:
        messagebox.showerror(title="Error", message="Select a name")

def save():
    file = filedialog.asksaveasfile(defaultextension='.txt')
    if file:
        print(my_address_book,file=file)

def edit():
    idx = address_book.curselection()
    if idx:
        clearall()
        item_name = address_book.get(idx)
        address_book.delete(idx)
        name_entry.insert(END,item_name)
        address_entry.insert(END,my_address_book[item_name]["address"])
        mobile_entry.insert(END,my_address_book[item_name]["mobile"])
        email_entry.insert(END,my_address_book[item_name]["email"])
        birthday_entry.insert(END,my_address_book[item_name]["birthday"])

        del my_address_book[item_name]
    else:
        messagebox.showerror(title="Error", message="Select a name")


def open():
    global my_address_book
    file = filedialog.askopenfile(title='Open File')
    if file is not None:
        address_book.delete(0,END)
        my_address_book.clear()
        my_address_book = eval(file.read())
        for item in my_address_book:
            address_book.insert(END,item)
        print(my_address_book)


def clearall():
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    birthday_entry.delete(0,END)
    address_entry.delete(0,END)
    mobile_entry.delete(0,END)
    


def display(event):
    idx = address_book.curselection()
    if idx:
        selected_name = address_book.get(idx[0])  # Get the selected name from Listbox
        details = my_address_book.get(selected_name, {})
        info = (
            f"Address:\t{details.get('address', 'N/A')}\n"
            f"Email:\t{details.get('email', 'N/A')}\n"
            f"Mobile:\t{details.get('mobile', 'N/A')}\n"
            f"Birthday:\t{details.get('birthday', 'N/A')}"
        )
        messagebox.showinfo(title="Details", message=info)
main_win = Tk()

root = Frame(main_win)
root.pack(padx=20,pady=20)

heading = Label(root, text="My Address Book")
heading.grid(row=0,column=0,columnspan=3, padx=5,pady=5)


# scrollbar = Scrollbar(root, orient='vertical')
address_book = Listbox(root, width=35,height=15)
# scrollbar.config(command=listbox.yview)
address_book.grid(row=1,column=0, columnspan=3, rowspan=5,padx=5,pady=10)
# scrollbar.grid(row=1,column=0)
address_book.bind("<<ListboxSelect>>", display)
# buttons

edit_bttn = Button(root, text="Edit",width=10, command=edit)
delete_bttn = Button(root, text="Delete",width=10, command=delete)
open_bttn = Button(root, text="Open",width=10, command=open)
update_add_bttn = Button(root, text="Update/Add",width=20, command=add)
save_bttn = Button(root, text="Save", width=40,command=save)

edit_bttn.grid(row=6,column=0,pady=10,padx=10)
delete_bttn.grid(row=6,column=1,pady=10,padx=10)
open_bttn.grid(row=0,column=3,pady=10,padx=10)
update_add_bttn.grid(row=6,column=4,pady=10,padx=10)
save_bttn.grid(row=7,column=1, columnspan=3,padx=12)

# Fields

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

main_win.mainloop()