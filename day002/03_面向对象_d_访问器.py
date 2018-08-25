# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 15:41:18

"""


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        pass

    @property  # 访问器
    def my_age(self):
        return self.__age

    @property
    def birth(self):
        return 2018 - self.__age


if __name__ == '__main__':
    zhangsan = Student('张三', 22)
    print(zhangsan.my_age)  # 访问的时候，不需要再用括号

    print(zhangsan.birth)
