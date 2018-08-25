# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 15:29:33

"""


class Student(object):

    def __init__(self, name, age):
        print('__init__', name, age)
        self.__name = name
        self.__age = age
        pass

    def info(self):
        print('__info__', self.__name, self.__age)
        pass

    def setName(self, name):
        if name and (name != '') and (len(name) > 1):
            self.__name = name
        else:
            print('setName __name = ', name, 'not valid')

    def getName(self):
        return self.__name


if __name__ == '__main__':
    lisi = Student('李四', 31)
    lisi.info()
    lisi.setName('a')
    lisi.info()
    lisi.setName('James')
    lisi.info()
    print(lisi.getName())
