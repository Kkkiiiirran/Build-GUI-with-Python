import random
from tkinter import Tk
from tkinter import *
import tkinter.messagebox


correct_answer = random.randint(1,20)

def print_name():
    entered_name = name_entry.get()
    Message = (f"Entered name: {entered_name}")
    tkinter.messagebox.showinfo(title= "Welcome!", message = Message)
    frame_1.place_forget()
    frame_2.place(x = 0, y = 75)

def checkAnswer():
    user_answer = int(guess_entry.get())
    
    if user_answer>correct_answer:
        hint.config(text="TOO HIGH")
    elif user_answer<correct_answer:
        hint.config(text="TOO LOW")
    else:
      
        hint.config(text="YOU GOT IT RIGHT")



window = Tk()
window.title("Higher or Lower")
window.geometry("450x450")

frame_1 = Frame(window, width= 450, height= 450)
frame_1.place(x = 20, y = 20)

Title = Label(window, text = "Higher or lower", font = ("Aptos", 25, "bold"), fg = "White", bg = "Cyan")
Title.place(x = 135, y = 25)

name_label = Label(frame_1, text="Enter your name")
name_label.place(x=50, y=100)

name_entry = Entry(frame_1)
name_entry.place(x=145, y=100)

enter_button = Button(frame_1, text="Enter", fg= "Cyan", command = print_name)
enter_button.place(x=350, y=95)

frame_2 = Frame(window, width = 450, height = 450)
# frame_2.place( x = 0, y = 75)

guess_label = Label(frame_2, text="My Guess:")
guess_label.place(x=50, y=100)

guess_entry = Entry(frame_2)
guess_entry.place(x=145, y=100)

ent_button = Button(frame_2, text="Enter", fg= "Red", command=checkAnswer)
ent_button.place(x=350, y=95)

hint = Label(frame_2, bg="light blue", fg="red")
hint.place(x=100, y = 150 )

window.mainloop()