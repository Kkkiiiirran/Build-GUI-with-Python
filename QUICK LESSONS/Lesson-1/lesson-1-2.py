from tkinter import *

data = {}

def save():
    username = user_entry.get()
    passcode = password_entry.get()
    data[username] = passcode
    
    submitlabel = Label(root, text="✅ Submitted!", fg="green")
    submitlabel.place(x=40, y=180)
    

    # Clear entry fields
    user_entry.delete(0, END)
    password_entry.delete(0, END)

root = Tk()
root.geometry('500x500')

# Labels
user_name = Label(root, text="Username")
user_name.place(x=40, y=60)

password = Label(root, text="Password")
password.place(x=40, y=100)

# Entry Fields (FIXED)
user_entry = Entry(root, width=60)
user_entry.place(x=120, y=60)

password_entry = Entry(root, show='*', width=60)
password_entry.place(x=120, y=100)

# Submit Button
button = Button(root, text="Submit", command=save)
button.place(x=40, y=140)

root.mainloop()
