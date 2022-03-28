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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)

def resolve():
  H, W = map(int, input().split(" "))
  FIELD = [list(input()) for _ in range(H)]
  good_rows = set()
  gdd_columns = set()
  for h in range(H):
    for w in range(W):
      if FIELD[h][w] == "#":
        good_rows.add(h)
        gdd_columns.add(w)

  good_rows = sorted(list(good_rows))
  gdd_columns = sorted(list(gdd_columns))
  H, W = len(good_rows), len(gdd_columns)
  ans = [["."]*W for _ in range(H)]
  for h in range(H):
    for w in range(W):
      ans[h][w] = FIELD[good_rows[h]][gdd_columns[w]]

  for a in ans:
    print("".join(a))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()