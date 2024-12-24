from tkinter import *

from tkinter.ttk import Combobox

def ShowOrder():
    pizza_choice = pizza_type.get()
    quantity_choice = quantity.get()
    size_choice = size.get()
   
    order_details.config(text=f"You ordered {quantity_choice} {pizza_choice} {size_choice} Size Pizza(s)")
    order_details.grid(row=4, column=1)
root = Tk()

root.title("Pizza App")
root.geometry("500x200")
heading = Label(root, text="Welcome to Pizza Hut")
heading.pack()
frame = Frame(root)
frame.pack(padx=20)

select_pizza_label = Label(frame, text="Select Your Fav Pizza")
pizza_type = StringVar()
category_list = Combobox(frame, textvariable=pizza_type, width=20)
pizza_type_list = [
    "Veg Extravaganza",
    "Non-Veg Extravagana",
    "Delux",
    "Farmhouse",
    "Chefs kiss",
    "Double Decker"
]
category_list['values'] = pizza_type_list
category_list.set(pizza_type_list[0])

quantity_label = Label(frame,text="Enter Quantity")
quantity = IntVar()
quantity_list = Combobox(frame, textvariable=quantity, width=20)
quantity_list['values'] = list(range(1,11))
quantity_list.set(1)

size = StringVar()
sizeS = Radiobutton(frame, text="S", variable=size, value="Small")
sizeM = Radiobutton(frame, text="M", variable=size, value="Medium")
sizeL = Radiobutton(frame, text="L", variable=size, value="Large")
size.set("Small")

order_bttn = Button(frame, anchor="center", text="Order", bg="blue", fg="white", command=ShowOrder)

order_details = Label(frame)

select_pizza_label.grid(row=0,column=0)
category_list.grid(row=0,column=1, padx=80)

quantity_label.grid(row=1,column=0)
quantity_list.grid(row=1,column=1, padx=80)

sizeS.grid(row=0,column=2)
sizeM.grid(row=1,column=2)
sizeL.grid(row=2,column=2)

order_bttn.grid(row=3,column=1, ipadx=20, ipady=5)

root.mainloop()