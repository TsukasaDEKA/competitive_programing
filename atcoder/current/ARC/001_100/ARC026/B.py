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

    def test_入力例1(self):
        input = """6"""
        output = """Perfect"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """24"""
        output = """Abundant"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """27"""
        output = """Deficient"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """945"""
        output = """Abundant"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """10000000000"""
        output = """Abundant"""
        self.assertIO(input, output)

    def test_入力例6(self):
        input = """1"""
        output = """Deficient"""
        self.assertIO(input, output)

def resolve():
  # 約数列挙する過程で足していく。
  # N が大きい時しんどい気がする。
  N = int(input())

  if N == 1:
    print("Deficient")
    return

  dist = 1
  for i in range(2, int(-(-N**0.5//1))):
    if N%i==0:
      dist+=i
      if i != N//i: dist += N//i

  if dist == N:
    print("Perfect")
  elif dist > N:
    print("Abundant")
  else:
    print("Deficient")

resolve()

if __name__ == "__main__":
    unittest.main()
