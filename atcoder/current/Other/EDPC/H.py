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
        input = """3 4
...#
.#..
...."""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2
..
#.
..
.#
.."""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
..#..
.....
#...#
.....
..#.."""
        output = """24"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """20 20
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
...................."""
        output = """345263555"""
        self.assertIO(input, output)

def resolve():
  # 普通に二次元 DP
  mod = 10**9+7
  H, W = map(int, input().split(" "))
  grid = [list(input()) for _ in range(H)]

  dp = [[0]*W for _ in range(H)]
  dp[0][0] = 1
  for h in range(H):
    for w in range(W):
      if grid[h][w]=="#" or (h==0 and w==0): continue
      up   = dp[h-1][w] if h!=0 else 0
      left = dp[h][w-1] if w!=0 else 0
      dp[h][w] = up + left
  print(dp[-1][-1]%mod)

resolve()

if __name__ == "__main__":
    unittest.main()
