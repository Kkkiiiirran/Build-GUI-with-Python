from tkinter import *

root = Tk()
root.geometry('700x500')

def Convert():
    weight_in_kg = float(weight.get())  # Get input weight from entry box
    in_grams = weight_in_kg*1000
    in_pounds =  weight_in_kg*2.20462
    in_ounces = weight_in_kg * 35.274
    
    gram_entry.config(text=f"{in_grams}")
    pounds_entry.config(text=f"{in_pounds}")
    ounce_entry.config(text=f"{in_ounces}")

seek_weight = Label(root, text="Enter weight in Kg")
weight = StringVar()
weight_entry = Entry(root,textvariable=weight, width=40)

convert_bttn = Button(root, text="Convert", bg="Grey", command=Convert)

seek_weight.grid(row=1,column=1)
weight_entry.grid(row=1,column=2)
convert_bttn.grid(row=1,column=3)

gram = Label(root, text="Gram")
pounds = Label(root, text="Pounds")
ounce = Label(root, text="Ounce")

gram.grid(row=2,column=1)
pounds.grid(row=2,column=2)
ounce.grid(row=2,column=3)

gram_entry = Label(root, bg="white", width=20)
pounds_entry = Label(root, bg="white", width=20)
ounce_entry = Label(root, bg="white",width=20)

gram_entry.grid(row=3,column=1)
pounds_entry.grid(row=3,column=2)
ounce_entry.grid(row=3,column=3)

root.mainloop()

