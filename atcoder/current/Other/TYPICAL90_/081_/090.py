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
        input = """2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """17 29"""
        output = """263173793"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2718 2818"""
        output = """393799986"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """28593 1"""
        output = """365728740"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """869120 1001"""
        output = """967393022"""
        self.assertIO(input, output)

def resolve():
  # K=1 の場合、連続した 1 は置けない。
  # 連続した二つの数字を置く場合、片方は K//2 以下である必要がある。
  mod = 998244353
  N, K = map(int, input().split(" "))
  if N>10**6: return
  dp = [[0]*(K+1) for _ in range(N)]
  for i in range(2):
    dp[0][i] = 1
  
  for i in range(1, N):
    for j in range(K+1):

    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]
    if dp[i][0] >= mod: dp[i][0]%=mod
    if dp[i][1] >= mod: dp[i][1]%=mod

  print(sum(dp[-1])%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()