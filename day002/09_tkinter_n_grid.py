# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 21:56:45

"""


import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=1, pady=10)

window.mainloop()
