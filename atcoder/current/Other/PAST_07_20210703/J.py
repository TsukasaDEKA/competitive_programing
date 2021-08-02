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
        input = """3 3
1 2
2 1
2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 7
2 4
2 8
7 3
6 1
8 4
8 3
5 3"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  from collections import deque, defaultdict
  # 閉ループが存在するかどうかを判定する。
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

  N, M = map(int, input().split(" "))

  out_ = defaultdict(list)
  in_degrees = defaultdict(int)

  for _ in range(M):
    a, b = [int(x)-1 for x in input().split(" ")]
    out_[a].append(b)
    in_degrees[b]+=1

  t_graph = topological_sort(N, in_degrees, out_)

  print("Yes" if len(t_graph) != N else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()