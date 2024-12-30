from tkinter import *
import random

root = Tk()

riddles = []
score = 0
total = 0

with open('LESSON-15/hw.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if ':' in line:
            question, answer = line.strip().split(':', 1)
            riddles.append({"question": question.strip(), "answer": answer.strip()})
    print(riddles)
num = random.randint(0, len(riddles)-1)

def default():
    global riddles, num
    word['text'] = riddles[num]['question']

def check():
    global riddles, num, total, score
    if answer_entry.get() == riddles[num]['answer'].lower():
        score += 1
        correct_answer.pack_forget()
    else:
        correct_answer.config(text=f"Correct Answer: {riddles[num]['answer']}")
        correct_answer.pack()
        # Schedule the correct_answer label to disappear after 3 seconds (3000 ms)
        root.after(3000, lambda: correct_answer.pack_forget())
    total+=1
    answer_entry.delete(0,END)
    score_text = f"Score: {score}/{total}"
    score_label.config(text=score_text)

    score_label.pack(side=LEFT)
    num = random.randint(0,len(riddles)-1)
    default()

def reset():
    global score, total
    score=0
    total=0
    score_label.pack_forget()

root.title("QUIZ GAME")
root.config(bg="black")

title = Label(root, text="QUIZ GAME",font=("Helvetica", 20, "bold"), bg="black", fg="white")
title.pack()

frame1 = Frame(root, bg="black")
frame1.pack(padx=20,pady=20)

word = Label(frame1, text="", bg="black", fg="white")
word.pack(padx=20,pady=20)

correct_answer = Label(frame1, text="", bg="black", fg="white")

answer = StringVar()
answer_entry = Entry(frame1, textvariable=answer, width=20, font=("Helvetica", 20))
answer_entry.pack(padx=20,pady=20)

check_bttn = Button(frame1, text="Check", bg="pink", fg="blue", width=10, height=1, font=("Helvetica", 15), command=check)
check_bttn.pack(padx=20,pady=20)

reset_bttn = Button(frame1, text="Reset", bg="Blue", fg="pink", width=10, height=1, font=("Helvetica", 15), command=reset)
reset_bttn.pack(padx=20,pady=20)

frame2= Frame(root, bg="black")
frame2.pack(padx=20,pady=20)

default()

score_label = Label(frame2)



root.mainloop()