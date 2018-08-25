# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 18:16:15

"""


from tkinter import *

root = Tk()  # 这个得先于其他widget创建

w = Label(root, text="Hello, world!")
w.pack()  # widget size itself, 让自己可见

root.mainloop()  # widget不可见直到tk开始循环
