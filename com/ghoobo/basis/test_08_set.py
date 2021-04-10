import unittest

class test_set(unittest.TestCase):

    def test_set_define(self):
        # 定义一个一般的set
        set1 = {1, 2, 3, 4, 5}
        # 定义一个空set 不能用set={}，这是定义空字典的
        emptySet = set()

    def test_set_operator(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {6, 7, 8, 9}
        # 给set添加元素
        set2.add(10)
        print(set2)
        # 给set添加元素，且参数可以是列表，元组，字典等,并且参数可以有多个
        set1.update(set2)
        print(set1)
        # 删除元素 如果元素不存在，则会发生错误
        set1.remove(10)
        print(set1)
        # 删除元素 如果元素不存在，不会发生错误
        set1.discard(12)
        print(set1)
        # 随机删除一个元素,并没有感觉到随机
        a = set1.pop()
        print(a)
        print(set1)
        # 清空set
        set2.clear()
        print(set2)

    def test_set_function(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        # 返回多个集合的差集
        set3 = set1.difference(set2)
        set4 = set1 - set2
        print(set3)
        print(set4)
        # 返回集合的交集
        set5  = set1.intersection(set2)
        set6  = set1 & set2
        print(set5)
        print(set6)
        # 判断两个集合是否包含相同的元素 如果没有返回 True，否则返回 False 就是这么不合情理
        a = set1.isdisjoint(set2)
        print(a)
        # 返回两个集合的并集
        set7 = set1.union(set2)
        set8 = set1 | set2
        print(set7)
        print(set8)

