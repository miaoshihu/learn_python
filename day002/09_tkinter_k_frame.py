# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 21:35:42

"""

import tkinter as tk

counter = 0


window = tk.Tk()
window.title('my window')
window.geometry('200x300')


frame = tk.Frame(window)
frame.pack()

frame_l = tk.Frame(frame, )
frame_r = tk.Frame(frame,)
frame_l.pack(side='left')
frame_r.pack(side='right')
tk.Label(frame_l, text='on the frm_l1').pack()
tk.Label(frame_l, text='on the frm_l2').pack()
tk.Label(frame_r, text='on the frm_r').pack()


window.mainloop()