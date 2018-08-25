# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 14:00:15

"""
import time


def test(m, n):
    """
    test() method doc
    xxx
    """
    print('test()')
    print(time.ctime(), m, n)
    return m + n


if __name__ == '__main__':
    test(1, 2)
    print(test.__doc__)
    print(test.__name__)
