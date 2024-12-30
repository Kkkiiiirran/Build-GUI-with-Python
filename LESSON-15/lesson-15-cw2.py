from tkinter import *
import random

answers=["apple","mango","banana",'achieve','kolkata','evening','servant','receiver','london','ferrari','hollow','horror','master','morning','bottle','pen','router','copy','narrow','wide','dive','love','block','right','simple','deaf','single','knight','hope']
words=['plpea','gnoma','annaba','hveeica','lkaatko','egvnine','aestnrv','iceever','lndono','rrreifa','wllhoo','oohrrr','rtemsa','nnrgimo','lttobe','enp','ourrte','ypco','rraonw','wdie','ievd','elov','klboc','ightr','plmsie','dfea','glneis','ghtkni','opeh']
num = random.randint(0,len(words)-1)
score = 0
total = 0

def default():
    global word, answers, num
    word.config(text=words[num])

def check():
    global num, answers, score, total
    if answer_entry.get() == answers[num]:
        score+=1
    total+=1

    answer_entry.delete(0,END)
    score_text = f"Score: {score}/{total}"
    score_label.config(text=score_text)

    score_label.pack(side=LEFT)
    num = random.randint(0,len(words)-1)
    default()

def reset():
    global score, total
    score=0
    total=0
    score_label.pack_forget()

root = Tk()

root.title("JUMBLED WORD GAME")
root.config(bg="black")

title = Label(root, text="JUMBLED WORD GAME",font=("Helvetica", 20, "bold"), bg="black", fg="white")
title.pack()

frame1 = Frame(root, bg="black")
frame1.pack(padx=20,pady=20)

word = Label(frame1, text="", font=("Helvetica", 20), bg="black", fg="white")
word.pack(padx=20,pady=20)

answer = StringVar()
answer_entry = Entry(frame1, textvariable=answer, width=20, font=("Helvetica", 20))
answer_entry.pack(padx=20,pady=20)

check_bttn = Button(frame1, text="Check", bg="pink", fg="blue", width=10, height=1, font=("Helvetica", 15), command=check)
check_bttn.pack(padx=20,pady=20)

reset_bttn = Button(frame1, text="Reset", bg="Blue", fg="pink", width=10, height=1, font=("Helvetica", 15), command=reset)
reset_bttn.pack(padx=20,pady=20)
frame2= Frame(root, bg="black")
frame2.pack(padx=20,pady=20)

score_label = Label(frame2)

default()

root.mainloop()