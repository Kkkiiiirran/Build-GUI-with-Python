from tkinter import *
import speech_recognition as sr
from tkinter import filedialog


# Voice Recognition Function
def Recognise():
    agent = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = agent.listen(source)
            text = agent.recognize_google(audio)  # Convert audio into text
        except:
            text = "Sorry, could not recognize your voice."
        text_area.delete(1.0, END)
        text_area.insert(END, text)


# Save Recognized Text to a File
def save():
    file = filedialog.asksaveasfile(defaultextension='.txt')
    if file:
        text = text_area.get(1.0, END)  # Get all text from the Text widget
        print(text,file=file)


# GUI Setup
newwin = Tk()
root = Frame(newwin)
root.pack(padx=40, pady=80)

heading = Label(root, text="Voice Recognition App", font=("helvetica", 30, "bold"))
heading.pack(pady=20)

cue = Label(root, text="Start Speaking...", font=("helvetica", 13, "bold"), fg="red")

text_area = Text(root, width=40, height=5, font=("helvetica", 15, "bold"))
text_area.pack()

frame = Frame(root)
frame.pack(pady=40)

start = Button(frame, text="Start Recording", bg="blue", fg="white", width=15,
               font=("helvetica", 10, "bold"), command=Recognise)
start.grid(row=0, column=0, padx=10, ipadx=10, ipady=3)

save_button = Button(frame, text="Save", bg="Orange", fg="white", width=10,
                     font=("helvetica", 10, "bold"), command=save)
save_button.grid(row=0, column=1, padx=10, ipadx=10, ipady=3)

root.mainloop()
