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
        input = """2
1 1
2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 4
4 6
7 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 1
1 2
2 1
2 2"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  # N がとても小さい。
  # p, q を定めた時にどれくらいのコストがかかるのかというのは O(N**2) で求められる。(set を使えば O(N))
  # p, q の候補は O(N**2) で算出できる。
  N = int(input())
  X_Y = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])
  ans = N
  for i in range(N-1):
    x1, y1 = X_Y[i]
    for j in range(i+1, N):
      x2, y2 = X_Y[j]
      p, q = x1-x2, y1-y2
      temp = N
      for i_ in range(N-1):
        x1_, y1_ = X_Y[i_]
        for j_ in range(i+1, N):
          x2_, y2_ = X_Y[j_]
          if x1_-p == x2_ and y1_-q == y2_:
            temp -= 1
      ans = min(ans, temp)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()