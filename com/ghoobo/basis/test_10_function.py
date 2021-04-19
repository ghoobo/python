import unittest

class test_function(unittest.TestCase):

    # 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    def change(self,a):
        print(id(a))  # 指向的是同一个对象
        a = 10
        print(id(a))  # 一个新对象

    # 形参和实参指向的是同一个对象（对象id相同），在函数内部修改形参后，形参指向的是不同的id
    def test_immutable(self):
        a = 1
        print(id(a))
        self.change(a)

    # 可写函数说明
    def changeme(self,mylist):
        "修改传入的列表"
        mylist.append([1, 2, 3, 4])
        print("函数内取值: ", mylist)
        return

    def test_mutable(self):
        # 调用changeme函数
        mylist = [10, 20, 30]
        self.changeme(mylist)
        print("函数外取值: ", mylist)

    # age不传值时默认为35
    def printinfo01(self, name, sex, age=35):
        "打印任何传入的字符串"
        print("名字: ", name)
        print("年龄: ", age)
        print("性别: ", sex)
        return

    def test_params01(self):
        # 不传age参数值，自定义参数顺序
        self.printinfo01(sex="男", name="guohb")
        print("------------------------")
        # 覆盖age默认值
        self.printinfo01("guohb", "男", age=23)

    # 不定长参数 加了星号*的参数会以元组(tuple)的形式导入
    def printinfo02(self, arg1, *vartuple):
        "打印任何传入的参数"
        print("输出: ")
        print(arg1)
        print(vartuple)

    def test_params02(self):
        # 调用printinfo 函数
        self.printinfo02(70, 60, 50)

    # 不定长参数 加了两个星号**的参数会以字典的形式导入。
    def printinfo03(self, arg1, **vardict):
        "打印任何传入的参数"
        print("输出: ")
        print(arg1)
        print(vardict)

    def test_params03(self):
        # 调用printinfo 函数
        self.printinfo03(1, a=2, b=3)

    def printinfo04(self, name, sex, *, age):
        "打印任何传入的字符串"
        print("名字: ", name)
        print("年龄: ", age)
        print("性别: ", sex)
        return

    # 强制位置参数
    def printinfo05(self, a, b, /, c, d, *, e, f):
        "形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参"
        print(a, b, c, d, e, f)

    def test_params05(self):
        self.printinfo05(10, 20, 30, d=40, e=50, f=60)

    # 如果单独出现星号 * 后的参数必须用关键字传入。
    def test_params04(self):
        self.printinfo04("guohb", "男", age = 23)

    sum = lambda self, arg1, arg2 : arg1 + arg2

    def test_lambda(self):
        print(self.sum(1, 2))