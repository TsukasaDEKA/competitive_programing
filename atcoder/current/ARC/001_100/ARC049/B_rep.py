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
        input = """2
0 0 1
10 10 1"""
        output = """5.000000000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
0 0 1
10 10 2"""
        output = """6.666666666666667"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
-27 -67 10
59 13 10
14 -15 9
-29 -84 7
-75 -2 2
-12 -74 5
77 31 9
40 64 8
-81 32 1
81 26 5"""
        output = """582.222222222222222"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
-81739 73917 446
42230 30484 911
79354 -50126 200
33440 -47087 651
-73 84114 905
79222 -53608 713
65194 -46284 685
81145 40933 47"""
        output = """54924095.383189122374461"""
        self.assertIO(input, output)

def resolve():
  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 10**(-7):
      mid = (ok+ng)/2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1

  # 答えで二分探索
  inf = 10**18+1
  N = int(input())
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  def solve(ans):
    min_x, max_x = -inf, inf
    min_y, max_y = -inf, inf
    for i in range(N):
      x, y, c = A[i]
      step = ans/c
      min_x_, max_x_ = x - step, x + step
      min_y_, max_y_ = y - step, y + step
      if max_x_ < min_x or max_x < min_x_: return False
      if max_y_ < min_y or max_y < min_y_: return False
      min_x, max_x = max(min_x, min_x_), min(max_x, max_x_)
      min_y, max_y = max(min_y, min_y_), min(max_y, max_y_)

    return True

  print(binary_search(inf, 0, solve))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()