# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 16:51:38

1.以__xxx__形式的函数是魔法函数
2.魔法函数很多时候不需要主动调用

"""


class Student(object):

    def __init__(self):
        print('Student __init__')

    def __del__(self):
        print('Student__del__')


def test():
    print('test() start')
    zhangsan = Student()
    print('test() end')
    pass


def test2():
    print('test2() start')
    lisi = Student()
    del lisi
    print('test2() end')


if __name__ == '__main__':
    print('------------------------1------------------------')
    test()
    print('------------------------2------------------------')
    test2()
    print('------------------------3------------------------')

