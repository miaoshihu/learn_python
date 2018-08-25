# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 14:13:53

"""
import time
from functools import wraps


def decorator(func):
    """
    decorator() doc
    :param func:
    :return:
    """
    print('decorator() method called')

    @wraps(func)  # 将func属性赋给wraps
    def wrapper(*args, **kwargs):
        """
        wrapper() doc
        :param args:
        :param kwargs:
        :return:
        """
        print('wrapper() start')
        value = func(*args, **kwargs)
        print('wrapper() end %s' % value)
        return value

    return wrapper


@decorator
def test(m, n):
    """
    test() doc
    :return:
    """
    print(time.ctime(), m, n, 'test() method called')
    return m + n


if __name__ == '__main__':
    print('------------------------1------------------------')
    test(1, 2)
    print('------------------------2------------------------')
    print(test.__name__)
    print('------------------------3------------------------')
    print(test.__doc__)
    print('------------------------4------------------------')
