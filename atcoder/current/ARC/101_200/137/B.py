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
        input = """4
0 1 1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
0 0 0 0 0"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
0 1 0 1 0 1"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  # 何通りあるかを求める。
  # シミュレーションしてたら間に合わない。
  # 「スコアとしてあり得る値」を求める。
  # 減ることもあり得る。
  # 得点の増減は 区間の幅 - <区間に含まれる 1 の個数>。
  # 累積和を上手く使う？
  # 区間に含まれる 1 の個数と 0 の個数が等しい時、得点は変化しない。
  # 割合のバリエーションが問題。
  # 左から 0 の個数 - 1 の個数を記録していく。
  # 左から見ていって最大値と最小値を記録していく
  # 最大値と最小値を記録していけば、取りうる得点の最大値と最小値がわかる。
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  agg = [0]*(N+1)
  for i in range(1, N+1):
    agg[i] = agg[i-1] + (1 if A[i-1]==0 else -1)

  max_ = [-inf]*(N+1)
  max_[0] = 0
  min_ = [inf]*(N+1)
  min_[0] = 0
  for i in range(1, N+1):
    max_[i] = max(max_[i-1], agg[i])
    min_[i] = min(min_[i-1], agg[i])

  top = -inf
  bottom = inf

  for i in range(N+1):
    top = max(top, agg[i] - min_[i])
    bottom = min(bottom, agg[i] - max_[i])

  # print(agg, max_, min_)
  # print(top, bottom)
  print(top-bottom+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()