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
        input = """2 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3"""
        output = """79"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """50 10000"""
        output = """77436607"""
        self.assertIO(input, output)

def resolve():
  # スコアはボールがインデックス上、遠い場所にある人のインデックスとボールの距離に等しい。
  # なのでスコアの上限は N-1 になることがわかる。
  # スコアが N-1 になる組み合わせは何通りあるのか考える。
  # i 番目の人のボールが i+1 番目の人のところにあって、かつ他の人のボールがそれより近い場合、スコアが N-1 になる。
  # その組み合わせを各人で試していく。
  # 全員の距離が 0 の時、スコアが 1 になる点に注意
  mod = 998244353
  N, K = map(int, input().split(" "))
  ans = 1
  for p in range(1, N-1):
    # ボールとの距離が p になる人を固定して、それ以外の人とボールとの距離が p 未満になる場合数を求める。
    # ボールとの距離の合計値は N の倍数になりそう。
    # 
    pattarn = 1
    for i in range(N):

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