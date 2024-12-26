from tkinter import *

from tkinter.ttk import Combobox

def PrintTable():
    number= int(num.get())
    limit = int(limit_num.get())
    text = ""
    for i in range(limit):
        text += f"{number:^5} X {i+1:^5} = {number*(i+1):^5}\n"
    result_label.config(text=text)
    result_label.grid(row=4, column=1, ipadx=5, pady=10)
    print(text)


root = Tk()

root.title("Mathematical Table")

heading = Label(root, text="Mathematical Table")
heading.pack(pady=15)

frame = Frame(root)
frame.pack(padx=10)

num = IntVar()
number_range_label = Label(frame, text = "Number and Range")
number_range = Combobox(frame, textvariable=num, width=5)
number_range['values'] = list(range(101))

limit_num = IntVar()
limit_10 = Radiobutton(frame, text="10", variable=limit_num, value=10)
limit_20 = Radiobutton(frame, text="20", variable=limit_num, value=20)
limit_30 = Radiobutton(frame, text="30", variable=limit_num, value=30)

limit_num.set(10)

generateButton = Button(frame, text="Generate", command=PrintTable)
result_label = Label(frame, bg="maroon", fg="white", font=("Arial", 12, "bold"))


number_range_label.grid(row=0,column=0)
number_range.grid(row=0, column=1, padx=35)
limit_10.grid(row=0,column=2)
limit_20.grid(row=1,column=2)
limit_30.grid(row=2,column=2)
generateButton.grid(row=3,column=1, ipadx=3, ipady=2, pady=10)


root.mainloop()
