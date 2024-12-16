from tkinter import *

import calendar

def showCalendar():
    cal = Tk()

    cal.config(background="white")
    cal.geometry("700x1000")
    cal.title("Calendar")

    year = int(year_entry.get())

    year_content = calendar.calendar(year)

    cal_content = Label(cal, text=year_content, font="Consolas 12 bold")

    cal_content.grid(row=1, column=1)

    cal.mainloop()


if __name__=="__main__":
    root = Tk()

    root.config(background="White")

    root.title("Calendar")

    root.geometry("250x140")

    cal = Label(root, text="Enter Year", bg="light green")

    year_entry = Entry(root)

    show_bttn = Button(root, text="Show Calendar", bg="Magenta", fg="white", command=showCalendar)

    exit_bttn = Button(root, text="Exit", bg="Red",fg="White",command=root.destroy)

    cal.grid(row=1,column=1)
    year_entry.grid(row=2,column=1)
    show_bttn.grid(row=3,column=1)
    exit_bttn.grid(row=4,column=1)


    root.mainloop()