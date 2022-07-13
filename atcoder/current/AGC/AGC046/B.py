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
        input = """1 1 2 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1 3 4"""
        output = """65"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """31 41 59 265"""
        output = """387222020"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # dp で行けそう。
  # dp[i][j] := 現在のマス目が i 行 j 列だった場合の塗り方の組み合わせ数。
  # 遷移が 2 パターンあって、dp[i-1][j] と dp[i][j-1] からの遷移
  # 組み合わせが重複するパターンがあり、
  # 重複するのは (i-1)*(j-1)*dp[i-1][j-1] 個
  # => 先に右に行って上に移動するパターンと上に行って右に行くパターンで同じ塗り方が発生する可能性があり、それを排除する。
  # 同じ塗り方はどちらの繊維でもマス i, j 以外を塗ったパターンなので、(i-1)*(j-1)。
  # また、そこに至るまでマス目 i-1, j-1 までの塗り方の通り数が dp[i-1][j-1] に入っているので、(i-1)*(j-1)*dp[i-1][j-1]
  mod = 998244353
  A, B, C, D = map(int, input().split(" "))

  dp = [[0]*(D+1) for _ in range(C+1)]
  dp[A][B] = 1
  for h in range(A, C+1):
    for w in range(B, D+1):
      dp[h][w] += w*dp[h-1][w] + h*dp[h][w-1] - ((h-1)*(w-1)*dp[h-1][w-1])%mod
      dp[h][w]%=mod

  # print(*dp, sep="\n", file=sys.stderr)
  print(dp[-1][-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()