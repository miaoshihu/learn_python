# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 17:00:43

"""


class Student(object):
    __slots__ = ('name')

    def __init__(self):
        self.name = 'zhangsan'
        self.age = 20


if __name__ == '__main__':
    zhangsan = Student()
