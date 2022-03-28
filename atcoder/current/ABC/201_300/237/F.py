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
        input = """4 5"""
        output = """135"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """111 3"""
        output = """144980434"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N, M = map(int, input().split(" "))

  dp = [[[0]*(M+1) for _ in range(N)] ]
  for i in range(1, M+1):
    dp[0][i] = 1


  print()

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