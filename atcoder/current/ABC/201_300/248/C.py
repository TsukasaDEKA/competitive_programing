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
        input = """2 3 4"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """31 41 592"""
        output = """798416518"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  input = sys.stdin.readline().rstrip
  N, M, K = map(int, input().split(" "))
  dp = [[0]*(K+1) for _ in range(N)]
  for i in range(1, M+1):
    dp[0][i] = 1

  for i in range(1, N):
    for j in range(1, M+1):
      for k in range(j+1, K+1):
        dp[i][k] += dp[i-1][k-j]
        if dp[i][k] >= mod: dp[i][k]%=mod

  # print(*dp, sep="\n", file=sys.stderr)
  print(sum(dp[-1])%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()