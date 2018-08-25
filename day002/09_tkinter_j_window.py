# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 21:20:24

"""

import tkinter as tk

counter = 0

def do_job():
    global counter
    counter += 1
    l.config(text='counter = %s' % counter)


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

l = tk.Label(window, text='', bg='yellow')
l.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0,)
menubar.add_cascade(labe='file', menu=filemenu)
filemenu.add_command(label='new', command=do_job)
filemenu.add_command(label='open', command=do_job)
filemenu.add_command(label='save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='exit', command=window.quit)

window.config(menu=menubar)

window.mainloop()