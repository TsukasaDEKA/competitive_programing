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
        input = """chchokudai"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """atcoderrr"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """chokudaichokudaichokudai"""
        output = """45"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
import numpy as np
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def resolve():
  from collections import defaultdict

  mod = 10**9+7
  S = list(input())
  chokudai = "chokudai"
  c_i = defaultdict(int)
  for i in range(len(chokudai)):
    c_i[chokudai[i]] = i

  # print(c_i)
  dp = [[0]*8 for _ in range(len(S))]
  if S[0] == "c":
    dp[0][0] = 1

  for i in range(1, len(S)):
    dp[i][0] = dp[i-1][0]
    if S[i] == "c":
      dp[i][0]+=1

  for i in range(1, len(S)):
    for j in range(1, 8):
      dp[i][j] = dp[i-1][j]
      if j == c_i[S[i]]:
        dp[i][j] += dp[i-1][j-1]
      

  # print(*dp, sep="\n")
  print(dp[-1][-1]%mod)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()