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
        input = """2 1
1 2 2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3
1 2 2 3
1 2 2 1
1 1 1 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 2
1 2 3 4
3 4 5 6"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6 9
1 1 0 0
1 3 1 2
1 5 2 3
5 2 16 5
2 6 1 10
3 4 3 4
3 5 3 10
5 6 1 100
4 2 0 110"""
        output = """20"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  from math import sqrt, floor
  from heapq import heappop, heappush
  # 制約有のダイクストラっぽい
  # t 分待った方が早く抜けれる場合がある。
  # 今すぐ通り始めてから別の都市へ到着する時刻よりも待機時間が長くなってはしょうがない。
  # w := 待機時間として、w+[Di/((t+w)+1)] の最小値を求めたい。コストは毎回二分探索でいけるか？
  # 道のコストが時刻によって変化するのが厄介。
  # メグル式二分探索。
  N, M = map(int, input().split(" "))
  EDGES = [set() for _ in range(N)]
  for _ in range(M):
    A, B, C, D = map(int, input().split(" "))
    if A == B: continue
    A-=1
    B-=1
    EDGES[A].add((C, D, B))
    EDGES[B].add((C, D, A))

  candidate = [(0, 0)]
  dist = [inf]*N
  while candidate:
    cost, i = heappop(candidate)
    if cost > dist[i]: continue
    dist[i] = cost
    for c, d, j in EDGES[i]:
      # かかる時間
      cost = c + min(d//(dist[i]+1), d//(floor(sqrt(d))+1))
      if cost+dist[i] > dist[j]: continue
      # dist[j] = cost+dist[i]
      heappush(candidate, (cost+dist[i], j))

  # print(dist)
  print(-1 if dist[-1] >= inf else dist[-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
