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
        input = """4 5
s####
....#
#####
#...g"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g##.#.#.#.
###.#.#.#.
###.#.#.#.
#.....#..."""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6 6
.....s
###...
###...
######
...###
g.####"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """1 10
s..####..g"""
        output = """NO"""
        self.assertIO(input, output)



def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  from collections import deque

  # s から BFS して壁破壊 0 回で到達できるマスを見つけて、それに隣接している壁を記録していく。
  # 壁破壊 0 回で到達できるマスを調べ終わったら全ての壁を破壊してそこから BFS していく。
  # 壁破壊 2 回以内に g マスに到達できるのであれば YES、そうでないなら NO
  H, W = map(int, input().split(" "))
  FIELD = [list(input())+["#"] for _ in range(H)] + [["#"]*(W+1)]

  nexts = deque()
  checked = [[False]*W+[True] for _ in range(H)]+[[True]*(W+1)]
  g_h = g_w = None
  for h in range(H):
    for w in range(W):
      if FIELD[h][w] == "s":
        nexts.append((h, w))
        checked[h][w] = True
      if FIELD[h][w] == "g":
        g_h, g_w = h, w

  for i in range(3):
    target_wall = set()
    while nexts:
      h, w = nexts.popleft()
      for i in range(4):
        h_ = h+dh[i]
        w_ = w+dw[i]
        if checked[h_][w_]: continue
        checked[h_][w_] = True
        if FIELD[h_][w_] == "g":
          print("YES")
          return
        if FIELD[h_][w_] == "#":
          target_wall.add((h_, w_))
          continue
        nexts.append((h_, w_))
    for tar in target_wall:
      nexts.append(tar)
      checked[tar[0]][tar[1]] = True

  print("NO")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()