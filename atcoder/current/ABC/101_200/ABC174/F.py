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
        input = """4 3
1 2 1 3
1 3
2 4
3 3"""
        output = """2
3
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 10
2 5 6 5 2 1 7 9 7 2
5 5
2 4
6 7
2 2
7 8
7 9
1 8
6 9
8 10
6 8"""
        output = """1
2
2
1
2
2
6
3
3
3"""
        self.assertIO(input, output)

def resolve():
  # クエリ先読みして l, r それぞれでソートする。
  # 最も左側の r_0 をとってその r よりも左側の l の内、最も右側の l_i をとる。
  # l_i ~ r_0 の種類数を数えて記録。
  # 右側を動かして r_1 を見つけたらそこでストップ
  # r_0 ~ r_1 までの間にある l_[i+1:] を探して、
  # それぞれの l_[i+1:] と r_1 の組み合わせを記録していく。
  # 
  N, Q = map(int, input().split(" "))
  C = [int(x) for x in input().split(" ")]
  QUERY = [[int(x) for x in input().split(" ")] for _ in range(Q)]

  print(sorted(QUERY))

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