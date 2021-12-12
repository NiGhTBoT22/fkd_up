from data import question_data
from app_questions import Question
from quiz_brain import QuizBrain

import time
from tkinter import *
from tkinter import ttk 
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Welcome to NiGhT_BoT quiz !!!").grid(column=1, row=0)
ttk.Label(frm, text="Do you want to play the game?").grid(column=1, row=1)
ttk.Button(frm, text="start", command=root.destroy).grid(column=2, row=2)
root.mainloop()
tic = time.perf_counter()

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]

    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

toc = time.perf_counter()
duration = toc -tic
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="successfully completed NiGhT_BoT quiz !!!").grid(column=1, row=0)
#ttk.Label(frm, text="your score is "+ str(SCORE)).grid(column=1, row=1)
ttk.Label(frm, text="Do you want to quit the game?").grid(column=1, row=2)
ttk.Button(frm, text="time taken = " + str(int(duration)) + "seconds").grid(column=1, row=3)
ttk.Button(frm, text="stop", command=root.destroy).grid(column=3, row=4)
root.mainloop()
print("quitting the game")
quit()