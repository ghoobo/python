import unittest

class test_tuple(unittest.TestCase):

    def test_tuple_define(self):
        # 正常声明一个元组
        tuple1 = (1, 2, 3, 4, 5)
        # 这样也行
        tuple2 = 1,2,3,4,5
        # 元组中只有一个元素，元素后要加逗号
        tuple3 = (1,)
        # 这样也行
        tuple4 = 1,
        # 不加的话就不是元组，跟不带括号效果一样
        tuple5 = (1)
        print(type(tuple1))
        print(type(tuple2))
        print(type(tuple3))
        print(type(tuple4))
        print(type(tuple5))

    def test_tuple_operate(self):
        tuple = (1, 2, 3, 4, 5)
        # 以下修改元组元素操作是非法的。
        # tuple[0] = 100
        # 不能通过del删除元组的某个元素，但是可以删除整个元组
        tuple1 = (1, 2, 3, 4, 5)
        del tuple1

    def test_tuple_function(self):
        tuple1 = (1, 2, 3, 4, 5)
        # 长度，跟list等一样
        a = len(tuple1)
        print(a)
        # 返回元组中元素最大值
        b = max(tuple1)
        print(b)
        # 返回元组中元素最小值
        c = min(tuple1)
        print(c)
        # 将可迭代系列转换为元组
        # 当使用list()、tuple()等方法将序列转换为list或者元组的时候，需要之前没有定义过名字为lsit、tuple的变量，不然就报错了
        list = ["a", "b", "c", "d"]
        tuple2 = tuple(list)
        print(tuple2)