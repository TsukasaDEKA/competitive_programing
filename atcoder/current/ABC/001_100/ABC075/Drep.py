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
1 4
3 3
6 2
8 1"""
        output = """21"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 2
0 0
1 1
2 2
3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 3
-1000000000 -1000000000
1000000000 1000000000
-999999999 999999999
999999999 -999999999"""
        output = """3999999996000000001"""
        self.assertIO(input, output)

def resolve():
  inf = 10**32+1
  N, K = map(int, input().split(" "))
  A = [[int(x) for x in input().split(" ")] for _ in range(N)]
  ans = inf
  for i in range(N-1):
    x, _ = A[i]
    for i_ in range(i+1, N):
      x_, _ = A[i_]
      min_x, max_x = min(x, x_), max(x, x_)

      for j in range(N-1):
        _, y = A[j]
        for j_ in range(j+1, N):
          _, y_ = A[j_]
          min_y, max_y = min(y, y_), max(y, y_)

          count = 0
          for x__, y__ in A:
            if min_x <= x__ and x__ <= max_x and min_y <= y__ and y__ <= max_y: count+=1

          # print(x, x_, y, y_, A[j], A[j_], count)
          if count < K: continue
          ans = min(abs(x-x_)*abs(y-y_), ans)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()