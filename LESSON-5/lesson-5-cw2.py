from tkinter import *
import tkinter.messagebox
import random

# Initialize game state
tries = 10
answer = random.randint(1, 20)  # Generate a random number globally

def reset_game():
    """Reset the game state for a new round."""
    global tries, answer
    tries = 5
    answer = random.randint(1, 50)
    result.config(text="You have 5 tries left", fg="#2c3e50")
    guess_input.config(state=NORMAL)
    check_button.config(state=NORMAL)
    play_again_button.pack_forget()

def NameEntered():
    """Handle name entry and start the game."""
    player_name = name.get()
    message = f"Hello {player_name}, Guess a number between 1 and 50!"
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
    global tries, answer  
    
    try:
        my_guess = int(guess_input.get())  
    except ValueError:
        result.config(text="Please enter a valid number!", fg="red")
        return
    
    # Check the guess
    if my_guess == answer:
        result.config(text="You guessed it correctly!!!", fg="green")
        disable_game()  # End the game
    elif my_guess < answer:
        tries -= 1
        result.config(text=f"Too Low, {tries} tries left", fg="orange")
    else:
        tries -= 1
        result.config(text=f"Too High, {tries} tries left", fg="orange")

    if tries <= 0:
        result.config(text=f"Sorry, you are out of tries. The correct guess was {answer}!", fg="red")
        disable_game()

def disable_game():
    """Disable further input and check button, and show the Play Again button."""
    guess_input.config(state=DISABLED)
    check_button.config(state=DISABLED)
    play_again_button.pack(pady=20)

# Create the main window
root = Tk()
root.title("High Low Game")
root.geometry("600x400")
root.config(bg="#f0f8ff")  # Light blue background

# Heading
heading = Label(
    root,
    text="High Low Game",
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
guess = Label(frame2, text="My Guess:", font=("Helvetica", 14), bg="#f0f8ff", fg="#2c3e50")
guess_input = Entry(frame2, font=("Helvetica", 14))
check_button = Button(frame2, text="Check", font=("Helvetica", 14, "bold"), bg="#e74c3c", fg="white", command=Play)

# Play Again button (hidden initially)
play_again_button = Button(
    root,
    text="Play Again",
    font=("Helvetica", 14, "bold"),
    bg="#27ae60",
    fg="white",
    command=reset_game
)

# Run the Tkinter event loop
root.mainloop()
