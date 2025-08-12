from tkinter import *

data = {}

def save():
    username = user_entry.get()
    passcode = password_entry.get()
    data[username] = passcode

    # Show confirmation message
    submit_label.config(text="✅ Submitted!", fg="green")

    # Clear entry fields
    user_entry.delete(0, END)
    password_entry.delete(0, END)

# Root setup
root = Tk()
root.geometry('500x300')
root.title("Login Form")

# Fonts and padding
LABEL_FONT = ("Arial", 12)
ENTRY_WIDTH = 40
PAD_X = 10
PAD_Y = 10

# Labels
Label(root, text="Username", font=LABEL_FONT).grid(row=0, column=0, padx=PAD_X, pady=PAD_Y, sticky=E)
Label(root, text="Password", font=LABEL_FONT).grid(row=1, column=0, padx=PAD_X, pady=PAD_Y, sticky=E)

# Entry fields
user_entry = Entry(root, width=ENTRY_WIDTH, font=LABEL_FONT)
user_entry.grid(row=0, column=1, padx=PAD_X, pady=PAD_Y)

password_entry = Entry(root, show='*', width=ENTRY_WIDTH, font=LABEL_FONT)
password_entry.grid(row=1, column=1, padx=PAD_X, pady=PAD_Y)

# Submit button
button = Button(root, text="Submit", font=LABEL_FONT, bg="#007acc", fg="white", command=save)
button.grid(row=2, column=1, pady=PAD_Y, sticky=W)

# Submission label (initially empty)
submit_label = Label(root, text="", font=("Arial", 10, "italic"))
submit_label.grid(row=3, column=1, sticky=W, padx=PAD_X)

root.mainloop()
