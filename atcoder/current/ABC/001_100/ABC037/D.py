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
1 4 5
2 4 9"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 6
1 3 4 6 7 5
1 2 4 8 8 7
2 7 9 2 7 2
9 4 2 7 6 5
2 8 4 6 7 6
3 7 9 1 2 7"""
        output = """170"""
        self.assertIO(input, output)
dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]

def resolve():
  # 開始地点が決まってれば DFS で一発だけど、好きな升目から開始できるのが困る。
  # 升目の数は 10**6 程度まであるので O(1) で求めたい。
  # 閉路を持たない有向グラフ。
  # 開始点を一個定めると、その開始点からの移動経路数はその開始点から移動できる点の数 (自身も含める) になる。
  # 一旦全部見て回って、隣接点が全部自身より小さい点を探す。そこが開始点になる。
  # そこから BFS していく。
  # 単純に BFS すると合流点の計算がおかしくなるので、隣接点を見回して、
  # 自分より大きい数の隣接点が全て訪問済みの場合のみ、次の探索候補に加えるという処理にする。
  from collections import deque
  mod = 10**9+7
  H, W = map(int, input().split(" "))
  F = [[int(x) for x in input().split(" ")]+[0] for _ in range(H)]+[[0]*(W+1)]

  nexts = deque()
  for h in range(H):
    for w in range(W):
      for i in range(4):
        h_ = h+dh[i]
        w_ = w+dw[i]
        if F[h_][w_] > F[h][w]: break
      else:
        nexts.append((h, w))

  pattern = [[0]*(W+1) for _ in range(H+1)]
  while nexts:
    h, w = nexts.popleft()
    pattern[h][w]=1
    for i in range(4):
      h_ = h+dh[i]
      w_ = w+dw[i]
      if F[h_][w_] > F[h][w]: pattern[h][w]+=pattern[h_][w_]
    if pattern[h][w]>mod: pattern[h][w]%=mod

    for i in range(4):
      h_ = h+dh[i]
      w_ = w+dw[i]
      if F[h_][w_] == 0: continue
      if F[h_][w_] < F[h][w]:
        for i in range(4):
          h__ = h_+dh[i]
          w__ = w_+dw[i]
          if F[h__][w__] == 0: continue
          if F[h__][w__] <= F[h_][w_]: continue
          if pattern[h__][w__] == 0: break
        else:
          nexts.append((h_, w_))
  
  # print(*pattern, sep="\n")
  ans = 0
  for h in range(H):
    for w in range(W):
      ans+=pattern[h][w]
      if ans >= mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()