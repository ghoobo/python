import unittest


class test_datatype(unittest.TestCase):

    def test_datatype(self):
        # 整型变量
        counter = 100
        # 浮点型变量
        miles = 1000.0
        # 字符串
        name = "runoob"

        # 同时为多个变量赋值
        a = b = c = 1
        a, b, c = 1, 2, "runoob"

        print(isinstance(a, int))

        # 删除a的引用
        del a

    def test_list(self):
        list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
        tinylist = [123, 'runoob']
        # 输出完整列表
        print (list)
        # 输出列表第一个元素
        print (list[0])
        # 从第二个开始输出到第三个元素
        print (list[1:3])
        # 输出从第三个元素开始的所有元素
        print (list[2:])
        # 输出两次列表
        print (tinylist * 2)
        # 连接列表
        print (list + tinylist)
        # 索引1到索引4的位置并设置为步长为2截取list
        print (list[1:4:2])
        # 以下用于反转字符串或list，两种都可
        print (list[-1::-1])
        print (list[::-1])

        # 将一句话的每个单词反转
        input = 'I like runoob'
        inputWords = input.split(" ")
        # 反转列表
        inputWords = inputWords[-1::-1]
        # 重新组合字符串
        output = ' '.join(inputWords)
        print(output)

    def test_tuple(self):
        # 元组 不知道什么用
        tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
        tinytuple = (123, 'runoob')
        # 空元组
        tuple1 = ()
        # 只有一个元素记得加逗号,为了跟数学公式中的小括号做区分
        tuple2 = (1,)
        # 输出完整元组
        print (tuple2)
        # 输出元组的第一个元素
        print (tuple[0])
        # 输出从第二个元素开始到第三个元素
        print (tuple[1:3])
        # 输出从第三个元素开始的所有元素
        print (tuple[2:])
        # 输出两次元组
        print (tinytuple * 2)
        # 连接元组
        print (tuple + tinytuple)

    def test_Set(self):
        # 集合（其实就是Set）
        sites = {'Google', 'Taobao', 'Ghoobo', 'Facebook', 'Zhihu', 'Baidu'}
        # 输出集合，重复的元素被自动去掉
        print(sites)
        # 成员测试
        if 'Ghoobo' in sites :
            print('Ghoobo 在集合中')
        else :
            print('Ghoobo 不在集合中')

        # 定义集合的其他方法
        a = set('abracadabra')
        b = set('alacazam')
        #当定义空集合时，不能 sites={},这是定义空字典的
        c = set() # 定义一个空集合
        print(a)
        print(b)
        print(c)
        # set可以进行集合运算
        # a 和 b 的差集
        print(a - b)
        # a 和 b 的并集
        print(a | b)
        # a 和 b 的交集
        print(a & b)
        # a 和 b 中不同时存在的元素
        print(a ^ b)

    def test_Dictionary(self):
        # Dictionary(其实就是Map，关键字其实就是key)
        ghoobo1 = {} # 定义一个空字典
        ghoobo1["name"] = "郭浩博"
        ghoobo1["age"] = "23"
        ghoobo1["sex"] = "男"
        ghoobo2 = {"name":"郭浩博", "age":"23", "sex":"男" }
        # 输出键为name的值
        print (ghoobo1["name"])
        # 输出键为age的值
        print (ghoobo1["age"])
        # 输出完整的字典
        print (ghoobo1)
        # 输出完整的字典
        print (ghoobo2)
        # 输出所有键
        print (ghoobo2.keys())
        # 输出所有值
        print (ghoobo2.values())