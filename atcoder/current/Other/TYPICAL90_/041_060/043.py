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
  # 方向の変換は 縦->横 or 横->縦 のどちらか
  # 縦横で分離して考えると良さそう。
  # 縦・横方向で方向転換をしないで移動できるマス目をグルーピングする。
  # 同じマスを共有しているグループ間の移動は可能と考えて、何個グループを跨いでゴールにいけるか考える。
  # 縦のグループ同士、横のグループ同士はマスを共有しないのでグループ間の移動 == 方向転換と考えて良い。
  # グループをノードと考えると BFS で行けそう。
  from collections import defaultdict
  H, W = map(int, input().split(" "))
  Sh, Sw = [int(x)-1 for x in input().split(" ")]
  Gh, Gw = [int(x)-1 for x in input().split(" ")]
  MAZE = [[x=="." for x in list(input())] for _ in range(H)]

  index = 0
  size = [0]*((H+100)*(W+100))
  row = [[-1]*W for _ in range(H)]
  column = [[-1]*W for _ in range(H)]
  # 横方向のグルーピング
  for h in range(H):
    for w in range(W):
      if not MAZE[h][w]:
        index+=1
        continue
      row[h][w] = index
      size[index]+=1
    else:
      index+=1

  # 縦方向のグルーピング
  for w in range(W):
    for h in range(H):
      if not MAZE[h][w]:
        index+=1
        continue
      column[h][w] = index
      size[index]+=1
    else:
      index+=1

  # グラフの構築
  edges = [[] for _ in range(index)]
  for h in range(H):
    row_h = row[h]
    column_h = column[h]
    MAZE_H = MAZE[h]
    for w in range(W):
      g1 = row_h[w]
      if g1 < 0: continue
      g2 = column_h[w]
      if size[g1] <= 1: continue
      if size[g2] <= 1: continue
      edges[g1].append(g2)
      edges[g2].append(g1)
  
  goals = set([row[Gh][Gw], column[Gh][Gw]])
  if row[Sh][Sw] in goals or column[Sh][Sw] in  goals:
    print(0)
    return

  count = 0
  checked = [False]*index
  checked[row[Sh][Sw]] = checked[column[Sh][Sw]] = True
  nexts = [row[Sh][Sw], column[Sh][Sw]]

  for count in range(1, index+1):
    temp_nexts = []
    for current in nexts:
      for n in edges[current]:
        if checked[n]: continue
        checked[n] = True
        if n in goals:
          print(count)
          return
        temp_nexts.append(n)
    nexts = temp_nexts

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
