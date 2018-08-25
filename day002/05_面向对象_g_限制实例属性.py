# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 17:01:52

"""


class Student(object):
    __slots__ = ("name",)  # 此元组用来限制可以有的属性

    def __init__(self):
        self.name = 'zhangsan'
        self.age = 30   # 不能运行 slots限制了属性
        pass


if __name__ == '__main__':
    zhangsan = Student()
