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
1 3
1 5
3
2 2
3"""
        output = """3
7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
1 1000000000
2 1000000000
2 1000000000
2 1000000000
2 1000000000
3"""
        output = """5000000000"""
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
  from heapq import heappop, heappush
  Q = int(input())

  p_que = []
  add_sum = [0]*(Q+1)
  for i in range(Q):
    # T, X = map(int, input().split(" "))
    query = input().split(" ")
    if len(query) != 1:
      T, X = [int(x) for x in query]
      if T == 1:
        heappush(p_que, (X-add_sum[i], i))
      if T == 2:
        add_sum[i+1] = X
    else:
      x, j = heappop(p_que)
      print(x+add_sum[i])
    add_sum[i+1] += add_sum[i]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()