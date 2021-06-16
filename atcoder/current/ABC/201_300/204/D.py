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
8 3 7 2 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1000 1"""
        output = """1000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """9
3 14 15 9 26 5 35 89 79"""
        output = """138"""
        self.assertIO(input, output)

def resolve():
  # 二つに分割した時の和の差が最小になる組み合わせを考える。
  # DP で作成できる時間の和のパターンを出して、小さい方から総当たり。
  N = int(input())
  T = [int(x) for x in input().split(" ")]
  sum_T = sum(T)
  limit = sum_T
  # limit = 30
  dp = [[0]*(limit+1) for _ in range(N+1)]
  dp[0][0] = 1
  for i in range(1, N+1):
    for t in range(limit+1):
      if dp[i-1][t]:
        dp[i][t] = 1
        if t+T[i-1] <= limit:
          dp[i][t+T[i-1]] = 1
  
  last = dp[-1]
  for i in range((sum_T+1)//2, limit+1):
    if last[i]:
      print(i)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
