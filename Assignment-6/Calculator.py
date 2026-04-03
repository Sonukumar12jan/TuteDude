from tkinter import *
from turtle import clear

from numpy import equal

window = Tk()
window.geometry("500x500")

e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))


b = Button(window, text="1", width=12, command=lambda: click(1))
b.place(x=10, y=60)

b = Button(window, text="2", width=12, command=lambda: click(2))
b.place(x=80, y=60)

b = Button(window, text="3", width=12, command=lambda: click(3))
b.place(x=170, y=60)

b = Button(window, text="4", width=12, command=lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text="5", width=12, command=lambda: click(5))
b.place(x=80, y=120)

b = Button(window, text="6", width=12, command=lambda: click(6))
b.place(x=170, y=120)

b = Button(window, text="7", width=12, command=lambda: click(7))
b.place(x=10, y=180)

b = Button(window, text="8", width=12, command=lambda: click(8))
b.place(x=80, y=180)

b = Button(window, text="9", width=12, command=lambda: click(9))
b.place(x=170, y=180)

b = Button(window, text="0", width=12, command=lambda: click(0))
b.place(x=80, y=240)


def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
b = Button(window, text="+", width=12, command=add)
b.place(x=260, y=60)

def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
b = Button(window, text="-", width=12, command=subtract)
b.place(x=260, y=120)

def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
b = Button(window, text="*", width=12, command=multiply)
b.place(x=260, y=180)

def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
b = Button(window, text="/", width=12, command=divide)
b.place(x=170, y=240)



def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
b = Button(window, text="=", width=12, command=equal)
b.place(x=260, y=240)

def clear():
    e.delete(0, END)
b = Button(window, text="C", width=12, command=clear)
b.place(x=10, y=240)


mainloop()