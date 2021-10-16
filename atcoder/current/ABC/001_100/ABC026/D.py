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
        input = """1 1 1"""
        output = """100.0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """53 82 49"""
        output = """1.63372043395339"""
        self.assertIO(input, output)

def resolve():
  # 三分探索かな。
  # 局地が複数あるので実装が難しそう。
  # B*sin(C*pi*t) は -B ~ B の範囲で動く。
  # A をざっくり合わせて 10**(-6) 刻みくらいで探索したら良さそう。
  # メグル式二分探索。

  def binary_search(ok, ng, solve, A, B, C):
    mid = (ok+ng)/2
    while abs(100.0-(A*mid + B*sin(C*pi*mid))) > 10**(-6):
      mid = (ok+ng)/2
      if solve(A, B, C, mid): ok = mid
      else: ng = mid

    return mid

  def solve(A, B, C, t):
    return A*t + B*sin(C*pi*t) <= 100

  from math import sin, pi
  A, B, C = map(int, input().split(" "))

  print(binary_search(0, 200, solve, A, B, C))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()