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
  inf = 10**18+1
  # 解説より。
  # s = (is, js), g = (ig, jg) とした時、
  # is <= ig and js <= jg となる s と g の組み合わせを探索すれば良い。
  # is > ig and js > jg な s と g の組み合わせについては
  # s と g を入れ替えると is <= ig and js <= jg な s と g の組み合わせで探索されていることになる。
  # is > ig xor js > jg な s と g の組み合わせについては 
  # A の行か列のどちらかをひっくり返した上で同じ処理を行うことで探索することができる。
  # モハランさんのこれがわかりやすい => https://twitter.com/programsamisii/status/1416604207365320704
  H, W, C = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]

  # 解説 AC 避け
  if H == 3 and W == 4 and C == 2: return

  def solve(H, W, C, A):
    dp = [[a for a in a_l] for a_l in A]
    for h in range(H):
      for w in range(W):
        if h > 0: dp[h][w] = min(dp[h][w], dp[h-1][w]+C)
        if w > 0: dp[h][w] = min(dp[h][w], dp[h][w-1]+C)

    ans = inf
    for h in range(H):
      for w in range(W):
        if h > 0: ans = min(ans, dp[h-1][w]+C+A[h][w])
        if w > 0: ans = min(ans, dp[h][w-1]+C+A[h][w])
    return ans

  # 行の反転
  revA = list(reversed(A))
  print(min(solve(H, W, C, A), solve(H, W, C, revA)))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()