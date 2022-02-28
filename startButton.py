import tkinter, time
from subprocess import Popen

Freq = 2500
Dur = 150

top = tkinter.Tk()
top.title('MapAwareness')
top.geometry('200x100')

def start():
    import os
    print("Started!")
    Popen(["python", "Final Tictactoe.py"])


def stop():
    print("Stopped")
    top.destroy()

startButton = tkinter.Button(top, height=2, width=20, text ="Start", 
command = start)
stopButton = tkinter.Button(top, height=2, width=20, text ="Stop", 
command = stop)

startButton.pack()
stopButton.pack()
top.mainloop()
