# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 15:19:01

"""


class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print('student.info', self.__name, self.__age)


if __name__ == '__main__':
    zhangsan = Student('张三', 22)
    zhangsan.info()

    zhangsan.__age = '32'
    zhangsan.info()

    zhangsan._Student__age = 32  # 这样才能访问，对私有变量进行了重命名
    zhangsan.info()