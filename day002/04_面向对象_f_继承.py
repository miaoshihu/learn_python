# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 16:05:40

"""


class Plane(object):
    def __init__(self, path, name):
        self.__path = path
        self.__name = name
        print("Plane__init__", path, name)
        pass

    def move(self):
        print('Plane move')
        pass


class HeroPlane(Plane):
    def __init__(self, path, name, engine):
        self.__engine = engine
        print('HeroPlane__init__', path, name)
        Plane.__init__(self, path, name)  # 如何调用父类的方法
        pass

    def move(self):
        Plane.move(self)  # 如何调用父类的方法
        print('HeroPlane move')
        pass


if __name__ == '__main__':
    hp = HeroPlane("./img/plane.png", '飞机', 100)
    hp.move()
