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
        input = """3
2 7 6"""
        output = """1
0
0
0
2
1
0
0
0
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
0 1 2 3 4"""
        output = """6
0
1
1
4
0
1
1
0
2"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  dp = [[0]*10 for _ in range(N)]
  dp[0][A[0]] = 1

  for i in range(1, N):
    for j in range(9+1):
      dp[i][(j+A[i])%10] += dp[i-1][j]
      if dp[i][(j+A[i])%10] >= mod: dp[i][(j+A[i])%10]%=mod
      dp[i][(j*A[i])%10] += dp[i-1][j]
      if dp[i][(j*A[i])%10] >= mod: dp[i][(j*A[i])%10]%=mod

  print(*dp[-1], sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()