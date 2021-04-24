import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """7"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """149696127901"""
        output = """27217477801"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """17"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
  from math import ceil
  # 好きな面から開始できるので、6, 5, 6, 5・・・の繰り返しができる。
  # X//11*2 + (X%11)//6 + floor((X%11)%6)・・・？
  X = int(input())
  print((X//11)*2 + ceil((X%11)/6))
resolve()

if __name__ == "__main__":
    unittest.main()
