# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 19:38:24

"""

import tkinter as tk

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
    pass


window = tk.Tk()
window.title('my window')
window.geometry('200x300')

var = tk.StringVar()

l = tk.Label(window, textvariable=var, bg='green', width=15, height=2)
l.pack()

# l.place()  # 具体放在某个点上

button = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
button.pack()

window.mainloop()
