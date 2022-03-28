import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  from functools import reduce
  def lcm(x, y):
    return (x * y) // gcd(x, y)

  inf = 10**18+1
  # A 以上 B 以下の整数の個数 - C で割り切れるものの個数 - D で割り切れるものの個数 + C と D で割り切れるものの個数
  A, B, C, D = map(int, input().split(" "))
  # C で割り切れるものの個数
  C_ = B//C - (A-1)//C
  # D で割り切れるものの個数
  D_ = B//D - (A-1)//D
  # C と D で割り切れるものの個数
  l = lcm(C, D)
  C_D_ = B//(l) - (A-1)//(l)

  # print(C_, D_, C_D_)
  print((B-A+1)-C_-D_+C_D_)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()