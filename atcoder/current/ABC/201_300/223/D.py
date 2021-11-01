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
        input = """4 3
2 1
3 4
2 4"""
        output = """2 1 3 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3
1 2
1 2
2 1"""
        output = """-1"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  from collections import defaultdict, deque

  def topological_sort(N, in_degrees, outs):
    topological_graph = []
    # 入次数 0 のノードから始める。
    c = [x for x in range(N) if in_degrees[x] == 0]
    nexts = []
    for i in c:
      heappush(nexts, i)

    while nexts:
      current = heappop(nexts)
      topological_graph.append(current)
      for tar in outs[current]:
        in_degrees[tar]-=1
        # 入次数が 0 だったら追加する。
        if in_degrees[tar]==0:
          heappush(nexts, tar)

    return topological_graph

  N, M = map(int, input().split(" "))
  EDGES = set()
  for i in range(M):
    x, y = [int(x)-1 for x in input().split(" ")]
    EDGES.add((x, y))

  out_ = [set() for _ in range(N)]
  in_degrees = defaultdict(int)

  for x, y in EDGES:
    out_[x].add(y)
    in_degrees[y]+=1

  for i in range(N):
    out_[i] = sorted(list(out_[i]))

  topological_graph = topological_sort(N, in_degrees, out_)
  if len(topological_graph) != N:
    print(-1)
    return

  ans = [x+1 for x in topological_graph]
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()