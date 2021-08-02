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
        input = """12"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100128"""
        output = """447"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  def solve(x):
    return x*(x+1)//2 >= N

  ok = 10**9
  ng = 0

  print(binary_search(ok, ng, solve))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
