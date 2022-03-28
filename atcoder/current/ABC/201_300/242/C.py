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
        input = """4"""
        output = """203"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000"""
        output = """248860093"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N = int(input())
  # dp?
  dp = [[0]*11 for _ in range(N)]
  for i in range(1, 10):
    dp[0][i] = 1
  
  for i in range(1, N):
    for j in range(1, 10):
      dp[i][j] = dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1]
      if dp[i][j] >= mod: dp[i][j]%=mod
  print(sum(dp[-1])%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()