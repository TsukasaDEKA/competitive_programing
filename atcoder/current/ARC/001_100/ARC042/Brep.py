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
        input = """0 0
4
100 100
-100 100
-100 -100
100 -100"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 10
3
0 100
-100 -100
100 -100"""
        output = """31.3049516850"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """34 6
7
-43 -65
-23 -99
54 -68
65 92
16 83
-18 43
-39 2"""
        output = """25.0284205314"""
        self.assertIO(input, output)


def resolve():
  from math import sqrt
  # 全ての辺までの最短距離を求める。
  inf = 10**18+1
  X, Y = map(int, input().split(" "))
  N = int(input())
  POS = [[int(x) for x in input().split(" ")] for _ in range(N)]
  ans = inf
  for i in range(N):
    x_0, y_0 = POS[i]
    x_1, y_1 = POS[i-1]
    val = abs((y_1-y_0)*X - (x_1-x_0)*Y - (y_1-y_0)*x_0 + (x_1-x_0)*y_0)/sqrt((y_1-y_0)**2 + (x_1-x_0)**2)
    # print(i, val)
    ans = min(ans, val)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()