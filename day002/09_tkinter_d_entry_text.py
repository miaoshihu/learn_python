# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 20:08:26

"""

import tkinter as tk


def insert_point():
    var = e.get()
    t.insert('insert', var)
    pass


def insert_end():
    var = e.get()
    t.insert('end', var)
    pass


def insert_some():
    var = e.get()
    t.insert(1, 1, var)
    pass


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

e = tk.Entry(window, show='*')
e.pack()

# l.place()  # 具体放在某个点上

b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end", command=insert_end)
b2.pack()

b3 = tk.Button(window, text="insert end", command=insert_some)
b3.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
