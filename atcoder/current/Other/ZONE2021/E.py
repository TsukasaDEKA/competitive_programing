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
        input = """3 3
10 1
10 10
1 10
1 10 1
1 10 1"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 11
42 77 94 76 40 66 43 28 66 23
27 34 41 31 83 13 64 69 81 82
23 81 0 22 39 51 4 37 84 43
62 37 82 86 26 67 45 78 85 2
79 18 72 62 68 84 69 88 19 48
0 27 21 51 71 13 87 45 39 11
74 57 32 0 97 41 87 96 17 98
69 58 76 32 51 16 38 68 86 82 64
53 47 33 7 51 75 43 14 96 86 70
80 58 12 76 94 50 59 2 1 54 25
14 14 62 28 12 43 15 70 65 44 41
56 50 50 54 53 34 16 3 2 59 88
27 85 50 79 48 86 27 81 78 78 64"""
        output = """498"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0 0
0 0 0 0
0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  R, C = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(R)]
  B = [[int(x) for x in input().split(" ")] for _ in range(R-1)]

  PATH = [[set() for _ in range(C)] for _ in range(R)]
  for r in range(R):
    for c in range(C):
      for i in range(4):
        if c+1 <  C: PATH[r][c].add((A[r][c], (r, c+1)))
        if c-1 >= 0: PATH[r][c].add((A[r][c-1], (r, c-1)))
        if r+1 < R: PATH[r][c].add((B[r][c], (r+1, c)))
        if r-1 >= 0: PATH[r][c].add((1, (r, c+1)))
          
  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()
