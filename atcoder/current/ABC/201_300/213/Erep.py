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
        input = """5 5
..#..
#.#.#
##.##
#.#.#
..#.."""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 7
.......
######.
.......
.######
......."""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 8
.#######
########
########
########
########
########
########
#######."""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  from collections import deque

  # BFS をいい感じにやっていく。
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  S = [list(input())+["_"] for _ in range(H)]+[["_"]*(W+1)]
  steps = [[-1]*W for _ in range(H)]
  steps[0][0] = 0

  nexts = deque()
  nexts.append((0, 0))
  walls = set()
  while nexts:
    h, w = nexts.popleft()
    step = steps[h][w]

    for i in range(4):
      h_, w_ = h+dh[i], w+dw[i]

      if S[h_][w_] == "_": continue
      if steps[h_][w_] >= 0: continue
      if S[h_][w_] == "#":
        walls.add((h_, w_))
        continue
      nexts.append((h_, w_))
      steps[h_][w_] = step

    if nexts: continue

    for h, w in walls:
      nexts.append((h, w))
      steps[h][w] = step+1
      for h_ in range(h-1, h+2):
        for w_ in range(w-1, w+2):
          if S[h_][w_] == "_": continue
          S[h_][w_] = "."
    walls = set()
  
  print(steps[-1][-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()