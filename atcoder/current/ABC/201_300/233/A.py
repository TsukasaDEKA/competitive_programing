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
        input = """80 94"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000 63"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """270 750"""
        output = """48"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  X, Y = map(int, input().split(" "))
  print(max(0, (Y-X+9)//10))

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