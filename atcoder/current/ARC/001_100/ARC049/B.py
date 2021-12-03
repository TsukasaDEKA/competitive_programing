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
#         self.assertIO(input, output)

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
  # N が少なめなので、x, y をそれぞれ三分探索しても間に合いそう。
  # 一点に集まる際、座標は明らかに集合の内側に入る。
  # 極が一個しかないかどうかが保証できないっポイんだけど一応試してみる。
  inf = 10**18+1
  N = int(input())
  POINTS = [[int(x) for x in input().split(" ")] for _ in range(N)]
  # x について時間最小になる点を三分探索で求める。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 10**(-7):
      mid = (ok+ng)/2
      if solve(mid): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok) else -1
  
  def solve(t):
    # POINTS[i], POINTS[j] が共通範囲を持つかどうか。
    for i in range(N-1):
      x_i, y_i, c_i = POINTS[i]
      d_i = t/c_i
      x_i_l, x_i_r  = x_i-d_i, x_i+d_i
      y_i_l, y_i_r  = y_i-d_i, y_i+d_i
      for j in range(i+1, N):
        x_j, y_j, c_j = POINTS[j]
        d_j = t/c_j
        x_j_l, x_j_r  = x_j-d_j, x_j+d_j
        if x_i_l > x_j_r or x_j_l > x_i_r: return False
        y_j_l, y_j_r  = y_j-d_j, y_j+d_j
        if y_i_l > y_j_r or y_j_l > y_i_r: return False
    return True

  print(binary_search(inf, 0, solve))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()