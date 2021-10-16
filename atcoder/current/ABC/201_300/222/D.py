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
        input = """2
1 1
2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
2 2 2
2 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100"""
        output = """978222082"""
        self.assertIO(input, output)

def resolve():
  # 二乗オーダーでいける。
  # ai <= bi なのでパターンが 0 になることはない。

  mod = 998244353
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  B = [int(x) for x in input().split(" ")]
  range_ = max(B)+1

  dp = [[0]*range_ for _ in range(N)]
  for i in range(A[0], B[0]+1):
    dp[0][i] = 1

  for i in range(1, N):
    temp = 0
    for j in range(B[i]+1):
      temp+=dp[i-1][j]
      if temp >= mod: temp%=mod

      if j < A[i]: continue
      dp[i][j] = temp
      if dp[i][j] >= mod: dp[i][j]%=mod
  
  # print(*dp, sep="\n")
  print(sum(dp[-1])%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()