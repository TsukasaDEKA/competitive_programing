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
        input = """3 4
.#..
..#.
..##"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
."""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
.....
.....
.....
.....
....."""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  # DP
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  FIELD = [list(input()) for _ in range(H)]
  dp = [[0]*W+[-1] for _ in range(H)]+[[-1]*(W+1)]
  dp[0][0] = 1

  # print(*dp)
  for h in range(H):
    for w in range(W):
      if h == 0 and w == 0: continue
      if FIELD[h][w] == "#": continue

      temp = max(dp[h-1][w], dp[h][w-1])
      if temp <= 0: continue
      dp[h][w] = temp+1
  
  ans = 0
  for h in range(H):
    ans = max(ans, max(dp[h]))

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()