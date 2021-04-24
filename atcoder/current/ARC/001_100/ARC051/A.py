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
        input = """-1 -1 2
2 3 4 5"""
        output = """YES
YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """0 1 1
-2 0 4 3"""
        output = """NO
YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 0 5
-2 -2 2 1"""
        output = """YES
NO"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """0 0 2
0 0 4 4"""
        output = """YES
YES"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """0 0 5
-4 -4 4 4"""
        output = """YES
YES"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt
  X1, Y1, R = map(int, input().split(" "))
  X2, Y2, X3, Y3, = map(int, input().split(" "))
  # 原点ずらし
  X2-=X1
  X3-=X1
  Y2-=Y1
  Y3-=Y1
  red_exist = X2 > -R or X3 < R or Y2 > -R or Y3 < R
  brue_exist = sqrt(X2**2+Y2**2) > R or sqrt(X2**2+Y3**2) > R or sqrt(X3**2+Y2**2) > R or sqrt(X3**2+Y3**2) > R 
  print("YES" if red_exist else "NO",  "YES" if brue_exist else "NO", sep="\n")

resolve()

if __name__ == "__main__":
    unittest.main()
