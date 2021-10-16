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

    def test_Sample_Input_2(self):
        input = """4
ABBA"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_1(self):
        input = """4
BGBH"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIEIJEIJIJCGCCFGIEBIHFCGFBFAEJIEJAJJHHEBBBJJJGJJJCCCBAAADCEHIIFEHHBGF"""
        output = """330219020"""
        self.assertIO(input, output)

def debug_out(dp, kinds, N):
  for j in range(kinds):
    print(bin(j))
    for i in range(N):
      print(dp[i][j])

def resolve():
  alpha2num = lambda c: ord(c) - ord('A')

  mod = 998244353
  N = int(input())
  S = [alpha2num(x) for x in list(input())]

  # 種類数
  kinds = 10

  # dp[i][j][U] = i 番目までの文字を見た時に、
  # それまでの集合が U で最後に取った文字が j だった場合の組み合わせの数
  dp = [[[0]*(1<<kinds) for _ in range(kinds)] for _ in range(N)]
  for i in range(N):
    dp[i][S[i]][1<<S[i]] = 1

  for i in range(1, N):
    for U in range(1<<kinds):
      for j in range(kinds):
        # 取らなかった場合
        dp[i][j][U] += dp[i-1][j][U]
        dp[i][j][U]%=mod
        if S[i] == j:
          # 最後に取った文字が S[i] と等しかった場合
          dp[i][j][U]+=dp[i-1][j][U]
          dp[i][j][U]%=mod
        elif U&(1<<S[i]) == 0:
          # 最後に取った文字が S[i] と別で、かつ S[i] が U に含まれない場合
          dp[i][S[i]][U+(1<<S[i])] += dp[i-1][j][U]
          dp[i][S[i]][U+(1<<S[i])]%=mod

  ans = 0
  for j in range(kinds):
    for U in range(1<<kinds):
      ans += dp[-1][j][U]

  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()