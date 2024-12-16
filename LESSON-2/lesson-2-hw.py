from tkinter import *

root =Tk()
root.geometry("350x100")
root.title('Currency Converter')

def Convert():
    in_rupees = float(rupees.get())
    in_dollars = in_rupees/80
    target_curr.config(text=in_dollars)




title = Label(root, text="RS --> $ CONVERTER")
title.pack()

frame = Frame(root)
frame.pack()

source_curr_label = Label(frame, text="Source Currency Amount (Rs)")
target_curr_label = Label(frame, text="target Currency Amount ($)")

rupees = StringVar()
input_curr = Entry(frame, textvariable=rupees)

target_curr = Label(frame)

convert_bttn = Button(frame, text="Convert",command=Convert)

source_curr_label.grid(row=0,column=0)
target_curr_label.grid(row=1,column=0)

input_curr.grid(row=0,column=3)
target_curr.grid(row=1,column=3)

convert_bttn.grid(row=2, column=2)

root.mainloop()

