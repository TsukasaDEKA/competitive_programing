import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """4 6
#..#..
.....#
....#.
#.#..."""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 8
..#...#.
....#...
##......
..###..#
...#..#.
##....#.
#...#...
###.#..#"""
        output = """13"""
        self.assertIO(input, output)

import numpy as np

def resolve():
  # 左から順に見ていって、障害物を見つけたら count を 0、そうでなければ count を +1 してそのマスに書き込む。
  # マスのカウントは「そのマスにランプを置いたときに照らせる左側の升目の数（ランプマス含む）」になる。
  # 同じように右から左、上から下、下から上に見ていって
  H, W = map(int, input().split(" "))
  GRID = [tuple(input()) for _ in range(H)]
  SUM = [[0]*W for _ in range(H)]
  ans = 0
  range_H = range(H)
  range_W = range(W)
  for h in range_H:
    count = 0
    for w in range_W:
      if GRID[h][w]=="#": count=0
      else:
        count+=1
        SUM[h][w] += count

  for h in range_H:
    count = 0
    for w in range_W:
      if GRID[h][W-w-1]=="#": count=0
      else:
        count+=1
        SUM[h][W-w-1] += count

  for w in range_W:
    count = 0
    for h in range_H:
      if GRID[h][w]=="#": count=0
      else:
        count+=1
        SUM[h][w] += count

  for w in range_W:
    count = 0
    for h in range_H:
      if GRID[H-h-1][w]=="#": count=0
      else:
        count+=1
        SUM[H-h-1][w] += count
        ans = max(ans, SUM[H-h-1][w]-3)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
