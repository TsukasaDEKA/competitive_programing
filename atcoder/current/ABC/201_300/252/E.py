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
1 2 1
2 3 2
1 3 10"""
        output = """1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 6
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 1"""
        output = """3 1 2"""
        self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  inf = 10**18+1

  def dijkstra(start, dist, path, ans):
    candidate = [(0, start)]
    while candidate:
      cost, i = heappop(candidate)
      if cost > dist[i]:
        continue

      for c, j, k in path[i]:
        if cost+c >= dist[j]: continue
        dist[j] = cost+c
        ans[j] = k+1
        heappush(candidate, (cost+c, j))

  # 都市 1 からの距離だけを最初化すれば良い。
  # 最小グラフ
  # ダイクストラで通った辺だけを残したい。
  # ダイクストラで全ての辺を記録していく？
  N, M = map(int, input().split(" "))
  EDGES = [[] for _ in range(N)]
  for i in range(M):
    a, b, c = [int(x)-1 for x in input().split(" ")]
    EDGES[a].append((c+1, b, i))
    EDGES[b].append((c+1, a, i))


  ans = [-1]*N
  dijkstra(0, [inf]*N, EDGES, ans)
  print(*ans[1:])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()