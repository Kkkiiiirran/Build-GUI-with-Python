from tkinter import *
from tkinter.ttk import *

student_data = {}

def add():
    global student_data
    item_name = name.get()
    item_roll = roll_num.get()
    item_science_marks = science_marks.get()
    item_maths_marks = maths_marks.get()
    
    if item_name and item_roll and item_science_marks and item_maths_marks:  # Ensure all fields are filled
        percentage = ((item_science_marks + item_maths_marks) / 200) * 100
        percentage_entry.delete(0, END)  # Clear previous entry
        percentage_entry.insert(0, f"{percentage:.2f}")  # Display percentage with 2 decimal places
        
        details = {
            "Roll Number": item_roll,
            "Science Marks": item_science_marks,
            "Maths Marks": item_maths_marks,
            "Percentage": f"{percentage:.2f}"
        }
        student_data[item_name] = details
        
        # Insert data into Listbox
        
        record_list.insert(END, item_name)
        
        # Clear fields after adding
        name_entry.delete(0, END)
        roll_num_entry.delete(0, END)
        science_marks_entry.delete(0, END)
        maths_marks_entry.delete(0, END)
        percentage_entry.delete(0, END)
    else:
        print("Please fill all fields.")

def display(event):
    new_win = Toplevel()
    idx = record_list.curselection()
    if idx:
        item_name = record_list.get(idx)
        data = (f'Name: {item_name}\n'
                f'Roll Number: {student_data[item_name]["Roll Number"]}\n'
                f'Science Marks: {student_data[item_name]["Science Marks"]}\n'
                f'Maths Marks: {student_data[item_name]["Maths Marks"]}\n'
                f'Percentage: {student_data[item_name]["Percentage"]}')
        
        display_label = Label(new_win, text=data, justify=LEFT, font=("Arial", 12))
        display_label.pack(padx=20, pady=20)
        new_win.mainloop()


root = Tk()

root.title("STUDENT INFORMATION AND MARKS LOGGER")

mainframe = Frame(root)
mainframe.pack(padx=20,pady=20)

heading = Label(mainframe,text="STUDENT REPORT LOG")
heading.grid(row=0,column=0)
# fields

# Name
name_label = Label(mainframe, text="Name:")
name = StringVar()
name_entry = Entry(mainframe, textvariable=name)

name_label.grid(row=1,column=0)
name_entry.grid(row=1,column=1)

# Roll Number
roll_num_label = Label(mainframe, text="Roll Number")
roll_num = IntVar()
roll_num_entry = Entry(mainframe, textvariable=roll_num)

roll_num_label.grid(row=2,column=0)
roll_num_entry.grid(row=2,column=1)


# Science Marks
science_marks_label = Label(mainframe, text="Science Marks")
science_marks = IntVar()
science_marks_entry = Entry(mainframe, textvariable=science_marks)

science_marks_label.grid(row=1,column=4)
science_marks_entry.grid(row=1,column=5)

# Maths Marks
maths_marks_label = Label(mainframe, text="Maths Marks")
maths_marks = IntVar()
maths_marks_entry = Entry(mainframe, textvariable=maths_marks)

maths_marks_label.grid(row=2, column=4)
maths_marks_entry.grid(row=2,column=5)

# Percentage
percentage_label =Label(mainframe, text="Percentage")
percentage = DoubleVar()
percentage_entry = Entry(mainframe, textvariable=percentage)

percentage_label.grid(row=3,column=4)
percentage_entry.grid(row=3,column=5)


# listbox
record_list = Listbox(mainframe, width=100, height=10,bg="sky blue", font=("helvetica", 10))
record_list.grid(row=4,column=0,columnspan=6)
record_list.bind("<<ListboxSelect>>", display)
# buttons

edit_bttn = Button(mainframe, text="Edit",width=10)
delete_bttn = Button(mainframe, text="Delete",width=10)
open_bttn = Button(mainframe, text="Open",width=10)
update_add_bttn = Button(mainframe, text="Update/Add",width=20, command=add)
save_bttn = Button(mainframe, text="Save", width=40)

edit_bttn.grid(row=5,column=0)
delete_bttn.grid(row=5,column=1)
open_bttn.grid(row=5,column=2)
update_add_bttn.grid(row=5,column=3)
save_bttn.grid(row=5,column=4,columnspan=2)

root.mainloop()