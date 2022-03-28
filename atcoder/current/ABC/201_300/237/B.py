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
        input = """4 3
1 2 3
4 5 6
7 8 9
10 11 12"""
        output = """1 4 7 10
2 5 8 11
3 6 9 12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
1000000000 1000000000
1000000000 1000000000"""
        output = """1000000000 1000000000
1000000000 1000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  H, W = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(H)]

  B = [[0]*H for _ in range(W)]
  for i in range(H):
    for j in range(W):
      B[j][i] = A[i][j]

  for b in B:
    print(*b, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()