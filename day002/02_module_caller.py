# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 14:59:53

"""
from _02_module_er import add2num
import _02_module_er

if __name__ == '__main__':
    print(add2num(2, 3))
    print(_02_module_er.sub2num(3, 1))
    print(_02_module_er.__name__)
    print(__name__)
