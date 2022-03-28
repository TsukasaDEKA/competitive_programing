from os import sep
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
        input = """3
2 1
3 1"""
        output = """1 2
2 2
1 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
3 4
5 4
1 2
1 4"""
        output = """1 3
3 3
2 2
1 2
1 1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
4 5
3 2
5 2
3 1"""
        output = """1 1
1 1
1 1
1 1
1 1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18
  from collections import deque

  # DFS をして葉っぱに順位をつけていく。
  inf = 10**18+1
  N = int(input())
  EDGES = [[] for _ in range(N)]
  for _ in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)
    EDGES[B].append(A)

  ans = [(inf, 0)]*N
  leaf_count = 0
  nexts = deque()
  nexts.append(~0)
  nexts.append(0)
  cheched = [False]*N
  cheched[0] = True
  while nexts:
    current = nexts.pop()
    if current < 0:
      current = ~current
      L, R = inf, 0
      for n in EDGES[current]:
        l, r = ans[n]
        L = min(l, L)
        R = max(r, R)
      if L == inf:
        leaf_count+=1
        ans[current] = (leaf_count, leaf_count)
      else:
        ans[current] = (L, R)
      continue

    for n in EDGES[current]:
      if cheched[n]: continue
      cheched[n] = True
      nexts.append(~n)
      nexts.append(n)

  for a in ans:
    print(*a, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()