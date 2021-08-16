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
        input = """4
1 2
4 2
3 1"""
        output = """1 2 4 2 1 3 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 2
1 3
1 4
1 5"""
        output = """1 2 1 3 1 4 1 5 1"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from heapq import heappop, heappush
  N = int(input())

  ROUTE = [[] for _ in range(N+1)]
  for i in range(N-1):
    A, B = [int(x) for x in input().split(" ")]
    heappush(ROUTE[A], B)
    heappush(ROUTE[B], A)
  
  for i in range(N):
    ROUTE[i].sort()

  # 深さ優先探索そのまま
  ans = [1]
  checked = [False]*(N+1)
  checked[1] = True
  nexts = deque()
  nexts.append(1)

  while nexts:
    current = nexts.pop()
    if current < 0:
      current *= -1
    
    # if len(ans) > 0:
      # if ans[-1] != current:
        # ans.append(current)
    if ans[-1] != current:
      ans.append(current)

    # ans.append(current)
    while ROUTE[current]:
      n = heappop(ROUTE[current])
      if checked[n]: continue
      checked[n] = True
      nexts.append(-current)
      nexts.append(-n)
      nexts.append(n)
      break
    else:
      if current == 1:
        break

  print(*ans)

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