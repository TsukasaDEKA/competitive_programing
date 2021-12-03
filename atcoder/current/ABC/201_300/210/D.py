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
        input = """3 4 2
1 7 7 9
9 6 3 7
7 8 6 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 1000000000
1000000 1000000 1
1000000 1000000 1000000
1 1000000 1000000"""
        output = """1001000001"""
        self.assertIO(input, output)

def resolve():
  # (i, j) を終点だとすると、上から遷移してくる場合と左から遷移してくる場合しかない。
  # 終点は駅があっても線路を引くと考える。
  # 上と左が線路の時と始点の時で考えることが異なる。
  # 遷移してきた場所が始点の場合、A[i-1][j] か A[i][j-1] + C が (i, j) まで線路を引くコストになる。
  # 遷移してきた場所が線路の場合、そこまでのコストの最小値 + C が (i, j) まで線路を引くコストになる。
  # dp[i][j] = dp[i-1][j] or dp[i][j-1] から遷移してきたときの最小コストを解く
  # ↑ だと左上から右下への遷移しかわからないので困る。
  # 上下反転して同じことをする。
  inf = 10**30+1
  H, W, C = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")]+[inf] for _ in range(H)]+[[inf]*(W+1)]
  dp = [[0]*W+[inf] for _ in range(H)]+[[inf]*(W+1)]
  dp[0][0] = A[0][0]
  ans = inf
  for h in range(H):
    for w in range(W):
      if h == 0 and w == 0: continue
      dp[h][w] = min(A[h-1][w], dp[h-1][w], A[h][w-1], dp[h][w-1])+C
      ans = min(ans, dp[h][w]+A[h][w])

  # 上下反転
  dp = [[0]*W+[inf] for _ in range(H)]+[[inf]*(W+1)]
  dp[H-1][0] = A[H-1][0]
  for h in reversed(range(H)):
    for w in range(W):
      if h == H-1 and w == 0: continue
      dp[h][w] = min(A[h+1][w], dp[h+1][w], A[h][w-1], dp[h][w-1])+C
      ans = min(ans, dp[h][w]+A[h][w])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()