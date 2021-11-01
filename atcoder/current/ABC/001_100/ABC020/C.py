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


dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]

def resolve():
  from collections import deque
  # H*W <= 100 なので O(log(T)*(H*W)**2) とかでも間に合うかも。
  # 答えを二分探索する。
  inf = 10**18+1
  H, W, T = map(int, input().split(" "))
  S = [list(input())+["#"] for _ in range(H)]+[["#"]*(W+1)]
  start = goal = None
  for h in range(H):
    for w in range(W):
      if S[h][w] == "S": start = (h, w)
      if S[h][w] == "G": goal = (h, w)

  # メグル式二分探索。
  def binary_search(ok, ng, solve):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid): ok = mid
      else: ng = mid
    return ok
  
  def solve(x):
    # ここは計算量が重そうだけど、実際は O(H*W) 程度のはず。
    nexts = deque()
    nexts.append(start)
    times = [[inf]*W+[0] for _ in range(H)]+[[0]*(W+1)]
    times[start[0]][start[1]] = 0
    while nexts:
      h, w = nexts.popleft()
      for i in range(4):
        h_ = h+dh[i]
        w_ = w+dw[i]

        cost = x if S[h_][w_] == "#" else 1
        if times[h][w]+cost > T: continue
        if times[h][w]+cost >= times[h_][w_]: continue
        times[h_][w_] = times[h][w]+cost
        nexts.append((h_, w_))
    return times[goal[0]][goal[1]] <= T

  print(binary_search(1, T+1, solve))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()