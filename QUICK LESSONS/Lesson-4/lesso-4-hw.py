from tkinter import *
from tkinter import simpledialog, messagebox

root = Tk()
root.title("Library Management System")

# Configure grid columns for consistent spacing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Title label
title = Label(root, text="Library Management System", font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=4, pady=10)

# Label to display selected book information
book = Label(root, text="Selected Book:", font=("Arial", 12))
book.grid(row=1, column=0, sticky="w", padx=10, pady=10)

book_name = Label(root, text="None", width=50, bg="white", anchor="w", font=("Arial", 12))
book_name.grid(row=1, column=1, columnspan=2, sticky="w", padx=10)

# Callback function to handle Listbox selection
def cb(event):
    selection = book_list.curselection()
    if selection:
        index = selection[0]
        book_name['text'] = f"{books[index]}"
    else:
        book_name['text'] = "None"

# Add Book functionality
def add_book():
    new_book = simpledialog.askstring("Add Book", "Enter the name and author of the new book:")
    if new_book:
        books.append(new_book)
        book_list.insert(END, new_book)
        messagebox.showinfo("Success", f"Book '{new_book}' added to the list!")

# Issue Book functionality
def issue_book():
    selection = book_list.curselection()
    if not selection:
        messagebox.showerror("Error", "No book selected!")
        return
    index = selection[0]
    selected_book = books[index]
    
    # Confirmation dialog
    confirm = messagebox.askyesno("Confirm Issue", f"Do you want to issue '{selected_book}'?")
    if not confirm:
        return

    issued_book = books.pop(index)
    book_list.delete(index)
    issued_books.append(issued_book)
    issued_books_list.insert(END, issued_book)
    book_name['text'] = "None"
    messagebox.showinfo("Issued", f"Book '{issued_book}' has been issued!")

# Return Book functionality
def return_book():
    selection = issued_books_list.curselection()
    if not selection:
        messagebox.showerror("Error", "No issued book selected!")
        return
    index = selection[0]
    selected_book = issued_books[index]
    
    # Confirmation dialog
    confirm = messagebox.askyesno("Confirm Return", f"Do you want to return '{selected_book}'?")
    if not confirm:
        return

    returned_book = issued_books.pop(index)
    issued_books_list.delete(index)
    books.append(returned_book)
    book_list.insert(END, returned_book)
    messagebox.showinfo("Returned", f"Book '{returned_book}' has been returned to the list!")

# Create a frame to hold the Listbox and Scrollbar
list_frame = Frame(root)
list_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Add scrollbar for available books
scrollbar = Scrollbar(list_frame, orient=VERTICAL)

# Create Listbox for available books
book_list = Listbox(
    list_frame,
    width=40,
    height=15,
    activestyle='dotbox',
    bg="pink",
    fg="purple",
    font=("Arial", 10),
    yscrollcommand=scrollbar.set,
)
scrollbar.config(command=book_list.yview)
book_list.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

list_frame.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)

# List of books
books = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Pride and Prejudice by Jane Austen",
    "The Catcher in the Rye by J.D. Salinger",
    "The Hobbit by J.R.R. Tolkien",
    "Moby Dick by Herman Melville",
    "War and Peace by Leo Tolstoy",
    "The Lord of the Rings by J.R.R. Tolkien",
    "Jane Eyre by Charlotte Brontë",
    "The Alchemist by Paulo Coelho",
    "Crime and Punishment by Fyodor Dostoevsky",
    "Wuthering Heights by Emily Brontë",
    "Animal Farm by George Orwell",
    "Brave New World by Aldous Huxley",
    "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
    "The Grapes of Wrath by John Steinbeck",
    "The Chronicles of Narnia by C.S. Lewis",
    "The Kite Runner by Khaled Hosseini",
    "The Book Thief by Markus Zusak"
]
for book in books:
    book_list.insert(END, book)
book_list.bind('<<ListboxSelect>>', cb)

# Issued Books Section
issued_books_label = Label(root, text="Issued Books", font=("Arial", 14, "bold"))
issued_books_label.grid(row=1, column=3, sticky="n", padx=10, pady=(0, 5))

issued_books_list = Listbox(
    root,
    width=40,
    height=15,
    activestyle='dotbox',
    bg="lightblue",
    fg="black",
    font=("Arial", 10),
)
issued_books_list.grid(row=2, column=3, sticky="nsew", padx=10, pady=10)

issued_books = []

# Buttons for adding, issuing, and returning books
button_frame = Frame(root)
button_frame.grid(row=3, column=0, columnspan=4, pady=10)

add_button = Button(button_frame, text="Add Book", command=add_book, bg="green", fg="white", font=("Arial", 12))
add_button.grid(row=0, column=0, padx=10)

issue_button = Button(button_frame, text="Issue Book", command=issue_book, bg="blue", fg="white", font=("Arial", 12))
issue_button.grid(row=0, column=1, padx=10)

return_button = Button(button_frame, text="Return Book", command=return_book, bg="orange", fg="white", font=("Arial", 12))
return_button.grid(row=0, column=2, padx=10)

root.mainloop()
