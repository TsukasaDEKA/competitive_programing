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
        input = """5 5
1 2
2 3
3 4
4 2
4 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  import numpy as np
  def scc(n, edge, directed=False, connection='strong'):
    # n は頂点数、edge は [[i, j],[k, l]] のような形式の配列
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse import csr_matrix

    shiten, shuten, value = [], [], []
    for e_s, e_t in edge:
      shiten.append(e_s)
      shuten.append(e_t)
      value.append(1)
    graph = csr_matrix((value, (shiten, shuten)), (n, n))

    # directed = True で有効グラフ
    # connection = 'strong' で強連結 (相互移動可能)
    return connected_components(graph, directed=directed, connection=connection)

  # 閉路の数を求める問題になりそう。
  # SCC だって。
  from collections import Counter, deque
  N, M = map(int, input().split(" "))
  EDGES = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  group, table = scc(N, EDGES, directed=True)

  count = Counter(table)

  # 複数頂点を持つ強連結成分については -1 ラベル (その頂点から開始した時に無限に移動できる) をつけておく。
  for i in range(N):
    if count[table[i]] > 1:
      table[i] = -1
  
  # 有向辺を逆走する経路
  REV_EDGES = [[] for _ in range(N)]
  for u, v in EDGES:
    REV_EDGES[v].append(u)

  for i in range(N):
    if table[i] >= 0: continue

    nexts = deque([i])
    while nexts:
      current = nexts.pop()
      for n in REV_EDGES[current]:
        if table[n] < 0: continue
        table[n] = -1
        nexts.append(n)

  print(np.count_nonzero(table == -1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()