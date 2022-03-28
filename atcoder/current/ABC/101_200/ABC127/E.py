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
        input = """2 2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 5 4"""
        output = """87210"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 100 5000"""
        output = """817260251"""
        self.assertIO(input, output)

def resolve():
  def comb_mod(n,r,mod):
    if n-r<r:
      r=n-r
    N=n
    R=r
    u=1
    d=1
    for i in range(r):
      u*=N
      u%=mod
      N-=1
      d*=R
      d%=mod
      R-=1
    return u*pow(d,mod-2,mod)%mod
  # (xi, yi), (xj, yj) マスに駒を置く場合に発生するコストの考える。
  # (xi, yi), (xj, yj) マスに駒を置く事を決めて、他のマスに駒を置く場合数は
  # H*W-2 C K-2 になる。
  # つまり、(xi, yi), (xj, yj)間で発生するコストの総和は (abs(xi-xj) + abs(yi-yj)) * (H*W-2 C K-2) になる。
  # つまり、全ての配置コストの総和は全ての 2 マス間組み合わせで発生するコストに (H*W-2 C K-2) を掛けた値になる。
  # 次に任意の 2 マス間組み合わせで発生するコストの総和を高速に求める方法について考える。
  # (xi, yi) = (0, 0) を選び、(xj, yj) を (0, 0) 以外の任意のマス目だとすると、(0, 0) と (xj, yj) 間で発生するコストは線形時間で求められる。
  # これの累積和を持っておけば全ての (xi, yi) を選んだ時に発生するコストの総和を O(1) で求めることができる。
  mod = 10**9+7
  H, W, K = map(int, input().split(" "))
  # コストのテーブル
  cost = [[0]*(W+1) for _ in range(H+1)]
  for i in range(1, H+1):
    for j in range(1, W+1):
      cost[i][j] = cost[i-1][j] + cost[i][j-1] - cost[i-1][j-1] + (i+j-2)

  # 累積和を取るために左と上を 0 埋めしたけど、計算上邪魔なので削る。
  cost = [c[1:] for c in cost[1:]]

  ans = 0
  for i in range(H):
    h = H-i-1
    for j in range(W):
      w = W-j-1
      # 左上から順に見ていって、今まで見た事の無いマスとペアにする時、そのコストの総和は以下のようになる。
      # cost[h][w]: 行、列が今いるマス以上 (広義右下？) のマスとの間に発生するコスト
      # cost[h][w]: 行が今いるマス以上で列が今いるマス以下（広義左下？）のマスとの間に発生するコスト
      # cost[h][0]: 広義右下と広義左下の重複区間分のコスト。2 回足されていることになるので 1 回分引く
      # cost[0][j]: 広義左下に含まれる今まで見てきたマス分のコスト
      ans += cost[h][w] + cost[h][j] - cost[h][0] - cost[0][j]
      if ans >= mod: ans%=mod
  print((ans*comb_mod(H*W-2, K-2, mod))%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()