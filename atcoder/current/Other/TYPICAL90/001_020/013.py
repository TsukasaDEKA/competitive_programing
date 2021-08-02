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
        input = """7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3"""
        output = """8
8
9
9
8
8
8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 2 1
2 3 10
3 4 100"""
        output = """111
111
111
111"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 3
1 2 314
1 3 159
1 4 265"""
        output = """265
893
583
265"""
        self.assertIO(input, output)

def resolve():
  # N が大きいのでワーシャルフロイドだと厳しそう。ダイクストラ？
  # マルチパスは無い。
  # ダイクストラで左右からの距離を求めて、足し算
  from heapq import heappop, heappush
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  PATH = [set() for _ in range(N)]

  for _ in range(M):
    A, B, C = [int(x)-1 for x in input().split(" ")]
    PATH[A].add((C+1, B))
    PATH[B].add((C+1, A))

  def dijkstra(start, dist):
    candidate = [(0, start)]

    while candidate:
      cost, i = heappop(candidate)
      if cost > dist[i]: continue
      dist[i] = cost

      for c, j in PATH[i]:
        if cost+c > dist[j]: continue
        heappush(candidate, (cost+c, j))


  from_0 = [inf]*N
  to_N = [inf]*N
  dijkstra(0, from_0)
  dijkstra(N-1, to_N)

  for i in range(N):
    print(from_0[i]+to_N[i])

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
