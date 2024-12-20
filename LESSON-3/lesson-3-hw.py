from tkinter import *

root = Tk()
root.geometry("400x300")

def CalculateDistance():
    
    speed = speed_entry.get()
    time = time_entry.get()

    if speed.replace('.','',1).isdigit() and time.replace('.','',1).isdigit():
        cal_distance = float(speed)*float(time)
        distance.config(text=cal_distance)
        error_message_speed.grid_forget()
        error_message_speed.grid_forget()
    else:
        if not speed.replace('.','',1).isdigit() and not time.replace('.','',1).isdigit():
            error_message_speed.grid(row=2, column=0)
            
            error_message_time.grid(row=2, column=1)
        elif not speed.replace('.','',1).isdigit():
            error_message_speed.grid(row=2, column=0)
            error_message_time.grid_forget()
        else: 
            error_message_time.grid(row=2, column=1)
            error_message_speed.grid_forget()


    print(speed,time)

title = Label(root, text="Distance Calculator", font=("Helvetica", 20))
title.pack()

frame = Frame(root)
frame.pack()

speed_label = Label(frame, text="Speed(km/sec)")
speed_entry = Entry(frame)

time_label =Label(frame, text="Time(hours)")
time_entry = Entry(frame)

distance_label = Label(frame, text="Distance(km)")
distance = Label(frame, width=20, bg="white")

error_message_speed = Label(frame, text="Please enter a valid speed", font=("Helvetica", 8), fg="Red")
error_message_time = Label(frame, text="Please enter a valid time", font=("Helvetica", 8), fg="Red")

calculate_bttn = Button(root, text="Calculate Distance", command=CalculateDistance)


speed_label.grid(row=0,column=0)
speed_entry.grid(row=1,column=0)
time_label.grid(row=0,column=1)
time_entry.grid(row=1,column=1)
distance_label.grid(row=0,column=2)
distance.grid(row=1,column=2)
calculate_bttn.pack()
root.mainloop()