from tkinter import *

window = Tk()
window.title("Product Guessing Game")
window.geometry("400x200")
window.configure(bg="white")


heading = Label(window, text="Product Guessing Game", font=("Helvetica", 18, "bold"), bg="white")
heading.place(x=10,y=10)

tries_label = Label(window, text="You have 5 tries left", font=("Helvetica", 12), bg="white")
tries_label.place(x=10,y=30)

guess_frame = Frame(window, bg="white")
guess_frame.place(x=10,y=80)

guess_label = Label(guess_frame, text="Your Guess:", font=("Helvetica", 12), bg="white")
# guess_label.place(x=20,y=20)

guess_entry = Entry(guess_frame, width=25)
# guess_entry.place(x=40,y=20)

check_button = Button(guess_frame, text="Check", bg="red", fg="red", font=("Helvetica", 10, "bold"))
# check_button.place(x=80,y=20)

guess_label.place(x=0, y=0)
guess_entry.place(x=100, y=0)
check_button.place(x=300, y=0)


window.mainloop()