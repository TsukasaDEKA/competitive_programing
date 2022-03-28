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
        input = """4 4
10 8 12 5
1 2
1 3
2 3
3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
0 10
1 2"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1

  from heapq import heappop, heappush
  def dijkstra(start, dist, path):
    candidate = [(0, start)]

    while candidate:
      cost, i = heappop(candidate)
      if cost >= dist[i]: continue
      dist[i] = cost

      for c, j in path[i]:
        if cost+c > dist[j]: continue
        heappush(candidate, (cost+c, j))

  N, M = map(int, input().split(" "))
  H = [int(x) for x in input().split(" ")]

  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    U, V = [int(x)-1 for x in input().split(" ")]
    diff = H[U] - H[V]
    # 常に U 側が高い
    if diff < 0:
      diff *= -1
      U, V = V, U
    
    # 楽しさ + 標高を考えると、低い方に移動する場合はコストが変わらない。
    EDGES[U].append((0, V))
    EDGES[V].append((diff, U))

  dist = [inf]*N
  dijkstra(0, dist, EDGES)
  start = H[0]
  ans = -min([H[i]+dist[i]-start for i in range(N)])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()