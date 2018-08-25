# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 20:54:45

"""

import tkinter as tk


def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        l.config(text='I love python')
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text='I love c++')
    elif var1.get() == 0 and var2.get() == 0:
        l.config(text='I love nothing')
    else:
        l.config(text='I love both')
        pass


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

l = tk.Label(window, bg='yellow', width=20, text='label default')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c2 = tk.Checkbutton(window, text='c++', variable=var2, onvalue=1, offvalue=0, command=print_selection)

c1.pack()
c2.pack()

window.mainloop()
