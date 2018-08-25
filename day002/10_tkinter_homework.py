# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 22:02:02

"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x300')

canvas = tk.Canvas(window, bg='blue', height=100, width=100)
image_file = tk.PhotoImage(file="image/biaoqing.png")
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.place(x=0, y=100, anchor='nw')

tk.Entry(window, text='用户名').place(x=100, y=100, anchor='nw')
tk.Entry(window, text='密码', show='*').place(x=100, y=150, anchor='nw')

tk.Label(window, text='注册账号', fg='blue', ).place(x=300, y=100, anchor='nw')
tk.Label(window, text='找回密码', fg='blue', ).place(x=300, y=150, anchor='nw')

tk.Checkbutton(window, text='记住密码', ).place(x=100, y=200, anchor='nw')
tk.Checkbutton(window, text='自动登录', ).place(x=200, y=200, anchor='nw')

button = tk.Button(window, text='登录').pack(side='bottom', pady=20)

window.mainloop()
