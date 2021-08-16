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
  dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
  dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]
  from collections import deque
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  field = [[x == "." for x in list(input())] for _ in range(H)]

  
  ans = [[-1]*W for _ in range(H)]
  ans[0][0] == 0
  nexts = deque()
  nexts.append((0, 0))

  break_count = 0
  while ans[-1][-1] == -1:
    break_tar = set()
    while nexts:
      h, w = nexts.pop()
      for i in range(4):
        h_, w_ = h+dh[i], w+dw[i]
        if h_ < 0 or h_ >= H or w_ < 0 or w_ >= W: continue
        if ans[h_][w_] != -1: continue
        if field[h_][w_] == False:
          break_tar.add((h_, w_))
          continue
        ans[h_][w_] = break_count
        nexts.append((h_, w_))

    break_count += 1
    for h, w in break_tar:
      nexts.append((h, w))
      field[h][w] = True
      for i in range(8):
        h_, w_ = h+dh8[i], w+dw8[i]
        if h_ < 0 or h_ >= H or w_ < 0 or w_ >= W: continue
        field[h_][w_] = True

  print(ans[-1][-1])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()