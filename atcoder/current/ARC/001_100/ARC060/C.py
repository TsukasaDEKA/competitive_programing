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
        input = """4 8
7 9 8 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 8
6 6 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 5
3 6 2 8 7 6 5 9"""
        output = """19"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """33 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3"""
        output = """8589934591"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 三次元 DP で解けるかも。
  # dp[i][j][k] := i 番目より前のカードを使って j 枚のカードを使って合計を k にできる通り数。
  # 単純に全部やると計算量が多すぎになりそうだけど、A を先に集計してまとめて実行することで行ける？
  inf = 10**18+1
  N, A = map(int, input().split(" "))
  X = sorted([int(x) for x in input().split(" ")])
  dp = [[[0]*(N*A+100) for _ in range(N+1)] for _ in range(N)]
  dp[0][0][0] = 1
  dp[0][1][X[0]] = 1

  for i in range(1, N):
    x = X[i]
    for j in range(i+1): # j = 枚数
      for k in range(N*A+1): # k = 合計値
        if dp[i-1][j][k]:
          dp[i][j][k] += dp[i-1][j][k]

          if k+x > N*A: continue
          dp[i][j+1][k+x] += dp[i-1][j][k]


  ans = 0
  for j in range(1, N+1):
    ans += dp[-1][j][j*A]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()