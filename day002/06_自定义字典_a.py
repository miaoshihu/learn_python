# coding:utf8

"""
@ Author Jue
@ Date 2018-08-25 16:28:50

"""


class MyDict(object):

    def __init__(self, **kwargs):
        self.dict = kwargs

    # 显示字典
    def showdict(self):
        print(self.dict)

    # 删除
    def del_dict(self, key):
        value = self.dict.pop(key)
        print('del_dict key = %s, value = %s' % (key, value))
        return value

    def has_key(self, key):
        return not self.dict.get(key)

    def all_keys(self):
        return list(self.dict.keys())

    def merge_dict(self, newdt):
        print("merge_dict", newdt)
        self.dict.update(newdt)
        pass

    def merge_dict2(self, **kwargs):
        self.dict.update(kwargs)


if __name__ == '__main__':
    md = MyDict(name='lisi', age=22, address='beijing')
    md.showdict()
    md.del_dict('name')
    md.showdict()

    print(md.has_key('score'))
    print(md.has_key('age'))

    print(md.all_keys())
    print('------------------------1------------------------')
    dd = {'money': 100000000, 'language': 'Chinese'}
    md.merge_dict(dd)
    md.showdict()
    print('------------------------2------------------------')

    dd = {'gender': '男'}
    md.merge_dict2(**dd)
    md.showdict()

    pass
