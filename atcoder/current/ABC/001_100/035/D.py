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
        input = """2 2 5
1 3
1 2 2
2 1 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2 3
1 3
1 2 2
2 1 1"""
        output = """3"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """8 15 120
# 1 2 6 16 1 3 11 9
# 1 8 1
# 7 3 14
# 8 2 13
# 3 5 4
# 5 7 5
# 6 4 1
# 6 8 17
# 7 8 5
# 1 4 2
# 4 7 1
# 6 1 3
# 3 1 10
# 2 6 5
# 2 4 12
# 5 1 30"""
#         output = """1488"""
#         self.assertIO(input, output)

def resolve():
  from heapq import heappop, heappush
  def dijkstra(start, dist, path):
    candidate = [(0, start)]

    while candidate:
      cost, i = heappop(candidate)
      if cost > dist[i]: continue
      dist[i] = cost

      for c, j in path[i]:
        if cost+c > dist[j]: continue
        heappush(candidate, (cost+c, j))

  # 街 1 と街 i を往復する時間を ti とすると、得られる金額は A[i]*(T-ti)
  # 街 1 と全ての街まで往復する時間を求めることができれば良さそう。
  # 行きは普通にダイクストラ法、帰りは有向辺を逆順にしてダイクストラ法をやれば良さそう？
  inf = 10**18+1
  N, M, T = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  EDGES = [[] for _ in range(N)]
  REV_EDGES = [[] for _ in range(N)]
  for _ in range(M):
    a, b, c = [int(x) for x in input().split(" ")]
    a, b = a-1, b-1
    EDGES[a].append((c, b))
    REV_EDGES[b].append((c, a))

  outbounds = [inf]*N
  dijkstra(0, outbounds, EDGES)
  inbounds = [inf]*N
  dijkstra(0, inbounds, REV_EDGES)

  ans = 0
  for i in range(N):
    ans = max(ans, (T-outbounds[i]-inbounds[i])*A[i])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()