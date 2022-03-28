from os import sep
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
  from collections import deque, defaultdict
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

  # トポロジカルソートをした後に頂点番号を振り直す。
  # ある頂点が複数の親を持っていた場合、新しい頂点番号が大きいものを選べば良い。
  # => トポロジカルソートをして頂点番号を振り直した時点で、より大きいものが子である。
  # => 元々あった根付き木に辺を足すとき、子孫に辺を繋ぐことか
  N, M = map(int, input().split(" "))
  IN_DEGREES = defaultdict(int)
  FROM = [[] for _ in range(N)]
  TO = [[] for _ in range(N)]
  for _ in range(N+M-1):
    A, B = [int(x)-1 for x in input().split(" ")]
    TO[A].append(B)
    FROM[B].append(A)
    IN_DEGREES[B]+=1

  topological_graph = topological_sort(N, IN_DEGREES, TO)

  conv = defaultdict(int)
  for i in range(N):
    conv[topological_graph[i]] = i

  ans = [0]*N
  for i in range(N):
    if len(FROM[i]) == 0: continue
    ans[i] = topological_graph[max([conv[x] for x in FROM[i]])]+1
  
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()