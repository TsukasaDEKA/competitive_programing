import re
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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 1
#"""
        output = """No"""
        self.assertIO(input, output)

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]

def resolve():
  H, W = map(int, input().split(" "))
  FIELD = [list(input())+["."] for _ in range(H)]+[["."]*(W+1)]

  for h in range(H):
    for w in range(W):
      if FIELD[h][w] == ".": continue
      for i in range(4):
        h_ = h+dh[i]
        w_ = w+dw[i]
        if FIELD[h_][w_] == "#":
          break
      else:
        print("No")
        return
  print("Yes")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()