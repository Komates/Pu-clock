from tkinter import *
import tkinter
from datetime import datetime




cor1 = "#3d3d3d"  # black
cor2 = "#fafcff"  # white
cor3 = "#21c25c"  # green
cor4 = "#eb463b"  # red
cor5 = "#dedcdc"  # gray
cor6 = "#3080f0"  # blue

root = Tk()
root.title("DIGITAL CLOCK")
root.geometry('540x220')
root.resizable(width=FALSE, height=FALSE)
root.configure(background=cor1)


def clock():
    time = datetime.now()

    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")
    l1.config(text=hour)
    l1.after(200, clock)
    l2.config(text=weekday + "" + str(day) + "/" + str(month) + "/" + (year))


l1 = Label(root, text="10:05:05", font=('digital-7  80'), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(root,  font=('digital-7  20'), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)

clock()

root.mainloop()