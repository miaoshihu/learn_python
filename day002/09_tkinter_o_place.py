# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 21:56:45

"""


import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')


tk.Label(window, text="账号",).place(x=10, y=100, anchor='nw')

window.mainloop()
