import tkinter as tk

window = tk.Tk()
window.title("New Project")
window.geometry("800x600")

item_label = tk.Label(window, text="Enter item", font=("Arial", 14))
item_label.pack(pady=(20, 5))

item_entry = tk.Entry(window, width=30, font=("Arial", 12))
item_entry.pack(pady=(0, 20))

button_frame = tk.Frame(window)
button_frame.pack(pady=(0, 20))

button1 = tk.Button(button_frame, text="ADD", fg = "Green",width=10, height=2)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(button_frame, text="EDIT", fg = "Orange", width=10, height=2)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(button_frame, text="DELETE", fg = "Red", width=10, height=2)
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = tk.Button(button_frame, text="CLEAR ALL", fg = "Purple", width=10, height=2)
button4.grid(row=1, column=1, padx=5, pady=5)

massive_text = tk.Text(window, width=60, height=15, font=("Arial", 11))
massive_text.pack(pady=(0, 20), padx=20)

bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=(0, 20))

bottom_button1 = tk.Button(bottom_frame, text="OPEN FILE", fg = "Blue", width=15, height=2)
bottom_button1.pack(side=tk.LEFT, padx=10)

bottom_button2 = tk.Button(bottom_frame, text="SAVE FILE", fg = "Gray", width=15, height=2)
bottom_button2.pack(side=tk.LEFT, padx=10)

window.mainloop()