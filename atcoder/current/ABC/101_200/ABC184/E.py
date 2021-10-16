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
        input = """2 5
S.b.b
a.a.G"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """11 11
S##...#c...
...#d.#.#..
..........#
.#....#...#
#.....bc...
#.##......#
.......c..#
..#........
a..........
d..#...a...
.#........G"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11 11
.#.#.e#a...
.b..##..#..
#....#.#..#
.#dd..#..#.
....#...#e.
c#.#a....#.
.....#..#.e
.#....#b.#.
.#...#..#..
......#c#G.
#..S...#..."""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  from collections import defaultdict, deque
  H, W = map(int, input().split(" "))
  FIELD = [list(input())+["#"] for _ in range(H)]+[["#"]*(W+1)]
  TELEPORTER = defaultdict(set)

  # 最初にマップを確認する。
  for h in range(H):
    FIELD_h = FIELD[h]
    for w in range(W):
      if FIELD_h[w] == "S":
        start = [h, w]
        continue
      if FIELD_h[w] == "G":
        continue
      if FIELD_h[w] != "." and FIELD_h[w] != "#":
        TELEPORTER[FIELD_h[w]].add((h, w))
  
  STEP = [[-1]*W for _ in range(H)]
  STEP[start[0]][start[1]] = 0
  nexts = deque()
  nexts.append(start)
  while nexts:
    temp_next = set()
    h, w = nexts.popleft()
    if FIELD[h][w] in TELEPORTER:
      remove = []
      for h_, w_ in TELEPORTER[FIELD[h][w]]:
        remove.append((h_, w_))
        if STEP[h_][w_] < 0:
          temp_next.add((h_, w_))
          STEP[h_][w_] = STEP[h][w]+1

      for h_, w_ in remove:
        TELEPORTER[FIELD[h_][w_]].remove((h_, w_))
        FIELD[h_][w_] = "."

    for i in range(4):
      h_ = h + dh[i]
      w_ = w + dw[i]
      if FIELD[h_][w_] == "G":
        print(STEP[h][w]+1)
        return
      if FIELD[h_][w_] == "#": continue
      if (h_, w_) in temp_next: continue
      if STEP[h_][w_] >= 0: continue
      temp_next.add((h_, w_))
      STEP[h_][w_] = STEP[h][w]+1

      if (h_, w_) in TELEPORTER[FIELD[h_][w_]]:
        TELEPORTER[FIELD[h_][w_]].remove((h_, w_))

    for h, w in temp_next:
      nexts.append((h, w))

  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()