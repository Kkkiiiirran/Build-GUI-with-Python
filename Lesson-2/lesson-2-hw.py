from tkinter import *
from tkinter.ttk import Progressbar

root = Tk()
root.config(bg="lightgreen")

root.geometry('500x500')

email = Label(root, text='Email', bg='light grey').place(x=40,y=100)
email_entry = Entry(root, width=40).place(x=100,y=100)

password = Label(root, text='Password', bg='light grey').place(x=40,y=140)
password = Entry(root, width=40).place(x=100, y=140)

food_choice = Label(root,bg='light grey', text="What food would you like: Chicken sandwich, B.L.T, Veg Sandwich?").place(x=40,y=180)

food_choice_entry = Entry(root, width=30).place(x=60,y=220)
food = Label(root, text='Food',bg='light grey').place(x=20, y=220)
food_quantity = Spinbox(root, from_=1, to=10).place(x=250,y=220)

drink_choice = Label(root, text="What beverage would you like: Cola, Fanta, Orange Juice, Water?").place(x=40,y=260)

drink = Label(root, text='Drink',bg='light grey').place(x=20, y=300)
drink_choice_entry = Entry(root, width=30).place(x=60,y=300)

drink_quantity = Spinbox(root, from_=1, to=10).place(x=250,y=300)

def bar():
    import time
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)

    progress['value']=40
    root.update_idletasks()
    time.sleep(1)

    progress['value']=50
    root.update_idletasks()
    time.sleep(1)

    progress['value']=60
    root.update_idletasks()
    time.sleep(1)

    progress['value']=80
    root.update_idletasks()
    time.sleep(1)

    progress['value']=100
    root.update_idletasks()
    time.sleep(1)

    root.destroy()
progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
progress.place(x=40, y=340)

submit_button = Button(root, text='Submit Order', command=bar)
submit_button.place(x=40, y=380)



root.mainloop()





