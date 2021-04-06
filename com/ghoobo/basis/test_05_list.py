import unittest


class test_list(unittest.TestCase):

    def test_operator(self):
        # 除了下边的，其他跟str差不多
        list = ["red", "green", "blue", "yellow", "white", "black"]
        # 相当于list.add(1,"purple")
        list[1] = "orange"
        print(list)
        # 相当于list.add("purple")
        list.append("purple")
        print(list)
        # 相当于list.remove(1)
        del list[1]
        print(list)

    def test_list_function(self):
        tuple = ("red", "green", "blue", "yellow", "white", "black")
        # 元组转换为列表
        list1 = list(tuple)
        print(list1, type(list1))
        # 列表元素个数
        a = len(list1)
        print(a)
        # 列表后追加一个序列，两个都是列表的话直接“+”就行
        list1.extend(tuple)
        print(list1)
        # "red"这个元素在list1中出现的次数
        b = list1.count("red")
        print(b)
        # 将对象插入列表 好像等价于list1[1] = "orange"
        list1.insert(1,"orange")
        print(list1)
        # 删除一个元素，默认最后一个，好像等价于del list1[-1]
        list1.pop()
        print(list1)

