from tkinter import *
from tkinter.colorchooser import askcolor

x = None
y = None
thickness = 1
color = "Black"
eraser_on = False

def setup():
    # global x,y,thickness,color
    # x = None
    # y = None
    # thickness = pen_width.get()
    # color = "Black"
    c.bind('<B1-Motion>', paint)
    c.bind('<ButtonRelease-1>', reset)
   
def paint(event):
    global thickness, color, x, y, eraser_on
    thickness = pen_width.get()

    if x and y:
        if eraser_on:
            c.create_line(x,y, event.x, event.y, width=thickness, fill='white', capstyle='round', smooth='True')
        else:
            c.create_line(x,y, event.x, event.y, width=thickness, fill=color, capstyle='round', smooth='True')

    x = event.x 
    y = event.y

def reset(event):
    global x,y
    x ,y = None, None

def choose_color():
    global color, eraser_on
    eraser_on=False
    color = askcolor(color=color)[1]

def use_eraser():
    global eraser_on
    eraser_on = True

def use_pen():
    global eraser_on
    eraser_on= False


root = Tk()

pen_button = Button(root, text="pen", command=use_pen)
pen_button.grid(row=0, column=0)

color_button = Button(root, text="color", command=choose_color)
color_button.grid(row=0, column=1)

eraser = Button(root, text="eraser", command=use_eraser)
eraser.grid(row=0, column=2)

pen_width = Scale(root, from_=1, to=10, orient=HORIZONTAL)
pen_width.grid(row=0, column=3)

c = Canvas(root, bg='white', width=600, height=600)
c.grid(row=1,columnspan=5)

setup()

root.mainloop()



