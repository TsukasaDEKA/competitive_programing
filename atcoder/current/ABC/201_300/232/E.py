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
        input = """2 2 2
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000000 1000000000 1000000
1000000000 1000000000 1000000000 1000000000"""
        output = """24922282"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 3 3
1 3 3 3"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  # シミュレーションしてたら間に合わない。
  # K は 10**6
  # 一手前は X_2, Y_2 のどちらかが一致している必要がある。
  # 配る DP
  mod = 998244353
  inf = 10**18+1
  H, W, K = map(int, input().split(" "))
  H_1, W_1, H_2, W_2 = [int(x)-1 for x in input().split(" ")]
  dp = [[0]*4 for _ in range(K+1)]
  if H_1 == H_2 and W_1 == W_2: dp[0][0] = 1
  elif H_1 == H_2: dp[0][2] = 1
  elif W_1 == W_2: dp[0][1] = 1
  else: dp[0][3] = 1

  for i in range(1, K+1):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2])%mod
    dp[i][1] = ((H-1)*dp[i-1][0] + (H-2)*dp[i-1][1] + dp[i-1][3])%mod
    dp[i][2] = ((W-1)*dp[i-1][0] + (W-2)*dp[i-1][2] + dp[i-1][3])%mod
    dp[i][3] = ((W-1)*dp[i-1][1] + (H-1)*dp[i-1][2] + ((H-2)+(W-2))*dp[i-1][3])%mod

  print(dp[-1][0])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()