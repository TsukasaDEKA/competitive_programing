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
        input = """7 8 7
3 4
5 6
1 4
2 1
2 8
4 5
5 7
6 2
6 6"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 6 2
3 2
3 5
4 5
2 5"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 10 1
1 5
1 1
1 7"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left, bisect_right
  from collections import deque, defaultdict

  inf = 10**18+1
  # 障害物を行と列毎に集計する。
  # 移動する時に同一の行 or 列の障害物の中で最も近いものに止まることができる。
  # 移動可能なマスは障害物の周囲だけなので、N*4 個しかないので、BFS で解ける。
  H, W, N = map(int, input().split(" "))
  S = [int(x) for x in input().split(" ")]
  G_r, G_c = tuple([int(x) for x in input().split(" ")])
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(N)]

  ROW = defaultdict(list)
  COLUMN = defaultdict(list)
  for i in range(N):
    r, c = X_Y[i]
    ROW[r].append(c)
    COLUMN[c].append(r)

  for r in ROW.keys():
    ROW[r].sort()
  for c in COLUMN.keys():
    COLUMN[c].sort()

  # 訪れたマス
  step = defaultdict(int)
  nexts = deque()
  nexts.append((S[0], S[1]))
  while nexts:
    r, c = nexts.popleft()
    current_step = step[(r, c)]
    if r == G_r and c == G_c:
      print(step[(r, c)])
      return
    # 同じ行で移動できる先を探す。
    row = ROW[r]
    if len(row) > 0:
      index = bisect_left(row, c)
      if index == 0:
        c_ = row[index]-1
        if (r, c_) not in step and c_ >= 1:
          step[(r, c_)] = current_step+1
          nexts.append((r, c_))
      elif index == len(row):
        c_ = row[-1]+1
        if (r, c_) not in step and c_ <= W:
          step[(r, c_)] = current_step+1
          nexts.append((r, c_))
      else:
        c_ = row[index]-1
        if (r, c_) not in step and c_ >= 1:
          step[(r, c_)] = current_step+1
          nexts.append((r, c_))
        c_ = row[index-1]+1
        if (r, c_) not in step and c_ <= W:
          step[(r, c_)] = current_step+1
          nexts.append((r, c_))

    # 同じ列で移動できる先を探す。
    column = COLUMN[c]
    if len(column) > 0:
      index = bisect_left(column, r)
      if index == 0:
        r_ = column[index]-1
        if (r_, c) not in step and r_ >= 1:
          step[(r_, c)] = current_step+1
          nexts.append((r_, c))
      elif index == len(column):
        r_ = column[-1]+1
        if (r_, c) not in step and r_ <= H:
          step[(r_, c)] = current_step+1
          nexts.append((r_, c))
      else:
        r_ = column[index]-1
        if (r_, c) not in step and r_ >= 1:
          step[(r_, c)] = current_step+1
          nexts.append((r_, c))
        r_ = column[index-1]+1
        if (r_, c) not in step and r_ <= H:
          step[(r_, c)] = current_step+1
          nexts.append((r_, c))
  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()