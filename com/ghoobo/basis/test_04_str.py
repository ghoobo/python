import unittest

class test_str(unittest.TestCase):

    def test_cut_str(self):
        str = "guohaobo is so handsome!"

        # 下标为1的字符
        a = str[1]
        print(a)
        # 截取下标为0-2的字符串，[0,2)
        b = str[0:2]
        print(b)
        # 从下标3开始到最后
        c = str[3:]
        print(c)
        # 从头开始到下标为8
        d = str[:8]
        print(d)
        # 运行会响一下，cmd中可以，编译器中不行
        print("\a")

    def test_str_operator(self):
        print("ghoobo" + " " + "is" + " " + "so" + " " + "handsome!")
        print("ghoobo" * 2)
        print("g" in "ghoobo")
        print("g" not in "ghoobo")
        # 原始字符串
        print(r"\n\r\a\t")
        # 字符串格式化
        print("我叫 %s 今年 %d 岁!" % ('guohaobo', 23))

    def test_f_string(self):
        name = 'guohaobo'
        age = 23
        print(f"我叫 {name} 今年 {age} 岁!")
        x = 1
        # python3.6
        print(f"{x+1}")
        # python3.8
        print(f"{x+1=}")

    def test_str_function(self):
        str = "guohaobo is so handsome!"
        # 将字符串的第一个字符转换为大写
        a = str.capitalize()
        print(a)
        # 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
        b = str.center(50, "f")
        print(b)
        # startWith True False
        c = str.startswith("g")
        print(c)
        # endWith True False
        d = str.endswith("e",0, 23)
        print(d)
        # indexOf 第一次出现下标，不存在返回-1
        e = str.find("q", 0, len(str))
        print(e)
        # 和上边方法一样，但是不存在报错
        f = str.index("o", 0, len(str))
        print(f)
        # 返回字符串长度
        g = len(str)
        print(g)
        # 全转换成大写
        h = str.upper()
        print(h)
        # 全转换成小写
        i = h.lower()
        print(i)
        # 分割字符串为列表,split()这个方法好像不能把字符串切成字符列表
        j = str.split(" ")
        print(j, type(j))
        # 返回"标题化"的字符串,就是说所有单词都是以大写开始
        k = str.title()
        print(k)