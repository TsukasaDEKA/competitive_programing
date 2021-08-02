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
        input = """3 2
3 3
5 5
9 2
11 2
5 5
3 3"""
        output = """Yes
2 6 1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
3 3
5 5
9 2
11 1000000000
5 5
3 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20 774
540130346 269080121
139837096 165633078
731188937 784167460
18996195 52176517
153153670 738204723
179733158 825294112
698198250 713974773
449248931 563096572
249863070 242694893
428066819 476630383
554127636 460973490
389988495 32320086
889782910 956212985
43905938 212030305
638141790 667879166
985957895 358743012
971007109 827787244
804625543 141347414
905270323 167192824
614855582 963943648
179733932 825294886
731188163 784166686
153154444 738205497
554128410 460973490
804626317 141348188
449249705 563096572
540129572 269079347
638142564 667878392
614855582 963944422
18996969 52177291
971007109 827788018
889782910 956213759
43906712 212031079
389987721 32319312
139836322 165633078
428067593 476631157
905271097 167192824
249862296 242694893
985958669 358742238
698199024 713975547"""
        output = """Yes
6 5 6 2 2 2 2 1 5 2 1 6 3 2 8 8 3 2 1 3"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
import numpy as np
from collections import deque
from heapq import heappop, heappush

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")


def resolve():
  # Ford_Fulkerson だと N**2 なので要素数が多い時に間に合わない。
  from collections import defaultdict
  dx = [-1,  0,  1, -1, 1, -1, 0, 1]
  dy = [-1, -1, -1,  0, 0,  1, 1, 1]

  def maximum_flow(graph, start, goal):
    INF = 1 << 30
    n = len(graph)
    max_flow = 0
    while True:
      # パスを見つける。n のサイズ次第では実行時間長めになるかもしれない。
      visited = [0] * n
      stack = [start]
      last = [None] * n
      while stack:
        x = stack.pop()
        visited[x] = 1
        if x == goal:
          break
        for y in graph[x].keys():
          if visited[y] or graph[x][y] == 0:
            continue
          stack.append(y)
          last[y] = x
      # パスが見つからなかったら終了
      if x != goal:
        break

      # 経路上の最小容量を出す。
      # last に記録してある経路を逆に辿っていっている。
      y = goal
      min_capacity = INF
      while last[y] is not None:
        x = last[y]
        min_capacity = min(min_capacity, graph[x][y])
        y = x

      # last に記録してある経路を逆に辿りながら、逆辺と順辺を入れ替えている。
      y = goal
      while last[y] is not None:
        x = last[y]
        graph[x][y] -= min_capacity
        graph[y][x] += min_capacity
        y = x
      max_flow += min_capacity
    return max_flow
  # A, B 間のマッチング問題から最大流問題に帰着する。
  # どの点にマッチする可能性があるのかをチェックするのが結構難しそう。
  inf = 10**18+1
  N, T = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  B = [[int(x) for x in input().split(" ")] for _ in range(N)]

  # 経路。
  # 0~N-1: A, N~2N-1: B、2N: source, 2N+1: sink
  graph = [defaultdict(int) for _ in range(2*(N+1))]
  for i in range(N):
    graph[2*N][i] = 1
    # graph[i][2*N] = 0
    graph[N+i][2*N+1] = 1
    # graph[2*N+1][N+i] = 0

  PATH = defaultdict(set)
  for a in range(N):
    x, y = A[a]
    for j in range(8):
      x_ = x+dx[j]*T
      y_ = y+dy[j]*T
      if x_ >= 0 and x_ <= 10**9 and y_ >= 0 and y_ <= 10**9:
        PATH[(x_, y_)].add(a)

  for b in range(N):
    x, y = B[b]
    for a in PATH[(x, y)]:
      graph[a][N+b] = 1
      # graph[N+b][a] = 0

  flow = maximum_flow(graph, 2*N, 2*N+1)
  if flow != N:
    print("No")
    return

  connects = [[a for a, v in g.items() if v > 0] for g in graph[N:2*N]]
  direct = [[6, 7, 8], [5, 0, 1], [4, 3, 2]]
  ans = [0]*N
  for b in range(N):
    a = connects[b][0]
    x_b, y_b = B[b]
    x_a, y_a = A[a]
    d_x = d_y = 0
    if x_b-x_a != 0:
      d_x = (x_b-x_a)//abs(x_b-x_a)
    if y_b-y_a != 0:
      d_y = (y_b-y_a)//abs(y_b-y_a)
    # print(d_x, d_y)
    ans[a] = direct[d_y+1][d_x+1]
  print("Yes")
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()