# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 17:18:37

"""


class Color:

    def __iter__(self):
        """
        遍历对象开始时，先调用这个函数
        """
        print('student__iter__')
        self.value = 5
        return self

    def __next__(self):
        """
        每循环一次，便调用一次，一直到发生了StopIteration异常为
        """
        print('student__next__')
        if self.value >= 0:
            self.value -= 1
            return self.value
        else:
            raise StopIteration


if __name__ == '__main__':
    print('------------------------0------------------------')
    c = Color()
    print('------------------------1------------------------')
    for x in c:
        print(x)
