import sys
from io import StringIO
from tabnanny import check
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
        input = """2 3 10
S##
.#G"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4 7
S##G
.##.
..#."""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4 1000000000
S###
####
####
###G"""
        output = """199999999"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]

  from collections import deque
  from heapq import heappop, heappush

  inf = 10**18+1
  # 二分探索
  H, W, T = map(int, input().split(" "))
  S = [list(input())+["#"] for _ in range(H)] + [["#"]*(W+1)]
  h_s, w_s = 0, 0
  h_g, w_g = 0, 0
  for h in range(H):
    for w in range(W):
      if S[h][w] == "S":
        h_s, w_s = h, w
      if S[h][w] == "G":
        h_g, w_g = h, w

  def dijkstra(x, dist):
    candidate = [(0, h_s, w_s)]

    while candidate:
      cost, h, w = heappop(candidate)
      if cost > dist[h][w]: continue

      for i in range(4):
        h_ = h+dh[i]
        w_ = w+dw[i]
        if h_ < 0 or h_ >= H or w_ < 0 or w_ >= W: continue
        c = 1
        if S[h_][w_] == "#": c = x
        if cost+c >= dist[h_][w_]: continue
        dist[h_][w_] = cost+c
        heappush(candidate, (cost+c, h_, w_))

  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid

    return ok

  def solve(x):
    dist = [[inf]*W for _ in range(H)]
    dijkstra(x, dist)
    return dist[h_g][w_g] <= T

  print(binary_search(1, inf, solve))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()