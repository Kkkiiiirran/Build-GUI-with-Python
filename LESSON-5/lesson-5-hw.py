from tkinter import *
import tkinter.messagebox
import random
import sys

# Initialize game state
tries = 5
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
product = num1 * num2

def reset_game():
    """Reset the game state for a new round."""
    global tries, num1, num2, product
    tries = 5
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    product = num1 * num2
    result.config(text="You have 5 tries left", fg="#2c3e50")
    guess_input.config(state=NORMAL)
    check_button.config(state=NORMAL)

def NameEntered():
    """Handle name entry and start the game."""
    player_name = name.get()
    if not player_name.strip():
        tkinter.messagebox.showerror("Error", "Please enter your name!")
        return
    message = f"Hello {player_name}, the first number is {num1}. Guess the product of {num1} and another random number!"
    tkinter.messagebox.showinfo("Greeting", message)
    result.config(text=f"{player_name}, you have {tries} tries left")
    frame.pack_forget()
    result.pack(pady=20)
    frame2.pack(pady=20)
    guess.grid(row=0, column=0, padx=10, pady=10)
    guess_input.grid(row=0, column=1, padx=10, pady=10)
    check_button.grid(row=0, column=2, padx=10, pady=10)

def Play():
    """Handle each guess."""
    global tries
    
    try:
        my_guess = int(guess_input.get())  
    except ValueError:
        result.config(text="Please enter a valid number!", fg="red")
        return
    
    # Check the guess
    if my_guess == product:
        tkinter.messagebox.showinfo("Congratulations", f"You guessed correctly! The product is {product}.")
        root.quit()  # Quit the application
    elif my_guess < product:
        tries -= 1
        result.config(text=f"Too Low, {tries} tries left", fg="orange")
    else:
        tries -= 1
        result.config(text=f"Too High, {tries} tries left", fg="orange")

    if tries <= 0:
        result.config(
    text=f"Sorry, you are out of tries.\nThe second number was {num2} and the correct product was {product}!",
    fg="red"
)

        disable_game()

def disable_game():
    """Disable further input and check button."""
    guess_input.config(state=DISABLED)
    check_button.config(state=DISABLED)

# Create the main window
root = Tk()
root.title("Product Guessing Game")
root.geometry("600x400")
root.config(bg="#f0f8ff")  # Light blue background

# Heading
heading = Label(
    root,
    text="Product Guessing Game",
    font=("Helvetica", 24, "bold"),
    bg="#f0f8ff",
    fg="#2c3e50"
)
heading.pack(pady=20)

# Frame 1: Name entry
frame = Frame(root, bg="#f0f8ff")
frame.pack()

name_label = Label(frame, text="Enter your name:", font=("Helvetica", 14), bg="#f0f8ff", fg="#2c3e50")
name_label.grid(row=0, column=0, padx=10, pady=10)
name = Entry(frame, font=("Helvetica", 14))
name.grid(row=0, column=1, padx=10, pady=10)
enter_bttn = Button(frame, text="Enter", font=("Helvetica", 14, "bold"), bg="#3498db", fg="white", command=NameEntered)
enter_bttn.grid(row=0, column=3, padx=10, pady=10)

# Frame 2: Game interface (hidden initially)
frame2 = Frame(root, bg="#f0f8ff")

result = Label(root, text="You have 5 tries left", font=("Helvetica", 14), bg="#f0f8ff", fg="#2c3e50")
guess = Label(frame2, text="Your Guess:", font=("Helvetica", 14), bg="#f0f8ff", fg="#2c3e50")
guess_input = Entry(frame2, font=("Helvetica", 14))
check_button = Button(frame2, text="Check", font=("Helvetica", 14, "bold"), bg="#e74c3c", fg="white", command=Play)

# Run the Tkinter event loop
root.mainloop()
