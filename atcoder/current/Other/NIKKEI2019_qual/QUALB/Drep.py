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
        input = """3 1
1 2
1 3
2 3"""
        output = """0
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 3
2 1
2 3
4 1
4 2
6 1
2 6
4 6
6 5"""
        output = """6
4
2
0
6
2"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict, deque

  def topological_sort(N, in_degrees, outs):
    topological_graph = []
    # 入次数 0 のノードから始める。
    nexts = deque(x for x in range(N) if in_degrees[x] == 0)
    while nexts:
      current = nexts.popleft()
      topological_graph.append(current)
      for tar in outs[current]:
        in_degrees[tar]-=1
        # 入次数が 0 だったら追加する。
        if in_degrees[tar]==0: nexts.append(tar)

    return topological_graph

  out_ = defaultdict(list)
  in_degrees = defaultdict(int)

  # 一旦
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A_B = [[int(x)-1 for x in input().split(" ")] for _ in range(N+M-1)]

  for i in range(N-1+M):
    x, y = A_B[i]
    out_[x].append(y)
    in_degrees[y]+=1

  topological_graph = topological_sort(N, in_degrees, out_)

  to_i = [0]*N
  for i in range(N):
    to_i[topological_graph[i]] = i

  A_B = [(to_i[a], to_i[b]) for a, b in A_B]

  parent = [-1]*N
  for a, b in A_B:
    parent[b] = max(a, parent[b])

  ans = [0]*N
  for i in range(N):
    p = parent[i]
    if p < 0: continue
    ans[topological_graph[i]] = topological_graph[p]+1
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()