# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 15:51:45

"""


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def my_name(self):
        return self.__name

    @my_name.setter
    def my2_name(self, name):
        """
        1.有设置器必须要有访问器
        2.装饰器的名的前部分需要与设置器方法名相同
        """
        if name and len(name) > 1:
            print('my2_name name = ', name)
            self.__name = name
        else:
            print('my2_name name = ', name, 'is invalid data')


if __name__ == '__main__':
    zhangsan = Student('张三', 22)
    print(zhangsan.my_name)
    zhangsan.my2_name = '李四'
    print(zhangsan.my_name)
    print(zhangsan.__dict__)
    print(zhangsan.__doc__)

    for k, w in Student.__members__.items():
        print(k, w)
