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
        input = """4 2
2 5 2 5"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 4
9 1 8 2 7 5 6 4"""
        output = """32"""
        self.assertIO(input, output)

def resolve():
  # 全ての部分和を求める。500500 個できる。
  # 美しさは最大 40 桁になるので、40 桁目が 1 になる数字が K 個あるか調べて、もしあるなら
  # その桁を 1 にして・・・というのを繰り返す。
  # 微妙に間に合わなさそう？
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  candidate = []
  dp = [[0]*N for _ in range(N)]
  for i in range(N):
    dp[i][i] = A[i]

  max_a = 0
  for i in range(N-1):
    for j in range(i+1, N):
      dp[i][j] = dp[i][j-1]+A[j]
      candidate.append(dp[i][j])
      max_a = max(max_a, dp[i][j])

  ans = 0
  candidate_i = set(range(len(candidate)))
  bit_len = max_a.bit_length()
  for b in reversed(range(bit_len)):
    zeros = []
    one_count = 0
    for i in candidate_i:
      if (candidate[i]>>b)&1:
        one_count+=1
      else:
        zeros.append(i)

    if one_count>=K:
      ans+=1<<b
      for i in zeros: candidate_i.remove(i)

  print(ans)

import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()