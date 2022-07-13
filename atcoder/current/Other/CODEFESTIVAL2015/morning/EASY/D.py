from email.policy import default
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
        input = """8
abacbabc"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8
abababab"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8
abababab"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """26
codefestivaltwozeroonefive"""
        output = """14"""
        self.assertIO(input, output)


def resolve():
  from collections import defaultdict

  # N がとても小さい。
  # 2**100 は無理。
  # 半全探索？
  # 2**50 は厳しそう。
  # 条件を満たす最長部分文字列
  # 切れ目を動かして最長部分文字列を求める。

  inf = 10**18+1
  N = int(input())
  S = list(input())
  ans = N
  for sep in range(1, N):
    dp = [[0]*(sep+1) for _ in range(N-sep+1)]
    for l in range(sep):
      for r in range(sep, N):
        dp[r-sep+1][l+1] = dp[r-sep][l] + 1 if S[l] == S[r] else max(dp[r-sep+1][l], dp[r-sep][l+1])

    ans = min(ans, N-2*dp[-1][-1])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()