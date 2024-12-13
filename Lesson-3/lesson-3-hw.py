from tkinter import *

root = Tk()

root.geometry('100x100')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, width=40,bg="light pink", fg="Purple",activestyle="dotbox", yscrollcommand=scrollbar.set)

languages = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "Ruby",
    "PHP",
    "Swift",
    "Go (Golang)",
    "Rust"
]

for language in languages:
    listbox.insert(END,language)

listbox.pack(side=LEFT)

scrollbar.config(command=listbox.yview)


root.mainloop()