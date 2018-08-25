# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 17:35:55

"""

from enum import Enum, unique


@unique
class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7
    # SOMEDAY = 7   # 使用@unique装饰器，就不能有重复的value值


if __name__ == '__main__':
    print(Day.MON)
    print(Day['MON'])
    print(Day.MON.value)
    # print(Day.MON == Day.SOMEDAY)
    # Day.MON = Day.SAT   # 常量不能赋值

    for k, w in Day.__members__.items():
        print(k, w)
