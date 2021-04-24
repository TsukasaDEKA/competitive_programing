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

    def test_入力例1(self):
        input = """3.0000"""
        output = """2.8708930019"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """0.0400"""
        output = """0.0400000000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1000000000000000000.0000"""
        output = """90.1855078128"""
        self.assertIO(input, output)

def resolve():
  from math import log2, log
  # ムーアの法則
  # t = x + P/( 2**(x/1.5) ) において、最小値 t を求めたい。
  # 傾きが 1 - (log(2)*P/1.5) * pow(2, (-x/1.5)) で求まるので、二分探索で頑張ってみる。
  P = float(input())
  A = (log(2)*P/1.5)
  def solve(x):
    t_ = 1 - A * pow(2, (-x/1.5))
    return t_ <= 0

  ok = 0.0
  ng = 180.0
  while abs(ok-ng) > 10**(-10):
    mid = (ok+ng)/2
    if solve(mid): ok = mid
    else: ng = mid

  ans = mid + P/(2**(mid/1.5))
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
