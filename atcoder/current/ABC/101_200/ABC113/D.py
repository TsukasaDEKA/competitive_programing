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
        input = """1 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2 3 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """7 1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_6(self):
        input = """15 8 5"""
        output = """437760187"""
        self.assertIO(input, output)

def resolve():
  mod = 1000000007 
  # dp でいけそう。
  # 少なくとも全ての縦棒の間に 1 本以上の横棒を入れる必要がある。=> 違う！
  # 跨ぐことはできない。
  H, W, K = map(int, input().split(" "))

  if W == 1 or W == 2:
    print(1)
    return

  dp = [[0]*W for _ in range(H+1)]
  dp[0][0] = 1
  for i in range(1, H+1):
    for bit in range(1<<(W-1)):
      # 横棒二連続のケースを除外する。
      if f'{bit:0b}'.find("11") >= 0: continue

      for j in range(W):
        # 左右から遷移してくるケース
        if bit&(1<<j):
          dp[i][j] += dp[i-1][j+1]
          dp[i][j+1] += dp[i-1][j]

        # 縦棒の左右に横棒が無いケース
        if bit&(1<<j) == 0 and bit&(1<<(max(0, j-1))) == 0:
          dp[i][j] += dp[i-1][j]
        dp[i][j ]%= mod

  print((dp[-1][K-1])%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()