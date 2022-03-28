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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)

def resolve():
  mod = 10**9+7
  N, M = map(int, input().split(" "))
  A = set([int(input()) for _ in range(M)])
  dp = [0]*(N+1)
  dp[0] = 1
  if 1 not in A:
    dp[1] = 1
  for i in range(2, N+1):
    if i not in A:
      dp[i] = (dp[i-1]+dp[i-2])%mod
    
  print(dp[-1])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()