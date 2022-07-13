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

# ↓をほぼ写経
# https://vartkw.hatenablog.com/entry/2016/12/02/002703
from collections import deque
class Dinic():
  # n: 要素数
  # start, goal: 始点と終点のノード番号。
  def __init__(self, n):
    self.n = n
    self.inf = 100000000000
    self.glaph = [[] for _ in range(n)]
    self.level = [0]*n
    self.iter = [0]*n

  # 辺の追加。
  # from_: 辺の開始点
  # to_: 行先
  # cap: 容量
  def add_edge(self, from_, to_, cap):
    self.glaph[from_].append({'to': to_, 'cap': cap, 'rev': len(self.glaph[to_])})
    self.glaph[to_].append({'to': from_, 'cap': 0, 'rev': len(self.glaph[from_])-1})

  # start からの最短経路を bfs で計算
  def bfs(self, start):
    # 幅優先探索を行い start => goal までの level (使用する辺の数) を設定する。
    self.level = [-1]*self.n
    self.level[start] = 0
    nexts = deque()
    nexts.append(start)
    
    while nexts:
      current = nexts.popleft()
      for e in self.glaph[current]:
        # 容量が残ってて (e['cap'] > 0) かつ、まだ深さが決まってない (self.level[e['to']] < 0) ノードだけ深さを決める。
        if e['cap'] > 0 and self.level[e['to']] < 0:
          self.level[e['to']] = self.level[current]+1
          nexts.append(e['to'])

  # 増加バスをdfsで探す
  # TODO : 非再帰で書き直す
  def dfs(self, v, goal, flow):
    if v==goal: return flow
    for i in range(self.iter[v], len(self.glaph[v])):
      # これは何？このタイミングで range の値変更してると怖くない？
      self.iter[v] = i
      e = self.glaph[v][i]
      if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
        # 再起的に流量を求める。
        f = self.dfs(e['to'], goal, min(flow, e['cap']))
        if f > 0:
          e['cap'] -= f
          self.glaph[e['to']][e['rev']]['cap'] += f
          return f
    return 0

  def max_flow(self, start, goal):
    flow = 0
    while True:
      self.bfs(start)
      # bfs でたどり着けない場合、それで計算を打ち切る。
      if self.level[goal] < 0: return flow
      self.iter = [0]*self.n
      f = self.dfs(start, goal, self.inf)
      while f > 0:
        flow += f
        f = self.dfs(start, goal, self.inf)

def resolve():
  # Ford_Fulkerson だと N**2 なので要素数が多い時に間に合わない。
  from collections import defaultdict
  dx = [-1,  0,  1, -1, 1, -1, 0, 1]
  dy = [-1, -1, -1,  0, 0,  1, 1, 1]
  # A, B 間のマッチング問題から最大流問題に帰着する。
  # どの点にマッチする可能性があるのかをチェックするのが結構難しそう。
  inf = 10**18+1
  N, T = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  B = [[int(x) for x in input().split(" ")] for _ in range(N)]

  PATH = defaultdict(set)
  for a in range(N):
    x, y = A[a]
    for j in range(8):
      x_ = x+dx[j]*T
      y_ = y+dy[j]*T
      if x_ >= 0 and x_ <= 10**9 and y_ >= 0 and y_ <= 10**9:
        PATH[(x_, y_)].add(a)

  # 経路。
  # 0~N-1: A, N~2N-1: B、2N: source, 2N+1: sink
  denic = Dinic(2*(N+1))
  for b in range(N):
    x, y = B[b]
    for a in PATH[(x, y)]:
      denic.add_edge(a, N+b, 1)

  # start => a の辺と b => goal の辺を追加する。
  for i in range(N):
    denic.add_edge(2*N, i, 1)
    denic.add_edge(N+i, 2*N+1, 1)

  flow = denic.max_flow(2*N, 2*N+1)
  if flow != N:
    print("No")
    return

  # a => b の連結を複合して向きに変更する。
  direct = [[6, 7, 8], [5, 0, 1], [4, 3, 2]]
  print("Yes")
  ans = [0]*N
  for i in range(N):
    x_a, y_a = A[i]
    b = 0
    for e in denic.glaph[i]:
      if e['cap'] == 0:
        b = e['to']
        break
    x_b, y_b = B[b-N]
    d_x = d_y = 0
    if x_b-x_a > 0: d_x = 1
    if x_b-x_a < 0: d_x = -1
    if y_b-y_a > 0: d_y = 1
    if y_b-y_a < 0: d_y = -1
    ans[i] = direct[d_y+1][d_x+1]
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()