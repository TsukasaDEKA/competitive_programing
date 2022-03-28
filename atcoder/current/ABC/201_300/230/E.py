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
        input = """3"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10000000000"""
        output = """231802823220"""
        self.assertIO(input, output)

def resolve():
  # メグル式二分探索。
  def binary_search(ok, ng, solve, N, tar):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, N, tar): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, N, tar) else -1

  def solve(i, N, tar):
    return N//i >= tar

  # N/i が v になる値で二分探索する。
  ans = 0
  N = int(input())
  l = 1
  while l <= N:
    v = N//l
    r = binary_search(l, N+1, solve, N, v)
    ans+= (r-l+1)*v
    l = r+1

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()