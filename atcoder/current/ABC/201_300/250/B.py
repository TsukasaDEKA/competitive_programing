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
        input = """4 3 2"""
        output = """..##..##
..##..##
..##..##
##..##..
##..##..
##..##..
..##..##
..##..##
..##..##
##..##..
##..##..
##..##.."""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 1 5"""
        output = """.....#####.....#####.....
#####.....#####.....#####
.....#####.....#####.....
#####.....#####.....#####
.....#####.....#####....."""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 4 1"""
        output = """.#.#
.#.#
.#.#
.#.#
#.#.
#.#.
#.#.
#.#.
.#.#
.#.#
.#.#
.#.#
#.#.
#.#.
#.#.
#.#."""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """1 4 4"""
        output = """....
....
....
...."""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, A, B = [int(x) for x in input().split(" ")]

  ans = [["."]*(B*N) for _ in range(A*N)]
  # print(ans, file=sys.stderr)
  for h in range(N):
    for w in range(N):
      if (h+w)%2==0: continue
      for a in range(A):
        for b in range(B):
          # print(A*h+a, B*w+b, file=sys.stderr)
          ans[A*h+a][B*w+b] = "#"

  for a in ans:
    print("".join(a))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()