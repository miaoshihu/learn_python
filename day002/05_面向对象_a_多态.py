# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 16:19:51

"""


class Anim(object):
    def bark(self):
        print('Anim() bark')
        pass


class Dog(Anim):
    def bark(self):
        print("Dog() bark 汪汪")


class Cat(Anim):
    def bark(self):
        print("Cat() bark 喵喵")


class Toy(object):
    def bark(self):
        print("Toy() bark, 机器不是anim，但是也可以bark ")
        pass


def anim_bark(anim):
    anim.bark()
    pass


if __name__ == '__main__':
    a = Anim()
    d = Dog()
    c = Cat()
    t = Toy()

    anim_bark(a)
    anim_bark(d)
    anim_bark(c)
    anim_bark(t)

