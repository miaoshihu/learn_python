# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 14:37:54

"""
from functools import wraps


def my_decorator(x, y):  # 最外层是装饰器的参数
    print('------------------------0------------------------')
    print("my_decorator x = %s, y = %s" % (x, y))

    def wrapper_outter(func):  # 此外层是func

        print('wrapper_outter, x = %s, y = %s' % (x, y))

        @wraps(func)
        def wrapper_inner(*args, **kwargs):  # 最内层是*args, **kwargs
            print('wrapper_inner start')
            value = func(*args, **kwargs)
            print('wrapper_inner end')
            return value
        return wrapper_inner

    return wrapper_outter


@my_decorator(100, 200)
def test(m, n):
    """
    test() doc
    :return:
    """
    print('test(%s, %s)' % (m, n))
    return m + n


if __name__ == '__main__':
    print('------------------------1------------------------')
    test(1, 2)
    print('------------------------2------------------------')
