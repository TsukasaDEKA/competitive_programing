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
        input = """4 4
1 1
4 4
..#.
..#.
.#..
.#.."""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
1 4
4 1
.##.
####
####
.##."""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
2 2
3 3
....
....
....
...."""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 5
1 2
2 5
#.###
####.
#..##
#..##"""
        output = """2"""
        self.assertIO(input, output)


def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  from collections import deque

  # 変形 BFS
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  Ch, Cw = [int(x)-1 for x in input().split(" ")]
  Dh, Dw = [int(x)-1 for x in input().split(" ")]
  FIELD = [list(input())+["#"] for _ in range(H)] + [["#"]*(W+1)]
  ANS = [[-1]*(W+1) for _ in range(H+1)]

  nexts = deque()
  nexts.append((Ch, Cw))
  ANS[Ch][Cw] = step = 0

  while nexts:
    edges = set()
    while nexts:
      ch, cw = nexts.popleft()
      for i in range(4):
        h_ = ch + dh[i]
        w_ = cw + dw[i]
        if FIELD[h_][w_] == "#":
          edges.add((ch, cw))
          continue
        if ANS[h_][w_] != -1: continue
        ANS[h_][w_] = step
        nexts.append((h_, w_))
    step += 1
    temp = set()
    for ch, cw in edges:
      for h in range(max(ch-2, 0), min(ch+3, H)):
        for w in range(max(cw-2, 0), min(cw+3, W)):
          if ANS[h][w] != -1: continue
          if FIELD[h][w] == ".":
            temp.add((h, w))

    for ch, cw in temp:
      ANS[ch][cw] = step
      nexts.append((ch, cw))

  print(ANS[Dh][Dw])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()