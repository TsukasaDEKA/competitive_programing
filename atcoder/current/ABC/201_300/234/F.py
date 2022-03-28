import sys
from io import StringIO
from typing import Pattern
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
        input = """aab"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """aaa"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """abcdefghijklmnopqrstuvwxyz"""
        output = """149621752"""
        self.assertIO(input, output)

def resolve():
  # 0 ~ N までの二項係数テーブルを作る。
  # O(N**2) の計算量がかかる点に注意する。
  class Binomial:
    def __init__(self, n, mod):
      self.binomial = [[0]*(n+1) for _ in range(n+1)]
    
      for i in range(n+1):
        for j in range(i+1):
          if j > i: break
          if i == 0 or j == 0:
            self.binomial[i][j] = 1
            continue
          self.binomial[i][j] = (self.binomial[i-1][j-1] + self.binomial[i-1][j]) % mod

    def get(self, n, r):
      return self.binomial[n][r]

  mod = 998244353
  alpha2num = lambda c: ord(c) - ord('a')

  S = list(input())
  N = len(S)
  agg = [0]*26
  for i in range(N):
    agg[alpha2num(S[i])]+=1
  
  binomial = Binomial(N, mod)
  dp = [[0]*(N+1) for _ in range(27)]
  dp[0][0] = 1
  ans = 0
  for i in range(26):
    # 最終的に j 文字になる時、i 文字目を k 文字使う場合の組合せ数。
    for j in range(N+1):
      for k in range(min(j, agg[i])+1):
        dp[i+1][j] += dp[i][j-k]*binomial.get(j, k)
        if dp[i+1][j] >= mod: dp[i+1][j]%=mod

  ans = sum(dp[-1][1:])%mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()