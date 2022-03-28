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
        input = """5 3 2
1 5 1 5"""
        output = """...#.
#.#..
.#...
#.#..
...#."""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3 3
4 5 2 5"""
        output = """#.#.
...#"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000000000000 999999999999999999 999999999999999999
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000"""
        output = """#.#
.#.
#.#"""
        self.assertIO(input, output)

def resolve():
  N, A, B = map(int, input().split(" "))
  P, Q, R, S = map(int, input().split(" "))
  ans = [["."]*(S-R+1) for _ in range(Q-P+1)]
  min_1 = max(1-A, 1-B)
  max_1 = min(N-A, N-B)
  min_2 = max(1-A, B-N)
  max_2 = min(N-A, B-1)
  for i in range(P, Q+1):
    k = i-A
    if k >= min_1 and k <= max_1:
      j = B+k
      if j >= R and j <= S:
        ans[i-P][j-R] = "#"
    
    if k >= min_2 and k <= max_2:
      j = B-k
      if j >= R and j <= S:
        ans[i-P][j-R] = "#"
  for a in ans:
    print(*a, sep="")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()