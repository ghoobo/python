import unittest
import math

class test_printAndInput(unittest.TestCase):

    def test_print01(self):
        s = 1/7
        # 函数返回一个用户易读的表达形式
        print(str(s))
        #  产生一个解释器易读的表达形式
        print(repr(s))


    def test_format(self):
        print("我的名字是{},今年{}岁了".format("guohb", "23"))
        print("我的名字是{1},今年{0}岁了".format("23", "guohb"))
        print("我的名字是{name},今年{age}岁了".format(age = "23", name = "guohb"))
        # ":.3f"保留3位小数
        print('常量 PI 的值近似为：{0:.3f}。'.format(math.pi))
        for x in range(1, 11):
            # {0:2d} {1:3d} {2:4d} 0指代format()方法中的第一个参数，1第二个，2第三个
            # 2d相当于>2d，表示右对齐，宽度为2，<3d表示左对齐，宽度为3，^4d表示中间对齐，宽度为4
            print('{0:2d} {1:<3d} {2:^4d}'.format(x, x * x, x * x * x))

    def test_input01(self):
        str = input("请输入：");
        print("你输入的内容是: ", str)
