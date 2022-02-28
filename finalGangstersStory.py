from tkinter import *
tk = Tk()

def delay():
    label['text'] = 'You chose A'
def delay2():
    label['text'] = 'You chose B'
def delay3():
    label['text'] = 'You chose C'
def delay4():
    label['text'] = 'Test'
    btn.pack()
    btn2.pack()
    btn3.pack()
    btn4["state"] = DISABLED
    btn4(tk, visible = 'no')

label = Label(tk, text = "Evil Gangsters Story by Aaryaman and Reyansh")
btn = Button(tk, text="A, Run", command=delay)
btn2 = Button(tk, text="B, Get in the car", command=delay2)
btn3 = Button(tk, text="C, Get your gun", command=delay3)
btn4 = Button(tk, text="Continue➡", command=delay4)

label.pack()
#btn.pack()
#btn2.pack()
#btn3.pack()
btn4.pack()
