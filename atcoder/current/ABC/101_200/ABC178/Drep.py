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
        input = """7"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)
    # def test_Sample_Input_2(self):
    #     input = """100"""
    #     output = """3"""
    #     self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1729"""
        output = """294867501"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ

  # 数列の長さは 700 未満。
  # DP でいけそう。計算量がやばそう。
  inf = 10**18+1
  mod = 10**9+7
  S = int(input())

  length = (S+2)//3
  dp = [[0]*(S+1) for _ in range(length)]
  for i in range(3, S+1):
    dp[0][i] = 1

  ans = dp[0][-1]
  for i in range(1, length):
    inte = list(accumulate(dp[i-1]))
    for n in range(3*(i+1), S+1):
      dp[i][n] = inte[n-3]
    ans+=dp[i][S]
    if ans>=mod: ans%=mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()