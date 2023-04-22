from tkinter import *
from datetime import datetime

cor1 = "darkslategray"
cor2 = "darkgoldenrod"

root = Tk()
root.title("Digital Clock")
root.resizable(width=FALSE, height=FALSE)
root.configure(bg=cor1)
root.geometry("400x200")


def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")
    l1.config(text=hour)
    l1.after(200, clock)

    l2.config(text=weekday + " " + str(day) + "  " + str(month) + " - " + year)
    l2.after(200, clock)


l1 = Label(root, font=('Arial', 60), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW)

l2 = Label(root, font=('Arial', 20), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW)

clock()
root.mainloop()
