import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """41 2
5 6"""
        output = """30"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import accumulate # 累積和作るやつ
import numpy as n
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def resolve():
  inf = 10**18+1
  N = int(input())
  N, K = map(int, input().split(" "))
  A = [[int(x)+i, i-int(x)] for i, x in enumerate(input().split(" "))]
  A = [int(x) for x in input().split(" ")]
  A = [int(input()) for _ in range(N)]
  A = [list(map(int, input().split(" "))) for _ in range(N)]
  S = list(input())
  S_map = [list(input()) for _ in range(H)]

  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()