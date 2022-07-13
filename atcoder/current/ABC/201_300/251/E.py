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
        input = """5
2 5 3 2 5"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62"""
        output = """426"""
        self.assertIO(input, output)

def resolve():
  # 変形 DP っぽい
  # dp[i] := i 番目まで動物に餌をあげるために必要なコストの最小値
  # 初手は固定で 2 パターン考える。
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  dp = [0]*N
  dp[0], dp[1] = A[0], A[0]

  for i in range(1, N-1):
    dp[i+1] = min(dp[i-1], dp[i]) + A[i]
  dp[N-1] = min(dp[N-1], dp[N-2]+A[N-1])

  ans = dp[N-1]

  A = A[N-1:] + A[:N-1]
  dp = [0]*N
  dp[0], dp[1] = A[0], A[0]

  for i in range(1, N-1):
    dp[i+1] = min(dp[i-1], dp[i]) + A[i]
  dp[N-1] = min(dp[N-1], dp[N-2]+A[N-1])

  ans = min(ans, dp[N-1])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()