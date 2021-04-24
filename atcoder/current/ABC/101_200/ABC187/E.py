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

    def test_Sample_Input_1(self):
        input = """5
1 2
2 3
2 4
4 5
4
1 1 1
1 4 10
2 1 100
2 2 1000"""
        output = """11
110
1110
110
100"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
2 1
2 3
4 2
4 5
6 1
3 7
7
2 2 1
1 3 2
2 2 4
1 6 8
1 3 16
2 4 32
2 1 64"""
        output = """72
8
13
26
58
72
5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11
2 1
1 3
3 4
5 2
1 6
1 7
5 8
3 9
3 10
11 4
10
2 6 688
1 10 856
1 8 680
1 8 182
2 2 452
2 4 183
2 6 518
1 3 612
2 6 339
2 3 206"""
        output = """1657
1657
2109
1703
1474
1657
3202
1474
1247
2109
2559"""
        self.assertIO(input, output)

def resolve():
  # 愚直にやると間に合わない。
  # imos 的にできるようにグラフを書き換えることができれば、計算量をあまり増やさずにできる。
  # クエリの a, b の関係が、ルート側かそうでないかが解れば、imos 的に解ける。
  # N-1 辺なのでループは無い。
  # 頂点に自分の子を保持する方法は無いか

  inf = 10**10+1
  N = int(input())
  graph = [[] for _ in range(N)]
  A_B = []
  for _ in range(N-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    A_B.append((A, B))
    graph[A].append(B)
    graph[B].append(A)

  from collections import deque
  next_nodes = deque([0])
  # 適当な頂点を root にして、そこから親と子の関係を決めていく。
  childs = [set() for _ in range(N)]
  checked = [False]*N
  checked[0] = True
  while next_nodes:
    current = next_nodes.popleft()
    for g in graph[current]:
      if checked[g]: continue
      childs[current].add(g)
      checked[g] = True
      next_nodes.append(g)

  imos_graph = [0]*N
  Q = int(input())
  for _ in range(Q):
    T, E, X = [int(x) for x in input().split(" ")]
    E-=1
    A, B = A_B[E]
    if T == 2: A, B = B, A

    if A in childs[B]:
      imos_graph[A]+=X
    else:
      imos_graph[0]+=X
      imos_graph[B]-=X

  # 根から配ってく。
  next_nodes = deque([0])
  # ans = [0]*N
  # ans[0] = imos_graph[0]
  while next_nodes:
    current = next_nodes.popleft()
    for c in childs[current]:
      imos_graph[c]+=imos_graph[current]
      next_nodes.append(c)
  print(*imos_graph, sep="\n")
resolve()

if __name__ == "__main__":
    unittest.main()
