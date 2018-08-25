# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 20:35:42

"""
import tkinter as tk


def print_selection():
    l.config(text='your have selected %s' % var.get())


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

l = tk.Label(window, bg='yellow', width=20, text='label default')
l.pack()

var = tk.StringVar()

r1 = tk.Radiobutton(window, text='A选项', variable=var, value='A', command=print_selection)
r2 = tk.Radiobutton(window, text='B选项', variable=var, value='B', command=print_selection)
r3 = tk.Radiobutton(window, text='C选项', variable=var, value='C', command=print_selection)

r1.pack()
r2.pack()
r3.pack()

window.mainloop()
