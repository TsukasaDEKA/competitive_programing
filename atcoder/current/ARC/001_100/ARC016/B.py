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
        input = """15
.........
.x.......
.........
...x.....
.........
.......o.
.......o.
.......o.
.........
..x.....o
........o
........o
....x...o
.x......o
........o"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
..o..x.o.
..o..x.o.
..x..o.o.
..o..o.o.
..o..x.o.
..o..x.o."""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
.........
........."""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  X = [["."]*9]+[list(input()) for _ in range(N)]
  ans = 0
  for i in range(1, N+1):
    for j in range(9):
      if X[i][j] == "x": ans += 1
      if X[i][j] == "o" and X[i-1][j] != "o":
        ans+=1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()