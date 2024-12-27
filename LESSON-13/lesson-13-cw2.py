from tkinter import *
from gtts import gTTS
import os

def play():
    agent = gTTS(text.get(), lang='en', slow=False)

    agent.save('audio.mp3')
    os.system("audio.mp3")


root = Tk()

root.config(bg="light green")

frame = Frame(root,bg="lightPink",height="250")
frame.pack(fill=X)

heading = Label(frame, text="Text To Speech", bg="lightPink" ,font=("Helvetica", 30, "bold"))
heading.place(y=90, x=500)

frame2 = Frame(root,bg="lightgreen",height="750")
frame2.pack(fill=X)

text = StringVar()
text_entry = Entry(frame2, width=30, font="bold, 30", textvariable=text)
text_entry.place(x=300, y=120)

submit_bttn = Button(frame2, text="Sumit", bg="Yellow", width=15, height=2, command=play)
submit_bttn.place(x=550, y=180)
root.mainloop()