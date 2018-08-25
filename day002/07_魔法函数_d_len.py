# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 17:14:05

"""


class Student(object):
    def __init__(self):
        self.__name = 'zhangsan'

    def __len__(self):
        return 100


if __name__ == '__main__':
    zhangsan = Student()
    print(len(zhangsan))
