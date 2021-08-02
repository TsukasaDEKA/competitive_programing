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
        input = """2 3
.#.
..."""
        output = """First"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 4
....
...#
....
.#.."""
        output = """Second"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11 44
............................................
............................................
............................................
.....#.....#####....####.....####....####...
....#.#....#....#..#....#...#....#..#....#..
....#.#....#....#..#.............#..#....#..
...#####...#####...#..........###....####...
...#...#...#....#..#.............#..#....#..
..#.....#..#....#..#....#...#....#..#....#..
..#.....#..#....#...####.....####....####...
............................................"""
        output = """Second"""
        self.assertIO(input, output)

dh = [0, 1, 1]
dw = [1, 0, 1]

def resolve():
  # そのマスに止まれば勝てるマスを勝ちます、そうでないマスを負けマスとする。
  # 右下から順に見ていって、
  # 進行方向にあるマスの内、負けマスが 1 個でもある => 勝ちマス
  # 進行方向にマスがない => 負けマス
  # 進行方向にあるマスが全て勝ちマス => 負けマス
  # というように分類していく。
  # スタート地点のマスが勝ちマスであれば first を出力する。

  H, W = map(int, input().split(" "))
  F = [[1 if x=="." else 0 for x in list(input())] for _ in range(H)]
  ANS = [[1]*W for _ in range(H)]
  for h in reversed(range(H)):
    for w in reversed(range(W)):
      # 障害物ならスキップ
      if F[h][w]==0: continue
      for i in range(len(dh)):
        h_ = h+dh[i]
        w_ = w+dw[i]
        if h_ >= H or w_ >= W: continue
        if ANS[h_][w_]==0:
          ANS[h][w] = 1
          break
      else:
        ANS[h][w] = 0
  print("First" if ANS[0][0] else "Second")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()