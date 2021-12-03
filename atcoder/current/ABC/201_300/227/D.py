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
        input = """3 3
2 3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 2
1 1 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 3
1 1 3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 2
1 2 3 8 9"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left

  inf = 10**30+1
  # メグル式二分探索。
  def binary_search(ok, ng, solve, A, K):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, A, K): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, A, K) else -1

  def solve(x, proj, sum_):
    for p in proj:
      sum_ -= max(0, x-p)
    return sum_ >= 0

  N, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])
  proj = A[N-K:]
  sum_ = sum(A[:N-K])
  ok = 1
  ng = inf

  print(binary_search(ok, ng, solve, proj, sum_))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()