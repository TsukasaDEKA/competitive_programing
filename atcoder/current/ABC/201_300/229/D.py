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
        input = """XX...X.X.X.
2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """XXXX
200000"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  # 区間和
  inf = 10**18+1
  S = list(input())
  K = int(input())
  N = len(S)
  sum_ = [0] + [1 if s == "." else 0 for s in S]  
  for i in range(1, N+1):
    sum_[i] += sum_[i-1]

  # メグル式二分探索。
  def binary_search(ok, ng, solve, l):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, l): ok = mid
      else: ng = mid

    return ok

  def solve(x, l):
    return sum_[x]-sum_[l] <= K

  ans = 0
  for l in range(N):
    r = binary_search(l, N+1, solve, l)
    ans = max(ans, r-l)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()