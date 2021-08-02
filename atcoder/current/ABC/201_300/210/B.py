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
00101"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
010"""
        output = """Aoki"""
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
  N = int(input())
  S = list(input())

  for i in range(N):
    if S[i] == "1":
      if i%2:
        print("Aoki")
      else:
        print("Takahashi")
      return 

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()