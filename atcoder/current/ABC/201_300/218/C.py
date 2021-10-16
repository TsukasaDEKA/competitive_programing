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
        input = """5
.....
..#..
.###.
.....
.....
.....
.....
....#
...##
....#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
#####
##..#
#..##
#####
.....
#####
#..##
##..#
#####
....."""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
#...
..#.
..#.
....
#...
#...
..#.
...."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4
#...
.##.
..#.
....
##..
#...
..#.
...."""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  def moveToLeftTop(X, N):
    # X の # を全部左上に寄せる。
    min_X_h = N+1
    min_X_w = N+1
    for h in range(N):
      for w in range(N):
        if X[h][w] == "#":
          min_X_h = min(min_X_h, h)
          min_X_w = min(min_X_w, w)
    for h in range(N):
      for w in range(N):
        if X[h][w] == "#":
          X[h][w] = "."
          X[h-min_X_h][w-min_X_w] = "#"
    return X

  N = int(input())
  S = [list(input()) for _ in range(N)]
  T = moveToLeftTop([list(input()) for _ in range(N)], N)

  for _ in range(4):
    # S を回転して # を全部左上に寄せる。
    S = moveToLeftTop([[S[w][N-1-h] for w in range(N)] for h in range(N)], N)
    if S == T:
      print("Yes")
      return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()