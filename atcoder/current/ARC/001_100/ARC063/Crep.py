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
        input = """3 2
100 50 200"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 8
50 30 40 10 20"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 100
7 10 4 5 9 3 6 8 2 1"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
  from collections import defaultdict

  # 高橋君は購入箇所を 1 箇所、販売箇所を 1 箇所に定めて、そこで全てのりんごの売買を
  # 行うと最大の利益が得られる。
  # 購入箇所は販売箇所より先に訪れる必要がある。
  # 後ろから見ていって、今まで見た中での最大値 max_i を記録していく。
  # (max_i-Ai)*(T//2) が利益の最大値で、今回は 1 円だけ下げればいいだけなので (T//2) は無視する。
  # max_i-Ai を集計して、最大値の個数が答え
  # 前から見ていってもできそう。
  inf = 10**18+1
  N, T = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  min_A = [inf]*N
  min_A[0] = A[0]
  for i in range(1, N):
    min_A[i] = min(min_A[i-1], A[i])

  # 利益の個数を集計する。最大利益を覚えておく。
  agg_gain = defaultdict(int)
  max_gain = 0
  for i in range(N):
    g = A[i] - min_A[i]
    max_gain = max(max_gain, g)
    agg_gain[g]+=1
  print(agg_gain[max_gain])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()