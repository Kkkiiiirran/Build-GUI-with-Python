from tkinter import *

import calendar

def showCal():
    root = Tk()

    root.config(background="white")

    root.title("Calendar")

    root.geometry("500x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(root, text=cal_content,font="Consolas 10 bold")

    cal_year.grid(row=5,column=1,padx=20)

    root.mainloop()


if __name__ =="__main__":
    top = Tk()

    top.config(background="white")

    # set the name of tkinter GUI window
    top.title("CALENDER")

    # Set the configuration of GUI window
    top.geometry("250x140")

    cal = Label(top,text="Calendar",bg="dark gray",font=("times", 28, 'bold'))

    year = Label(top, text="Enter Year", bg="light green")

    year_field = Entry(year)

    Exit = Button(top, text="Exit", fg="Black", bg="Red", command=exit)

    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)
    Show = Button(top, text="Show Calendar", fg="Black",
                  bg="Red", command=showCal)

    # Create a Exit Button and attached to exit function
    Exit = Button(top, text="Exit", fg="Black", bg="Red", command=exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    # start the GUI
    top.mainloop()