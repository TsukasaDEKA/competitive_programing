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
        input = """10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2"""
        output = """10"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  P = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])
  set_P = set([(x, y) for x, y in P])

  ans = 0
  for i in range(N-1):
    x_i, y_i = P[i]
    for j in range(i+1, N):
      x_j, y_j = P[j]
      P_1 = (x_i + (y_i - y_j), (x_j - x_i) + y_i)
      P_2 = (x_j + (y_i - y_j), (x_j - x_i) + y_j)
      if P_1 in set_P and P_2 in set_P:
        ans = max(ans, (x_i-x_j)**2 + (y_i-y_j)**2)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()