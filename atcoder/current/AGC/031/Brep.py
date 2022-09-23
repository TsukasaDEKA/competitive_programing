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
1
2
1
2
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
4
2
5
4
2
4"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
1
3
1
2
3
3
2"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  mod = 10**9+7
  inf = 10**18+1
  N = int(input())
  C = [int(input()) for _ in range(N)]

  last = defaultdict(int)
  dp = [0]*N
  dp[0] = 1
  last[C[0]] = 0
  for i in range(1, N):
    if C[i] not in last or last[C[i]] >= i-1: dp[i] = dp[i-1]
    else: dp[i] = dp[i-1]+dp[last[C[i]]]
    if dp[i]>=mod: dp[i]%=mod
    last[C[i]] = i

  print(dp[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()