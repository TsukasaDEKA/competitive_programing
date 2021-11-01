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
        input = """3 3 7
1 1 4
1 2 7
2 1 3
2 3 5
3 1 2
3 2 5
3 3 5"""
        output = """1
0
2
0
3
1
0
4 7 0
3 0 5
2 5 5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 7 20
2 7 8
2 6 4
4 1 9
1 5 4
2 2 7
5 5 2
1 7 2
4 6 6
1 4 1
2 1 10
5 6 9
5 3 3
3 7 9
3 6 3
4 3 4
3 3 10
4 2 1
3 5 4
1 2 6
4 7 9"""
        output = """2
4
1
5
3
6
6
2
7
0
0
4
1
5
3
0
5
2
4
0"""
        self.assertIO(input, output)

def resolve():
  def binary_search(ok, ng, solve, x, target):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(x, target[mid][0]): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(x, target[ok][0]) else -1

  def solve(x, tar):
    return x > tar


  from heapq import heappop, heappush
  from collections import defaultdict
  # a の最小値から BFS していく。<= 最大から逆順で探った方が楽。
  # 普通にやったら最長にならない場合があるので、値の大きいものを優先的に選ぶようにする。=> heapq を使う
  inf = 10**10
  N = int(input())
  H, W, N = map(int, input().split(" "))
  NODES = [[int(x) for x in input().split(" ")] for _ in range(N)]
  # a が最小の点を開始点にする。
  # a が最大の点が複数あるかもしれない。
  max_a = 0
  # 縦と横で集計しておく。
  # 二分探索できるように、配列で集計しておく。
  rows = defaultdict(list)
  columns = defaultdict(list)
  for i in range(N):
    r, c, a = NODES[i]
    if max_a < a: max_a = a
    rows[r].append((a, i))
    columns[c].append((a, i))
  
  # 二分探索用にソート
  for key in rows.keys(): rows[key].sort(reverse=True)
  for key in columns.keys(): columns[key].sort(reverse=True)

  # a が最大の点を探す。<= 連結だとは限らない。
  nexts = []
  for i in range(N):
    if NODES[i][2] == max_a:
      heappush(nexts, (-a, i))

  sorted_nodes = sorted([(x[2], i) for i, x in enumerate(NODES)])
  print(sorted_nodes)

  depth = [0]*N
  checked = [False]*N
  while nexts:
    a, i = heappop(nexts)
    a*=-1
    r, c, _ = NODES[i]
    tar = set()
    c_index = binary_search(0, len(columns[c]), a, columns[c])
    if c_index >= 0:
      for _, j in columns[c][:c_index+1]:
        if checked[j]: continue
        checked[j] = True
        tar.add(j)
    r_index = binary_search(0, len(rows[r]), a, rows[r])
    if r_index >= 0:
      for _, j in rows[c][:r_index+1]:
        if checked[j]: continue
        checked[j] = True
        tar.add(j)

    for j in tar:
      _, _, a_ = NODES[j]
      depth[j] = depth[i]+1
      heappush((a_, j))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()