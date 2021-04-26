import unittest

class test_file(unittest.TestCase):

    def test_write01(self):
        file01 = open("file01.txt", "w", encoding='utf-8')
        num = file01.write( "第一行 \n 第二行" )
        print(num)
        file01.close()

    def test_write02(self):
        file02 = open("file02.txt", "rb+")
        file02.write( b"ancasgsdgdfkgktwelwklkerkgkjgksljr" )
        # 移动到文件的第六个字节
        file02.seek(5)
        str01 = file02.read(1)
        print(str01)
        # 移动到文件的倒数第三字节
        file02.seek(-3, 2)
        str02 = file02.read(1)
        print(str02)
        file02.close()

    def test_read01(self):
        file01 = open("file01.txt", "r", encoding='utf-8')
        str01 = file01.read()
        print(str01)
        file01.close()

    def test_read02(self):
        file02 = open("file01.txt", "r", encoding='utf-8')
        str02 = file02.readline()
        print(str02)
        file02.close()

    def test_read03(self):
        file03 = open("file01.txt", "r", encoding='utf-8')
        str03 = file03.readlines()
        print(str03)
        file03.close()

    def test_read04(self):
        file04 = open("file01.txt", "r", encoding='utf-8')
        for line in file04:
            print(line, end='')
        file04.close()