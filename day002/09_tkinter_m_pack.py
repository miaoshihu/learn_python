# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 21:54:34

"""


import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

tk.Label(window, text=1).pack(side='top')
tk.Label(window, text=2).pack(side='bottom')
tk.Label(window, text=3).pack(side='right')
tk.Label(window, text=4).pack(side='left')
window.mainloop()
