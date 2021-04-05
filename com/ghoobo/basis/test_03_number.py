import unittest
import math
import random


class test_number(unittest.TestCase):

    def test_base8or16(self):
        # 十六进制
        number1 = 0xA0F
        # 八进制
        number2 = 0o37
        print(number1)
        print(number2)

    def test_datatype_conversion(self):
        a = 100
        print(a, type(a))
        b = float(a)
        print(b, type(b))
        c = int(b)
        print(c, type(c))
        d = 87.5
        print(d, type(d))
        f = int(d)
        print(f, type(f))

    def test_calculate(self):
        # 加减乘都一样
        a = 10
        b = 3
        # /跟java不一样，小数点后也有，返回类型为float
        c = a / b
        # //相当于java的/，只返回整数部分
        d = a // b
        # //返回类型不一定是整数，看a和b有float就也返回float
        e = 10.0 // 3
        # **为幂运算，a的b次方
        f = a ** b
        print(c, type(c))
        print(d, type(d))
        print(e, type(e))
        print(f, type(f))

    def test_final(self):
        pi = math.pi
        e = math.e
        print(pi)
        print(e)

    def test_math_function(self):
        # 返回数字的绝对值
        a = abs(-100)
        # 返回数字的绝对值,float类型？
        b = math.fabs(-100)
        # abs()是一个内置函数，而fabs()在math模块中定义的
        # fabs()函数只适用于float和integer类型，而abs()也适用于复数
        print(a)
        print(b)
        # 返回数字的上入整数
        c = math.ceil(5.3)
        d = math.ceil(-5.3)
        # 返回数字的下舍整数
        e = math.floor(5.3)
        f = math.floor(-5.3)
        print(c)
        print(d)
        print(e)
        print(f)
        # b和c比较，小于返回-1，等于返回0，大于返回1（原理：python中True=1，False=0）
        g = (c > d) - (c < d)
        print(g)
        # e的x次幂,如math.exp(1) 返回2.718281828459045
        print(math.exp(2))
        h = max(4,2,6,8)
        i = min(4,2,6,8)
        print(h)
        print(i)
        # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
        j = math.modf(2.4)
        k = math.modf(-2.4)
        print(j, type(j))
        print(k, type(k))
        # x的y次方，相当于x**y，返回类型不一样
        l = math.pow(3,2)
        print(l)
        # 四舍五入
        m = round(5.4)
        n = round(5.5)
        o = round(-5.4)
        p = round(-5.5)
        # 第二个参数表示保留到小数点后第几位
        q = round(5.52545,2)
        print(m)
        print(n)
        print(o)
        print(p)
        print(q)
        # 返回x的平方根
        r = math.sqrt(100)
        print(r)

    def test_random_function(self):
        # 从序列中随机获取一个元素
        a = range(10)
        b = random.choice(a)
        tuple = (0,1,2,3,4,5,6,7,8,9)
        c = random.choice(tuple)
        print(a, type(a))
        print(b)
        print(c)
        # 随机生成下一个实数，它在[0,1)范围内。
        e = random.random()
        print(e)
        # 随机生成下一个实数，它在[x,y]范围内。
        f = random.uniform(1, 2)
        print(f)
        # 将序列的所有元素随机排序,没有返回值，直接改变原序列，元组好像不行，list可以
        g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(g)
        print(g)

    def test_trigonometric_functions(self):
        # 将角度转换为弧度
        angle0 = math.radians(0)
        angle30 = math.radians(30)
        angle45 = math.radians(45)
        angle60 = math.radians(60)
        angle90 = math.radians(90)
        print(math.tan(angle45))
        print(math.sin(angle30))
        print(math.cos(angle60))