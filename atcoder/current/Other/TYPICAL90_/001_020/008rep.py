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
        input = """10
attcordeer"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """41
btwogablwetwoiehocghiewobadegwhoihegnldir"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr"""
        output = """279999993"""
        self.assertIO(input, output)

def resolve():
  # dp[i][d] = i 文字目まで見た時に、atcoder の d 文字目までの文字列を作れる組み合わせ数
  from collections import defaultdict
  mod = 10**9+7

  atcoder = list("atcoder")
  a_to_i = defaultdict(lambda: -1)
  for i in range(7):
    a_to_i[atcoder[i]] = i

  _ = int(input())
  S = [a_to_i[x] for x in list(input()) if a_to_i[x] >= 0]
  N = len(S)
  dp = [[0]*7 for _ in range(N)]
  for i in range(N):
    if S[i] == 0:
      dp[i][0] = 1
    else:
      dp[i][S[i]] = dp[i-1][S[i]-1]

    for j in range(7):
      dp[i][j] += dp[i-1][j]
      if dp[i][j] >= mod: dp[i][j]%=mod

  print(dp[-1][-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()