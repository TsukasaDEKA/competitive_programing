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
        input = """5 1
2 4
2 -3
1 2
2 1
2 -3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 0
2 -1000000000"""
        output = """-1000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 3
2 3
2 -1
1 4
2 -1
2 5
2 -9
2 2
1 -6
2 5
2 -3"""
        output = """15"""
        self.assertIO(input, output)

def resolve():
  # ti = 1 の操作を行なった場合、それまでの操作は無効になる。
  # 最後に行なった ti = 1 の操作の x  以降の yi < 0 なオペレーションを最大 K 個無視する方向で考える。
  # 無視できる ti = 1 の個数も最大 K 個な点に注意する。
  # 使用する ti = 1 を決めてそれ以降の ti = 1 の操作を全て無視する。（K 個以上存在するならそれ以上計算しない。）
  # 後ろから見ていって、
  # ti = 1 の場合、無視するかどうか決める。
  inf = 10**18+1
  N = int(input())
  N, K = map(int, input().split(" "))
  A = [[int(x)+i, i-int(x)] for i, x in enumerate(input().split(" "))]
  A = [int(x) for x in input().split(" ")]
  A = [int(input()) for _ in range(N)]
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  S = list(input())
  S_map = [list(input()) for _ in range(H)]

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