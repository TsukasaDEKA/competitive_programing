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
        input = """3 998244353"""
        output = """26"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """2 998244353"""
    #     output = """0"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """5 998244353"""
    #     output = """2626"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """3000 924844033"""
    #     output = """607425699"""
    #     self.assertIO(input, output)

def resolve():
  # 2 個までは同じ長さ。
  # 同じ長さ or 伸びる文字列の個数を数える。
  # dp で解けそう
  # 長くなるパターンと短くなるパターンを考える必要がある。
  # 長くなるパターンはその文字が 1 文字である場合。
  # 短くなるパターンはその文字が 3 文字以上連続する場合。
  # 
  N, P = map(int, input().split(" "))
  mod = P
  ans = pow(26, N, mod)

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