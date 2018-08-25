# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 17:10:54

"""


class Student():
    def __init__(self):
        self.__name = "zhangsan"
        self.__age = 20
        pass

    def __str__(self):  # 像java的toString方法
        return 'Student instance : %s %s' % (self.__name, self.__age)


if __name__ == '__main__':
    zhangsan = Student()
    print(zhangsan)
