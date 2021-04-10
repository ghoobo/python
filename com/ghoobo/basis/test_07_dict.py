import unittest

class test_dict(unittest.TestCase):

    def test_dict_define(self):
        # 一般的定义方式
        dict = {'name': 'guohb', 'age': 23, 'sex': 'man'}
        # 二般定义方式
        # 先定义个空字典，不是空的也可以，然后再加其他属性，类似map.put()
        dict1 = {}
        dict1['name'] = 'guohb'
        dict1['age'] = 23
        dict1['sex'] = 'man'
        print(dict1)
        # 输出某一个key的value，没有这个key的话会报错，跟map不一样，dict.get()方法key不存在时候不会报错
        print(dict['name'])
        # 删除字典元素
        del dict['sex']
        print(dict)
        # 清空字典内元素
        dict.clear()
        print(dict)
        # 删除字典
        del dict

    def test_dict_function(self):
        dict = {'name': 'guohb', 'age': 23, 'sex': 'man'}
        # 字典key的个数，或者元素的个数
        a = len(dict)
        print(a)
        # 输出字典，以可打印的字符串表示,好像toString()啊
        b = str(dict)
        print(type(b),b)

        dict1 = {'user': 'guohb', 'num': [1, 2, 3]}
        # 浅拷贝: 引用对象
        dict2 = dict1
        # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
        dict3 = dict1.copy()
        # 修改 data 数据
        dict1['user'] = 'root'
        dict1['num'].remove(1)
        # 输出结果
        print(dict1)
        print(dict2)
        print(dict3)
        # 类似于map.get()，不存在不会报错，第二个参数可以定义不存在时候默认返回值
        c = dict.get('name1',"none1")
        print(c)
        # 以列表返回可遍历的(键, 值) 元组数组
        d = dict.items()
        print(type(d),d)
        listd = list(d)
        print(type(listd), listd)
        # 返回一个迭代器，可以使用 list() 来转换为列表, values同理
        e = dict.keys()
        print(type(e), e)
        liste = list(e)
        print(type(liste), liste)
        # 把字典newDict的键/值对更新到dict里
        newDict = {'age': 24}
        dict.update(newDict)
        print(dict)
        # 删除字典给定键 key 所对应的值
        f = dict.pop('sex')
        print(f)
        print(dict)
        # 随机返回并删除字典中的最后一对键和值(最后一对为啥还叫随机删除)
        g = dict.popitem()
        print(g)
        print(dict)