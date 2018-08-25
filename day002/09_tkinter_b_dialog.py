# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 18:26:59

"""

from tkinter import *


class App:

    def __init__(self, master):

        # tk 维持了一个widget tree
        frame = Frame(master)
        frame.pack()  # 每个widget都要调用pack方法

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
        )
        self.button.pack(side=LEFT)  # 会安置再frame的最左边，默认是top

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)  # 处理点击事件
        self.hi_there.pack(side=LEFT)  # 会安置再button的左边

    def say_hi(self):
        print("hi there, everyone!")


root = Tk()

app = App(root)

root.mainloop()
root.destroy()  # optional; see description below
