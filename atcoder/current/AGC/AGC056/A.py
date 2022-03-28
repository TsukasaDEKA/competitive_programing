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

#     def test_Sample_Input_1(self):
#         input = """6"""
#         output = """##..#.
# ##..#.
# ..##.#
# ..##.#
# ##...#
# ..###."""
#         self.assertIO(input, output)

    def test_Sample_Input_1(self):
        input = """19"""
        output = """"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20"""
        output = """"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """12"""
#         output = """##..#.
# ##..#.
# ..##.#
# ..##.#
# ##...#
# ..###."""
#         self.assertIO(input, output)

def resolve():
  N = int(input())
  ans = [["."]*N for _ in range(N)]
  for i in range(N):
    t = i*3+N%3
    for j in range(t, t+3):
      ans[i][j%N] = "#"

  if N%3:
    sep_line = (N//3)*2+(2-N%3)
    ans = ans[:sep_line] + [ans[-1]] + ans[sep_line:-1]

  for a in ans:
    print(*a, sep="")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()