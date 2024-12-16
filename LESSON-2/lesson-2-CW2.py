from tkinter import *

root = Tk()
root.title("Temperature converter")

def Convert():
    
    celsius = temperature.get()
    if (celsius.replace('.','',1).isdigit()):
        error_msg.grid_forget()
        into_fahrenheit = (float(celsius)*9/5)+32
        fahrenheit.config(text=f"Temperature in Fahremheit: {into_fahrenheit}")
        fahrenheit.grid(row = 2, column = 0, columnspan = 2, pady = 10)
    else:
        error_msg.grid(row=1,column=1)
        fahrenheit.grid_forget()


title_label = Label(text="Celsius -> Fahrenheit", font=("Rosewood Std Regular", 24), fg="grey")
title_label.pack()

frame = Frame(root)
frame.pack(pady = 20)

temp_to_cels_label = Label(frame, text="Enter Temperature in Celsius: ")

temperature = StringVar()
temperature_label = Entry(frame, textvariable=temperature, background="white", width=40)

error_msg = Label(frame, text = 'Please enter valid input...', font = ("Helvetica", 8), fg = 'red')

fahrenheit = Label(frame)

convert_bttn = Button(frame, text = 'Convert', width = 30, fg = "black", bg = "light green", bd = 0, padx = 20, pady = 10, command = Convert)

temp_to_cels_label.grid(row=0,column=0)
temperature_label.grid(row=0,column=1)
# fahrenheit.grid(row = 2, column = 0, columnspan = 2, pady = 10)
convert_bttn.grid(row = 3, column = 0, columnspan = 2, pady = 10)


root.geometry('500x400')
root.mainloop()