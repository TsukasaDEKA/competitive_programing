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
        input = """3
0 0
0 1
1 1"""
        output = """1.4142135624"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
315 271
-2 -621
-205 -511
-952 482
165 463"""
        output = """1455.7159750446"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt
  inf = 10**18+1
  N = int(input())
  P = [[int(x) for x in input().split(" ")] for _ in range(N)]
  ans = 0
  for i in range(N-1):
    x_i, y_i = P[i]
    for j in range(i+1, N):
      x_j, y_j = P[j]
      ans = max(ans, sqrt((x_j-x_i)**2 + (y_j-y_i)**2))


  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()