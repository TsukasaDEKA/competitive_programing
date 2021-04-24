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
        input = """4 4
1 2 5
2 3 10
3 1 15
4 3 20"""
        output = """30
30
30
-1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 6
1 2 5
1 3 10
2 4 5
3 4 10
4 1 10
1 1 10"""
        output = """10
20
30
20"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 7
1 2 10
2 3 30
1 4 15
3 4 25
3 4 20
4 3 20
4 3 30"""
        output = """-1
-1
40
40"""
        self.assertIO(input, output)

def resolve():
  # i to j の最小コストを全て求める => 往復分の合計コストが出る。
  # ダイクストラでは？
  # 1 ~ N までの街に N+1 番目の街を付け加える。
  # N+1 番目の街に行く道は出発する街と同じ物にする。
  # その状態で 出発地点から N+1 番目の街の最短経路を求めれば良い。
  # 上手く枝切りをすれば O(M*logN) で計算できる。
  # 出発地点を全て使うので 全体だと O(N*M*logN)
  from heapq import heappop, heappush
  inf = 10**18+1

  N, M = map(int, input().split(" "))

  ROUTE = [set() for _ in range(N)]
  for _ in range(M):
    A, B, C = map(int, input().split(" "))
    ROUTE[A-1].add((C, B-1))

  for start in range(N):
    candidate = [(0, start)]
    distance = [inf]*(N+1)

    while candidate:
      cost, i = heappop(candidate)
      if cost > distance[i]: continue
      distance[i] = cost

      if i == N: continue
      for c, j in ROUTE[i]:
        if j == start: j = N
        if cost + c > distance[j]: continue
        heappush(candidate, (cost + c, j))
    print(distance[N] if distance[N] < inf else -1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
