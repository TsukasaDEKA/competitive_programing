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
        input = """9"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """999999999989449206"""
    #     output = """1000000000000000000"""
    #     self.assertIO(input, output)

def resolve():
  inf = 10**20+1
  N = int(input())

  # メグル式二分探索。
  def binary_search(ok, ng, solve, a):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, a): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, a) else -1
  

  def solve(b, a):
    return a**3 + (a**2)*b + a*(b**2) + b**3 >= N

  ans = inf
  for a in range((10**6)+1):
    b = binary_search((10**6)+1, -1, solve, a)
    if b == -1: continue
    ans = min(ans, a**3 + (a**2)*b + a*(b**2) + b**3)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()