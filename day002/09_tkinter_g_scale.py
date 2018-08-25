# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 20:46:50

"""

import tkinter as tk


def print_selection(v):
    # l.config(text='your have selected %s' % var.get())
    l.config(text='you have selected ' + v)
    pass


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

l = tk.Label(window, bg='yellow', width=20, text='label default')
l.pack()

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=False, tickinterval=2,
             resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
