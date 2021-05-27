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

    def test_入力例_1(self):
        input = """3 3
1 1
3 3
..#
#.#
#.."""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
2 1
2 3
#.#
...
#.#"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 6
2 1
1 5
...#..
.#.##.
.#....
...##."""
        output = """5"""
        self.assertIO(input, output)


def resolve():
  # 方向の変換は 縦->横 or 横->縦 のどちらか以外は意味がない。
  # 縦横で分離して考える？
  # そう考えると Light と似たような処理でいけるかも。
  # 縦・横方向にグルーピング
  # 何個グループを跨いでいけるか考える。
  # それは BFS で行けそう。
  from collections import deque
  H, W = map(int, input().split(" "))
  Sh, Sw = [int(x)-1 for x in input().split(" ")]
  Gh, Gw = [int(x)-1 for x in input().split(" ")]
  MAZE = [[x=="." for x in list(input())] for _ in range(H)]

  index = 0
  row = [[None]*W for _ in range(H)]
  column = [[None]*W for _ in range(H)]
  # 横方向のグルーピング
  for h in range(H):
    for w in range(W):
      if not MAZE[h][w]:
        index+=1
        continue
      row[h][w] = index
    index+=1

  # 縦方向のグルーピング
  for w in range(W):
    for h in range(H):
      if not MAZE[h][w]:
        index+=1
        continue
      column[h][w] = index
    index+=1

  # グラフの構築
  edges = [set() for _ in range(index+1)]
  for h in range(H):
    row_h = row[h]
    column_h = column[h]
    MAZE_H = MAZE[h]
    for w in range(W):
      if not MAZE_H[w]: continue
      g1, g2 = row_h[w], column_h[w]
      edges[g1].add(g2)
      edges[g2].add(g1)
  
  step = [0]*(index+1)
  checked = [False]*(index+1)
  checked[row[Sh][Sw]] = checked[column[Sh][Sw]] = True
  nexts = deque()
  nexts.append(row[Sh][Sw])
  nexts.append(column[Sh][Sw])
  while nexts:
    current = nexts.popleft()
    if current == row[Gh][Gw] or current == column[Gh][Gw]:
      print(step[current])
      return
    for n in edges[current]:
      if checked[n]: continue
      checked[n] = True
      step[n] = step[current]+1
      if n == row[Gh][Gw] or n == column[Gh][Gw]:
        print(step[n])
        return
      nexts.append(n)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
