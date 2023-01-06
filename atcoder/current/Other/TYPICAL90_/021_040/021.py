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
        input = """4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 1
1 2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  # 強連結成分分解
  def scc(n, edge, directed=False, connection='strong'):
    # n は頂点数、edge は [[i, j],[k, l]] のような形式の配列
    from collections import Counter
    import numpy as np
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse import csr_matrix

    m = len(edge)
    edge_t = np.array(edge, dtype = np.int64).T
    tmp = np.ones(m, dtype = np.int64).T
    graph = csr_matrix((tmp, edge_t[:]), (n, n))

    # directed = True で有効グラフ
    # connection = 'strong' で強連結 (相互移動可能)
    return connected_components(graph, directed=directed, connection=connection)

  inf = 10**18+1
  from collections import Counter
  N, M = map(int, input().split(" "))
  EDGES = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  _, labels = scc(N, EDGES, directed=True)
  groups = Counter(labels)
  ans = 0
  for val in groups.values():
    if val < 2: continue
    ans+=val*(val-1)//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
