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
        input = """3 20
2 80
9 120
16 1"""
        output = """191"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 20
2 80
9 1
16 120"""
        output = """192"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 100000000000000
50000000000000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """15 10000000000
400000000 1000000000
800000000 1000000000
1900000000 1000000000
2400000000 1000000000
2900000000 1000000000
3300000000 1000000000
3700000000 1000000000
3800000000 1000000000
4000000000 1000000000
4100000000 1000000000
5200000000 1000000000
6600000000 1000000000
8000000000 1000000000
9300000000 1000000000
9700000000 1000000000"""
        output = """6500000000"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ
  # カウンターをスタート地点で切り開いて考える。
  # ~~左のみのパターン、左を往復して右をとるパターン、右だけをとるパターン、右を往復して左をとるパターンの 4 種類~~ をそれぞれ計算して最大値をとる。
  # 実質、右を往復して左をとるパターンと、左を往復して右をとるパターンの 2 種類を考えれば良い。
  # 左からとってくパターンでそこまでみた時の接種カロリーの差し引き最大値、往復分の消費カロリーを計算し、
  # 右からとってくパターンでそこまでみた時の接種カロリーの差し引き最大値、往復分の消費カロリーを計算し、
  # 左のみのパターン、左を往復して右をとるパターン、右だけをとるパターン、右を往復して左をとるパターンの最大値を比較しながら計算する。
  inf = 10**18+1
  N, C = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]

  DISTANCE = [0]+[x for x, _ in A]
  CAL = [v for _, v in A]
  INTE_CAL = [0]+list(accumulate(CAL))

  from_left = [[0]*(N+1) for _ in range(2)]
  from_right = [[0]*(N+1) for _ in range(2)]

  ans = 0
  for i in range(N):
    from_left[0][i+1] = max(from_left[0][i], INTE_CAL[i+1] - DISTANCE[i+1])
    from_left[1][i+1] = max(from_left[1][i], INTE_CAL[i+1] - 2*DISTANCE[i+1])

  for i in reversed(range(N)):
    from_right[0][i] = max(from_right[0][(i+1)%N], INTE_CAL[-1] - INTE_CAL[i] - (C - DISTANCE[i+1]))
    from_right[1][i] = max(from_right[1][(i+1)%N], INTE_CAL[-1] - INTE_CAL[i] - 2*(C - DISTANCE[i+1]))

  ans = 0
  for i in range(N+1):
    ans = max(ans, from_left[0][i]+from_right[1][i], from_left[1][i]+from_right[0][i])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()