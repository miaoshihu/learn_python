# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 15:11:10

"""


class Person(object):
    role = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

    @classmethod
    def some_things(cls):
        print('some_things', cls)
        print("class method some_things called")


if __name__ == '__main__':

    zhangsan = Person('张三', 20)
    zhangsan.info()

    zhangsan.age += 1
    zhangsan.info()

    print(zhangsan.role)
    print(Person.role)

    Person.some_things()
