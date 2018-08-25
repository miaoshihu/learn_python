# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 14:01:28

"""
import time


def decorator(func):
    """
    decorater() doc
    """
    print('decorator')  # 开始的时候调用了!

    def wrapper(*args, **kwargs):
        """
        wrapper() doc
        """
        print('wrapper start, call func')
        print('wrapper args = ', args)
        print('wrapper *args=', *args)
        value = func(*args, **kwargs)
        print('wrapper end, return %s' % value)
        return value

    return wrapper


@decorator
def test(m, n):
    """
    test() doc
    """
    print(time.ctime(), m, n, 'test() called')
    return m + n


if __name__ == '__main__':
    print('------------------------1------------------------')
    test(1, 2)
    print('------------------------2------------------------')
    print(test.__doc__)  # 打印的是wrapper doc
    print(test.__name__)
    print('------------------------3------------------------')
