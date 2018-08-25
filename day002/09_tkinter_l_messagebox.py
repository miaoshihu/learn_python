# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 21:44:13

"""

import tkinter as tk
import tkinter.messagebox


def hit_me():
    tkinter.messagebox.showinfo(title='hi', message='hahaha')
    pass


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()